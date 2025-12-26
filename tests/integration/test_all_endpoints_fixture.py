from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

from intacct_sdk import IntacctClient, IntacctConfig
from intacct_sdk.models import Session
from tests.utils import SequenceTransport, read_fixture


DOCS_DIR = Path(__file__).resolve().parents[1].parent / "Docs"
ENDPOINTS_PATH = DOCS_DIR / "endpoints.md"


@dataclass(frozen=True)
class Endpoint:
    operation: str
    object_name: str
    sdk_method: str


def _load_endpoints() -> List[Endpoint]:
    endpoints: List[Endpoint] = []
    for line in ENDPOINTS_PATH.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 5:
            continue
        operation, obj, sdk_method, _status, _tests = parts
        if operation == "Operation":
            continue
        endpoints.append(Endpoint(operation=operation, object_name=obj, sdk_method=sdk_method))
    return endpoints


def _element_to_payload(element: ET.Element):
    payload = []
    for child in list(element):
        value = None
        if list(child):
            value = _element_to_payload(child)
        else:
            if child.text and child.text.strip():
                value = child.text.strip()
        attrs = dict(child.attrib) if child.attrib else None
        payload.append((child.tag, value, attrs))
    return payload


def _collect_operation_payloads() -> Dict[str, Tuple[Optional[list], Optional[dict]]]:
    operations: Dict[str, Tuple[Optional[list], Optional[dict]]] = {}

    def extract(item):
        if "item" in item:
            for child in item["item"]:
                extract(child)
            return
        request = item.get("request") or {}
        body = (request.get("body") or {}).get("raw")
        if not body:
            return
        body = body.strip()
        if not body.startswith("<?xml") and "<request" not in body:
            return
        try:
            root = ET.fromstring(body)
        except ET.ParseError:
            return
        func = root.find(".//function")
        if func is None:
            return
        for child in list(func):
            payload = _element_to_payload(child)
            attrs = dict(child.attrib) if child.attrib else None
            operations.setdefault(child.tag, (payload, attrs))
            break

    for path in sorted(DOCS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for item in data.get("item", []):
            extract(item)

    return operations


def _build_session_client(responses: List[bytes]) -> Tuple[IntacctClient, Session, SequenceTransport]:
    transport = SequenceTransport(responses)
    config = IntacctConfig(
        endpoint_url="https://example.com/xmlgw.phtml",
        sender_id="SENDER",
        sender_password="PASSWORD",
        company_id="COMPANY",
        user_id="USER",
        user_password="USERPASS",
    )
    client = IntacctClient(config, transport=transport)
    session = Session(session_id="SESSION123", endpoint=config.endpoint_url)
    return client, session, transport


def _expected_operation_tag(method: str) -> str:
    if method == "read_by_query":
        return "readByQuery"
    return method


def _assert_request(endpoint: Endpoint, request_xml: bytes) -> None:
    root = ET.fromstring(request_xml)
    func = root.find(".//function")
    assert func is not None, "Missing function node"
    operation_node = next(iter(func), None)
    assert operation_node is not None, "Missing operation node"

    if endpoint.sdk_method.startswith("SessionClient."):
        method = endpoint.sdk_method.split(".", 1)[1]
        assert operation_node.tag == _expected_operation_tag(method)
        if method in {"create", "update", "delete"}:
            obj_node = operation_node.find(f"./{endpoint.object_name}")
            assert obj_node is not None
        elif method in {"read", "read_by_query"}:
            obj_node = operation_node.find("object")
            assert obj_node is not None
            assert (obj_node.text or "").strip() == endpoint.object_name
    elif endpoint.sdk_method.startswith("OperationClient."):
        assert operation_node.tag == endpoint.operation
    elif endpoint.sdk_method.startswith("IntacctClient."):
        assert operation_node.tag == endpoint.operation
    else:
        raise AssertionError(f"Unexpected sdk method {endpoint.sdk_method}")


def test_all_endpoints_fixture() -> None:
    endpoints = _load_endpoints()
    payloads = _collect_operation_payloads()

    responses: List[bytes] = []
    for endpoint in endpoints:
        if endpoint.sdk_method == "SessionClient.read_by_query":
            responses.append(read_fixture("read_by_query_response.xml"))
        elif endpoint.sdk_method == "IntacctClient.get_api_session":
            responses.append(read_fixture("get_api_session_response.xml"))
        else:
            responses.append(read_fixture("operation_success_response.xml"))

    client, session, transport = _build_session_client(responses)
    session_client = client.session_client(session)

    for index, endpoint in enumerate(endpoints, start=1):
        control_id = f"ctrl-{index}"
        if endpoint.sdk_method.startswith("SessionClient."):
            method = endpoint.sdk_method.split(".", 1)[1]
            if method == "read_by_query":
                result = session_client.read_by_query(
                    endpoint.object_name,
                    fields=["RECORDNO"],
                    control_id=control_id,
                )
                assert result.total_count == 2
            elif method == "read":
                result = session_client.read(
                    endpoint.object_name,
                    keys=["1"],
                    fields=["RECORDNO"],
                    control_id=control_id,
                )
                assert result.fields.get("key") == "KEY-1"
            elif method == "create":
                result = session_client.create(
                    endpoint.object_name,
                    fields={"NAME": "Example"},
                    control_id=control_id,
                )
                assert result.fields.get("key") == "KEY-1"
            elif method == "update":
                result = session_client.update(
                    endpoint.object_name,
                    fields={"RECORDNO": "1"},
                    control_id=control_id,
                )
                assert result.fields.get("key") == "KEY-1"
            elif method == "delete":
                result = session_client.delete(
                    endpoint.object_name,
                    key_field="RECORDNO",
                    key_value="1",
                    control_id=control_id,
                )
                assert result.fields.get("key") == "KEY-1"
            else:
                raise AssertionError(f"Unhandled method {method}")
        elif endpoint.sdk_method.startswith("OperationClient."):
            method = endpoint.sdk_method.split(".", 1)[1]
            payload, attrs = payloads.get(endpoint.operation, (None, None))
            result = getattr(session_client.operations, method)(
                payload=payload,
                operation_attrs=attrs,
                control_id=control_id,
            )
            assert result.fields.get("key") == "KEY-1"
        elif endpoint.sdk_method.startswith("IntacctClient."):
            method = endpoint.sdk_method.split(".", 1)[1]
            assert method == "get_api_session"
            session_result = client.get_api_session(control_id=control_id)
            assert session_result.session_id == "SESSION123"
        else:
            raise AssertionError(f"Unexpected sdk method {endpoint.sdk_method}")

        request_xml = transport.requests[-1][1]
        _assert_request(endpoint, request_xml)
