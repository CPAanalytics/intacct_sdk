from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union
from xml.etree import ElementTree as ET


DTD_VERSION = "3.0"


def build_control(sender_id: str, sender_password: str, control_id: str) -> ET.Element:
    control = ET.Element("control")
    ET.SubElement(control, "senderid").text = sender_id
    ET.SubElement(control, "password").text = sender_password
    ET.SubElement(control, "controlid").text = control_id
    ET.SubElement(control, "uniqueid").text = "false"
    ET.SubElement(control, "dtdversion").text = DTD_VERSION
    ET.SubElement(control, "includewhitespace").text = "false"
    return control


def build_login_auth(user_id: str, company_id: str, user_password: str) -> ET.Element:
    authentication = ET.Element("authentication")
    login = ET.SubElement(authentication, "login")
    ET.SubElement(login, "userid").text = user_id
    ET.SubElement(login, "companyid").text = company_id
    ET.SubElement(login, "password").text = user_password
    return authentication


def build_session_auth(session_id: str) -> ET.Element:
    authentication = ET.Element("authentication")
    ET.SubElement(authentication, "sessionid").text = session_id
    return authentication


def build_function(control_id: str, body: ET.Element) -> ET.Element:
    function = ET.Element("function", {"controlid": control_id})
    function.append(body)
    return function


def build_request(control: ET.Element, authentication: ET.Element, function: ET.Element) -> bytes:
    root = ET.Element("request")
    root.append(control)

    operation = ET.SubElement(root, "operation")
    operation.append(authentication)

    content = ET.SubElement(operation, "content")
    content.append(function)

    return ET.tostring(root, encoding="UTF-8", xml_declaration=True)


def build_get_api_session() -> ET.Element:
    return ET.Element("getAPISession")


def build_read_by_query(
    object_name: str,
    fields: Iterable[str],
    query: str = "",
    page_size: int = 100,
    offset: Optional[int] = None,
) -> ET.Element:
    read_by_query = ET.Element("readByQuery")
    ET.SubElement(read_by_query, "object").text = object_name
    ET.SubElement(read_by_query, "fields").text = ",".join(fields)
    ET.SubElement(read_by_query, "query").text = query
    ET.SubElement(read_by_query, "pagesize").text = str(page_size)
    if offset is not None:
        ET.SubElement(read_by_query, "offset").text = str(offset)
    return read_by_query


def build_read(object_name: str, keys: Iterable[str], fields: Iterable[str]) -> ET.Element:
    read = ET.Element("read")
    ET.SubElement(read, "object").text = object_name
    keys_node = ET.SubElement(read, "keys")
    for key in keys:
        ET.SubElement(keys_node, "key").text = key
    ET.SubElement(read, "fields").text = ",".join(fields)
    return read


def build_create(object_name: str, fields: Dict[str, str]) -> ET.Element:
    create = ET.Element("create")
    payload = ET.SubElement(create, object_name)
    _append_fields(payload, fields)
    return create


def build_update(object_name: str, fields: Dict[str, str]) -> ET.Element:
    update = ET.Element("update")
    payload = ET.SubElement(update, object_name)
    _append_fields(payload, fields)
    return update


def build_delete(object_name: str, key_field: str, key_value: str) -> ET.Element:
    delete = ET.Element("delete")
    payload = ET.SubElement(delete, object_name)
    ET.SubElement(payload, key_field).text = key_value
    return delete


def _append_fields(target: ET.Element, fields: Dict[str, str]) -> None:
    for key, value in fields.items():
        ET.SubElement(target, key).text = value


PayloadEntry = Tuple[str, "PayloadValue", Optional[Dict[str, str]]]
Payload = Sequence[PayloadEntry]
PayloadValue = Union[str, None, Payload]


def build_operation(
    operation: str,
    payload: Optional[Payload] = None,
    attrs: Optional[Dict[str, str]] = None,
) -> ET.Element:
    element = ET.Element(operation, attrs or {})
    if payload:
        _append_payload(element, payload)
    return element


def _append_payload(target: ET.Element, payload: Payload) -> None:
    for entry in payload:
        if len(entry) == 2:
            tag, value = entry
            attrs = None
        else:
            tag, value, attrs = entry
        child = ET.SubElement(target, tag, attrs or {})
        if isinstance(value, list) or isinstance(value, tuple):
            _append_payload(child, value)
        elif value is not None:
            child.text = str(value)
