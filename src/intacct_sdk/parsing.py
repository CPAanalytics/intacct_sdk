from __future__ import annotations

from typing import Dict, List, Optional
from xml.etree import ElementTree as ET

from .errors import IntacctError
from .models import QueryResult, Record, ResultData, Session


def parse_session(xml_body: bytes) -> Session:
    root = ET.fromstring(xml_body)
    _raise_on_failure(root)

    session_id = _get_text(root, "operation/result/data/api/sessionid")
    endpoint = _get_text(root, "operation/result/data/api/endpoint")
    if not session_id or not endpoint:
        raise IntacctError("Missing session data in response")
    return Session(session_id=session_id, endpoint=endpoint)


def parse_read_by_query(xml_body: bytes) -> QueryResult:
    root = ET.fromstring(xml_body)
    _raise_on_failure(root)

    data_node = root.find("operation/result/data")
    if data_node is None:
        return QueryResult(records=[], result_id=None, num_remaining=None, total_count=None)

    result_id = _get_text(data_node, "resultId")
    num_remaining = _get_int(data_node, "numremaining")
    total_count = _get_int(data_node, "totalcount")

    records: List[Record] = []
    for element in data_node:
        if element.tag in {"resultId", "numremaining", "totalcount"}:
            continue
        record = _element_to_record(element)
        if record.fields:
            records.append(record)

    return QueryResult(
        records=records,
        result_id=result_id,
        num_remaining=num_remaining,
        total_count=total_count,
    )


def parse_result_data(xml_body: bytes) -> ResultData:
    root = ET.fromstring(xml_body)
    _raise_on_failure(root)

    data_node = root.find("operation/result/data")
    if data_node is None:
        return ResultData(fields={}, raw_xml=None)

    fields = {}
    for child in list(data_node):
        if child.text is None:
            continue
        fields[child.tag] = child.text.strip()

    raw_xml = ET.tostring(data_node, encoding="unicode")
    return ResultData(fields=fields, raw_xml=raw_xml)


def _element_to_record(element: ET.Element) -> Record:
    fields: Dict[str, str] = {}
    raw: Dict[str, str] = {}
    for child in list(element):
        if list(child):
            raw[child.tag] = ET.tostring(child, encoding="unicode")
            continue
        if child.text is None:
            continue
        value = child.text.strip()
        fields[child.tag] = value
        raw[child.tag] = value
    return Record(fields=fields, raw=raw)


def _raise_on_failure(root: ET.Element) -> None:
    control_status = _get_text(root, "control/status")
    if control_status != "success":
        raise IntacctError("Control status not success", description=control_status)

    result_status = _get_text(root, "operation/result/status")
    if result_status != "success":
        error = root.find("operation/result/errormessage/error")
        description = _get_text(error, "description") if error is not None else None
        description2 = _get_text(error, "description2") if error is not None else None
        full_description = description or description2
        if description and description2 and description2 not in description:
            full_description = f"{description} | {description2}"
        raise IntacctError(
            "Result status not success",
            error_number=_get_text(error, "errorno") if error is not None else None,
            description=full_description,
            correction=_get_text(error, "correction") if error is not None else None,
            control_id=_get_text(root, "control/controlid"),
            operation_id=_get_text(root, "operation/result/controlid"),
        )


def _get_text(node: Optional[ET.Element], path: str) -> Optional[str]:
    if node is None:
        return None
    found = node.find(path)
    if found is None or found.text is None:
        return None
    return found.text.strip()


def _get_int(node: Optional[ET.Element], path: str) -> Optional[int]:
    text = _get_text(node, path)
    if text is None:
        return None
    try:
        return int(text)
    except ValueError:
        return None
