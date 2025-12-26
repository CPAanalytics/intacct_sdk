from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

DOCS_DIR = Path('Docs')
OUTPUT = Path('src/intacct_sdk/operations_generated.py')


BASE_OBJECT_OPS = {'create', 'update', 'delete', 'read', 'readByQuery', 'readByName'}


def to_snake(name: str) -> str:
    name = re.sub(r'[^a-zA-Z0-9]+', '_', name)
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def iter_items(data: dict):
    for item in data.get('item', []):
        yield from _walk_item(item)


def _walk_item(item: dict):
    if 'item' in item:
        for child in item['item']:
            yield from _walk_item(child)
        return
    yield item


def parse_xml(body: str) -> ET.Element | None:
    if not body:
        return None
    body = body.strip()
    if not body.startswith('<?xml') and '<request' not in body:
        return None
    try:
        return ET.fromstring(body)
    except ET.ParseError:
        return None


def first_operation(root: ET.Element) -> ET.Element | None:
    func = root.find('.//function')
    if func is None:
        return None
    for child in list(func):
        return child
    return None


def extract_object_elem(operation: ET.Element) -> ET.Element | None:
    for child in list(operation):
        if child.tag.isupper():
            return child
    return None


def collect_field_paths(node: ET.Element, prefix: str = '') -> set[str]:
    fields: set[str] = set()
    for child in list(node):
        path = f'{prefix}.{child.tag}' if prefix else child.tag
        if list(child):
            fields.update(collect_field_paths(child, path))
        else:
            fields.add(path)
    return fields


def parse_fields_text(node: ET.Element | None) -> set[str]:
    if node is None or node.text is None:
        return set()
    text = node.text.strip()
    if not text:
        return set()
    if text == '*':
        return {'*'}
    return {part.strip() for part in text.split(',') if part.strip()}


ops: set[str] = set()
op_attrs: dict[str, set[str]] = {}
op_payload_fields: dict[str, set[str]] = {}
op_object_fields: dict[str, dict[str, set[str]]] = {}

for path in DOCS_DIR.glob('*.json'):
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in iter_items(data):
        body = (item.get('request') or {}).get('body', {}).get('raw')
        root = parse_xml(body or '')
        if root is None:
            continue
        op_elem = first_operation(root)
        if op_elem is None:
            continue

        op_tag = op_elem.tag
        ops.add(op_tag)

        if op_elem.attrib:
            op_attrs.setdefault(op_tag, set()).update(op_elem.attrib.keys())

        if op_tag in {'create', 'update', 'delete'}:
            obj_elem = extract_object_elem(op_elem)
            if obj_elem is None:
                continue
            object_name = obj_elem.tag.upper()
            fields = collect_field_paths(obj_elem)
            op_object_fields.setdefault(op_tag, {}).setdefault(object_name, set()).update(fields)
            continue

        if op_tag in {'read', 'readByQuery', 'readByName'}:
            obj = op_elem.find('object')
            object_name = obj.text.strip().upper() if obj is not None and obj.text else None
            if not object_name:
                continue
            fields = parse_fields_text(op_elem.find('fields'))
            op_object_fields.setdefault(op_tag, {}).setdefault(object_name, set()).update(fields)
            continue

        payload_fields = collect_field_paths(op_elem)
        op_payload_fields.setdefault(op_tag, set()).update(payload_fields)


def format_field_block(fields: set[str]) -> list[str]:
    if not fields:
        return ['- (no fields listed)']
    if fields == {'*'}:
        return ['- *']
    return [f'- {field}' for field in sorted(fields)]


def format_object_field_block(object_fields: dict[str, set[str]]) -> list[str]:
    if not object_fields:
        return ['- (no fields listed)']
    lines: list[str] = []
    for object_name in sorted(object_fields):
        fields = object_fields[object_name]
        lines.append(f'- {object_name}:')
        if fields == {'*'}:
            lines.append('  - *')
            continue
        if not fields:
            lines.append('  - (no fields listed)')
            continue
        for field in sorted(fields):
            lines.append(f'  - {field}')
    return lines


method_lines = []
for op in sorted(ops):
    method_name = to_snake(op)
    method_lines.append((method_name, op))

seen: dict[str, str] = {}
for method_name, op in method_lines:
    if method_name not in seen:
        seen[method_name] = op

lines = [
    'from __future__ import annotations',
    '',
    'from typing import Optional, Dict',
    '',
    'from . import xml as xml_builder',
    'from .models import ResultData',
    '',
    '',
    'class OperationMixin:',
    '    def execute(',
    '        self,',
    '        operation: str,',
    '        payload: Optional[xml_builder.Payload] = None,',
    '        operation_attrs: Optional[Dict[str, str]] = None,',
    '        control_id: Optional[str] = None,',
    '    ) -> ResultData:',
    '        raise NotImplementedError',
    '',
]

for method_name, op in sorted(seen.items()):
    lines.append(
        f'    def {method_name}(self, payload: Optional[xml_builder.Payload] = None, operation_attrs: Optional[Dict[str, str]] = None, control_id: Optional[str] = None) -> ResultData:'
    )
    doc_lines = [f'Execute "{op}".', '', 'Fields (from Docs samples):']

    object_fields = op_object_fields.get(op, {})
    if object_fields:
        doc_lines.extend(format_object_field_block(object_fields))
    else:
        doc_lines.extend(format_field_block(op_payload_fields.get(op, set())))

    attrs = op_attrs.get(op, set())
    if attrs:
        doc_lines.append('')
        doc_lines.append('Operation attributes:')
        doc_lines.extend([f'- {attr}' for attr in sorted(attrs)])

    lines.append('        """' + '\n        '.join(doc_lines) + '"""')
    lines.append(
        f'        return self.execute("{op}", payload=payload, operation_attrs=operation_attrs, control_id=control_id)'
    )
    lines.append('')

OUTPUT.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
