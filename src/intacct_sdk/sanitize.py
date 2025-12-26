from __future__ import annotations

from typing import Iterable
from xml.etree import ElementTree as ET


_REDACTED = "***REDACTED***"


SENSITIVE_TAGS = {
    "senderid",
    "userid",
    "companyid",
    "password",
    "sessionid",
    "accountno",
    "bankaccountno",
    "routingnumber",
    "ssn",
    "taxid",
    "accountnumber",
}


SENSITIVE_ATTRS = {
    "key",
    "sessionid",
}


def sanitize_xml(xml_bytes: bytes, extra_tags: Iterable[str] | None = None) -> bytes:
    root = ET.fromstring(xml_bytes)
    tags = set(SENSITIVE_TAGS)
    if extra_tags:
        tags.update(tag.lower() for tag in extra_tags)

    for elem in root.iter():
        if elem.tag.lower() in tags and elem.text:
            elem.text = _REDACTED
        for attr in list(elem.attrib):
            if attr.lower() in SENSITIVE_ATTRS:
                elem.attrib[attr] = _REDACTED

    return ET.tostring(root, encoding="UTF-8", xml_declaration=True)
