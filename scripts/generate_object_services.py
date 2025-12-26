from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

DOCS_DIR = Path('Docs')
OUTPUT = Path('src/intacct_sdk/object_services_generated.py')


def to_pascal(name: str) -> str:
    parts = re.split(r'[^a-zA-Z0-9]+', name)
    return ''.join(part[:1].upper() + part[1:].lower() for part in parts if part)


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


object_fields: dict[str, dict[str, set[str]]] = {}

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

        if op_tag in {'create', 'update', 'delete'}:
            obj_elem = extract_object_elem(op_elem)
            if obj_elem is None:
                continue
            object_name = obj_elem.tag.upper()
            fields = collect_field_paths(obj_elem)
            object_fields.setdefault(object_name, {}).setdefault(op_tag, set()).update(fields)
            continue

        if op_tag in {'read', 'readByQuery'}:
            obj = op_elem.find('object')
            object_name = obj.text.strip().upper() if obj is not None and obj.text else None
            if not object_name:
                continue
            fields = parse_fields_text(op_elem.find('fields'))
            object_fields.setdefault(object_name, {}).setdefault(op_tag, set()).update(fields)


def format_fields(fields: set[str]) -> list[str]:
    if not fields:
        return ['- (no fields listed)']
    if fields == {'*'}:
        return ['- *']
    return [f'- {field}' for field in sorted(fields)]


def build_docstring(action: str, object_name: str, fields: set[str]) -> str:
    lines = [
        f'{action} {object_name}.',
        '',
        'Valid fields (from Docs samples):',
        *format_fields(fields),
    ]
    return '\n'.join(lines)


def build_read_docstring(object_name: str, fields: set[str]) -> str:
    lines = [
        f'Read {object_name} records.',
        '',
        'Fields (from Docs samples):',
        *format_fields(fields),
    ]
    return '\n'.join(lines)


def build_read_by_query_docstring(object_name: str, fields: set[str]) -> str:
    lines = [
        f'Read {object_name} records via readByQuery.',
        '',
        'Fields (from Docs samples):',
        *format_fields(fields),
    ]
    return '\n'.join(lines)


def build_delete_docstring(object_name: str, fields: set[str]) -> str:
    lines = [
        f'Delete {object_name}.',
        '',
        'Key fields (from Docs samples):',
        *format_fields(fields),
    ]
    return '\n'.join(lines)


lines = [
    'from __future__ import annotations',
    '',
    'from typing import Dict, Iterable, Optional',
    '',
    'from .models import QueryResult, ResultData',
    'from .object_services_base import ObjectService',
    '',
    '',
    'class ObjectServices:',
    '    def __init__(self, session_client) -> None:',
    '        self._session_client = session_client',
    '',
    '    def __getattr__(self, name: str) -> ObjectService:',
    '        return ObjectService(self._session_client, name)',
    '',
]

sorted_objects = sorted(object_fields.keys())

for object_name in sorted_objects:
    class_name = f'{to_pascal(object_name)}Service'
    create_fields = object_fields.get(object_name, {}).get('create', set())
    update_fields = object_fields.get(object_name, {}).get('update', set())
    delete_fields = object_fields.get(object_name, {}).get('delete', set())
    read_fields = object_fields.get(object_name, {}).get('read', set())
    read_by_query_fields = object_fields.get(object_name, {}).get('readByQuery', set())

    lines.append('')
    lines.append(f'class {class_name}(ObjectService):')
    lines.append(f'    """Service for {object_name}."""')
    lines.append('    def __init__(self, session_client) -> None:')
    lines.append(f'        super().__init__(session_client, "{object_name}")')
    lines.append('')
    lines.append('    def read_by_query(')
    lines.append('        self,')
    lines.append('        fields: Iterable[str],')
    lines.append('        query: str = "",')
    lines.append('        page_size: int = 100,')
    lines.append('        offset: Optional[int] = None,')
    lines.append('        control_id: Optional[str] = None,')
    lines.append('    ) -> QueryResult:')
    doc = build_read_by_query_docstring(object_name, read_by_query_fields)
    lines.append(f'        """{doc}"""')
    lines.append('        return super().read_by_query(')
    lines.append('            fields,')
    lines.append('            query=query,')
    lines.append('            page_size=page_size,')
    lines.append('            offset=offset,')
    lines.append('            control_id=control_id,')
    lines.append('        )')
    lines.append('')
    lines.append('    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:')
    doc = build_read_docstring(object_name, read_fields)
    lines.append(f'        """{doc}"""')
    lines.append('        return super().read(keys, fields, control_id=control_id)')
    lines.append('')
    lines.append('    def create(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:')
    doc = build_docstring('Create', object_name, create_fields)
    lines.append(f'        """{doc}"""')
    lines.append('        return super().create(fields, control_id=control_id)')
    lines.append('')
    lines.append('    def update(self, fields: Dict[str, str], control_id: Optional[str] = None) -> ResultData:')
    doc = build_docstring('Update', object_name, update_fields)
    lines.append(f'        """{doc}"""')
    lines.append('        return super().update(fields, control_id=control_id)')
    lines.append('')
    lines.append('    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:')
    doc = build_delete_docstring(object_name, delete_fields)
    lines.append(f'        """{doc}"""')
    lines.append('        return super().delete(key_field, key_value, control_id=control_id)')
    lines.append('')

lines.append('')
lines.append('def _build_factory():')
lines.append('    class Factory(ObjectServices):')
lines.append('        pass')
lines.append('')

for object_name in sorted_objects:
    class_name = f'{to_pascal(object_name)}Service'
    prop_name = object_name.lower()
    lines.append('        @property')
    lines.append(f'        def {prop_name}(self) -> {class_name}:')
    lines.append(f'            """Service accessor for {object_name}."""')
    lines.append(f'            return {class_name}(self._session_client)')
    lines.append('')

lines.append('    return Factory')
lines.append('')
lines.append('ObjectServices = _build_factory()')

OUTPUT.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
