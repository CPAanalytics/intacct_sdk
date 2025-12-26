from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from xml.etree import ElementTree as ET

from intacct_sdk.config import IntacctConfig
from intacct_sdk.sanitize import sanitize_xml
from intacct_sdk.transport import HttpTransport
from intacct_sdk import xml as xml_builder


DOCS_DIR = Path(__file__).resolve().parents[1] / "Docs"
ENDPOINTS_PATH = DOCS_DIR / "endpoints.md"
FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "live"


@dataclass(frozen=True)
class Endpoint:
    operation: str
    object_name: str
    sdk_method: str


def _parse_env_file(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    values: Dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"").strip("'")
        values[key] = value
    return values


def _load_config_from_env() -> IntacctConfig:
    required = [
        "INTACCT_ENDPOINT_URL",
        "INTACCT_SENDER_ID",
        "INTACCT_SENDER_PASSWORD",
        "INTACCT_COMPANY_ID",
        "INTACCT_USER_ID",
        "INTACCT_USER_PASSWORD",
    ]
    if all(os.getenv(name) for name in required):
        return IntacctConfig.from_env()

    env_values = _parse_env_file(Path(".env"))
    mapping = {
        "INTACCT_ENDPOINT_URL": env_values.get("ENDPOINT_URl") or env_values.get("ENDPOINT_URL"),
        "INTACCT_SENDER_ID": env_values.get("SENDER_ID"),
        "INTACCT_SENDER_PASSWORD": env_values.get("SENDER_PASSWORD"),
        "INTACCT_COMPANY_ID": env_values.get("COMPANY_ID"),
        "INTACCT_USER_ID": env_values.get("USER_ID"),
        "INTACCT_USER_PASSWORD": env_values.get("USER_PASSWORD"),
    }
    for key, value in mapping.items():
        if value and not os.getenv(key):
            os.environ[key] = value

    return IntacctConfig.from_env()


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


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def _fixture_slug(endpoint: Endpoint) -> str:
    base = endpoint.sdk_method.replace(".", "_")
    return _slugify(f"{base}_{endpoint.operation}_{endpoint.object_name}")


def _is_success(response_xml: bytes) -> Tuple[bool, Optional[str], Optional[str], Optional[str]]:
    try:
        root = ET.fromstring(response_xml)
    except ET.ParseError:
        return False, None, None, None
    control_status = _get_text(root, "control/status")
    result_status = _get_text(root, "operation/result/status")
    if control_status == "success" and result_status == "success":
        return True, None, None, None
    error = root.find("operation/result/errormessage/error")
    return (
        False,
        _get_text(error, "errorno") if error is not None else None,
        _get_text(error, "description") if error is not None else None,
        _get_text(error, "correction") if error is not None else None,
    )


def _get_text(node: Optional[ET.Element], path: str) -> Optional[str]:
    if node is None:
        return None
    found = node.find(path)
    if found is None or found.text is None:
        return None
    return found.text.strip()


def _write_fixture(slug: str, request_xml: bytes, response_xml: bytes) -> None:
    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    request_out = FIXTURES_DIR / f"{slug}_request.xml"
    response_out = FIXTURES_DIR / f"{slug}_response.xml"
    request_out.write_bytes(sanitize_xml(request_xml))
    response_out.write_bytes(sanitize_xml(response_xml))


