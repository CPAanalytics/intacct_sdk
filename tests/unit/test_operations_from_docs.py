from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Tuple
from xml.etree import ElementTree as ET

import pytest

from intacct_sdk import xml as xml_builder


DOCS_DIR = Path(__file__).resolve().parents[1].parent / "Docs"


def _sort_attribs(element: ET.Element) -> None:
    if element.attrib:
        element.attrib = dict(sorted(element.attrib.items()))
    for child in list(element):
        _sort_attribs(child)


def _strip_whitespace(element: ET.Element) -> None:
    if element.text is not None and element.text.strip() == "":
        element.text = None
    if element.tail is not None and element.tail.strip() == "":
        element.tail = None
    for child in list(element):
        _strip_whitespace(child)


def _normalize(element: ET.Element) -> str:
    _sort_attribs(element)
    _strip_whitespace(element)
    return ET.tostring(element, encoding="unicode")


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


def _collect_operations() -> List[Tuple[str, ET.Element, List, dict]]:
    operations = []

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
            attrs = dict(child.attrib) if child.attrib else {}
            operations.append((child.tag, child, payload, attrs))
            break

    for path in sorted(DOCS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for item in data.get("item", []):
            extract(item)

    return operations


@pytest.mark.parametrize("operation, template_elem, payload, attrs", _collect_operations())
def test_build_operation_matches_docs(operation: str, template_elem: ET.Element, payload, attrs) -> None:
    built = xml_builder.build_operation(operation, payload, attrs=attrs or None)
    assert _normalize(built) == _normalize(template_elem)