def _build_request_xml(
    config: IntacctConfig,
    control_id: str,
    session_id: Optional[str],
    endpoint: Endpoint,
    payloads: Dict[str, Tuple[Optional[list], Optional[dict]]],
) -> Tuple[bytes, str]:
    control = xml_builder.build_control(
        config.sender_id,
        config.sender_password,
        control_id,
    )
    if endpoint.sdk_method == "IntacctClient.get_api_session":
        auth = xml_builder.build_login_auth(
            config.user_id,
            config.company_with_slide_in(),
            config.user_password,
        )
        operation = xml_builder.build_get_api_session()
        function = xml_builder.build_function(control_id, operation)
        return xml_builder.build_request(control, auth, function), config.endpoint_url

    if not session_id:
        raise RuntimeError("Missing session_id for session-based operation")

    auth = xml_builder.build_session_auth(session_id)

    if endpoint.sdk_method.startswith("SessionClient."):
        method = endpoint.sdk_method.split(".", 1)[1]
        if method == "read_by_query":
            operation = xml_builder.build_read_by_query(
                endpoint.object_name,
                fields=["RECORDNO"],
                query="",
                page_size=1,
                offset=None,
            )
        elif method == "read":
            operation = xml_builder.build_read(endpoint.object_name, keys=["1"], fields=["RECORDNO"])
        elif method == "create":
            operation = xml_builder.build_create(endpoint.object_name, fields={"NAME": "Live Fixture"})
        elif method == "update":
            operation = xml_builder.build_update(endpoint.object_name, fields={"RECORDNO": "1"})
        elif method == "delete":
            operation = xml_builder.build_delete(endpoint.object_name, key_field="RECORDNO", key_value="1")
        else:
            raise RuntimeError(f"Unsupported SessionClient method {method}")
    elif endpoint.sdk_method.startswith("OperationClient."):
        payload, attrs = payloads.get(endpoint.operation, (None, None))
        operation = xml_builder.build_operation(endpoint.operation, payload, attrs=attrs)
    else:
        raise RuntimeError(f"Unsupported sdk method {endpoint.sdk_method}")

    function = xml_builder.build_function(control_id, operation)
    return xml_builder.build_request(control, auth, function), config.endpoint_url


def main() -> int:
    config = _load_config_from_env()
    transport = HttpTransport(
        timeout_seconds=config.timeout_seconds,
        max_retries=config.max_retries,
        backoff_seconds=config.backoff_seconds,
        logger=config.logger,
    )

    endpoints = _load_endpoints()
    payloads = _collect_operation_payloads()

    failures: List[Dict[str, Optional[str]]] = []

    session_id: Optional[str] = None
    session_endpoint: Optional[str] = None

    for index, endpoint in enumerate(endpoints, start=1):
        control_id = f"live-{index}"
        try:
            if endpoint.sdk_method == "IntacctClient.get_api_session":
                request_xml, url = _build_request_xml(config, control_id, None, endpoint, payloads)
                response_xml = transport.post(url, request_xml)
                _write_fixture(_fixture_slug(endpoint), request_xml, response_xml)
                ok, error_no, desc, correction = _is_success(response_xml)
                if ok:
                    root = ET.fromstring(response_xml)
                    session_id = _get_text(root, "operation/result/data/api/sessionid")
                    session_endpoint = _get_text(root, "operation/result/data/api/endpoint")
                else:
                    failures.append(
                        {
                            "endpoint": f"{endpoint.sdk_method}:{endpoint.operation}:{endpoint.object_name}",
                            "error_no": error_no,
                            "description": desc,
                            "correction": correction,
                        }
                    )
                continue

            if not session_id:
                raise RuntimeError("Session not established; get_api_session did not succeed")

            request_xml, url = _build_request_xml(config, control_id, session_id, endpoint, payloads)
            if session_endpoint:
                url = session_endpoint
            response_xml = transport.post(url, request_xml)
            _write_fixture(_fixture_slug(endpoint), request_xml, response_xml)

            ok, error_no, desc, correction = _is_success(response_xml)
            if not ok:
                failures.append(
                    {
                        "endpoint": f"{endpoint.sdk_method}:{endpoint.operation}:{endpoint.object_name}",
                        "error_no": error_no,
                        "description": desc,
                        "correction": correction,
                    }
                )
        except Exception as exc:  # noqa: BLE001 - keep running to capture all endpoints
            failures.append(
                {
                    "endpoint": f"{endpoint.sdk_method}:{endpoint.operation}:{endpoint.object_name}",
                    "error_no": None,
                    "description": str(exc),
                    "correction": None,
                }
            )

    summary_path = FIXTURES_DIR / "summary.json"
    summary_path.write_text(json.dumps({"failures": failures}, indent=2), encoding="utf-8")

    if failures:
        print(f"Recorded fixtures with {len(failures)} failures. See {summary_path}.")
    else:
        print(f"Recorded fixtures for {len(endpoints)} endpoints with no failures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
