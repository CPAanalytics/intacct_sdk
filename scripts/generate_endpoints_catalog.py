from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

DOCS_DIR = Path('Docs')
OUTPUT = Path('docs/endpoints.md')

BASE_METHODS = {
    'getAPISession': 'IntacctClient.get_api_session',
    'readByQuery': 'SessionClient.read_by_query',
    'read': 'SessionClient.read',
    'create': 'SessionClient.create',
    'update': 'SessionClient.update',
    'delete': 'SessionClient.delete',
}


def to_snake(name: str) -> str:
    name = re.sub(r'[^a-zA-Z0-9]+', '_', name)
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def extract_from_item(item, module_name, rows):
    if 'item' in item:
        for child in item['item']:
            extract_from_item(child, module_name, rows)
        return

    request = item.get('request') or {}
    body = (request.get('body') or {}).get('raw')
    if not body:
        return

    body = body.strip()
    if not body.startswith('<?xml') and '<request' not in body:
        return

    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return

    func = root.find('.//function')
    if func is None:
        return

    op_elem = None
    for child in list(func):
        op_elem = child
        break
    if op_elem is None:
        return

    operation = op_elem.tag
    object_name = None

    obj_node = op_elem.find('object')
    if obj_node is not None and obj_node.text:
        object_name = obj_node.text.strip()
    else:
        for child in list(op_elem):
            if child.tag.isupper():
                object_name = child.tag
                break

    object_name = object_name or module_name

    if operation in BASE_METHODS:
        sdk_method = BASE_METHODS[operation]
        status = 'done'
    else:
        sdk_method = f'OperationClient.{to_snake(operation)}'
        status = 'wip'

    rows.append((operation, object_name, sdk_method, status, 'unit, fixture'))


rows = []
for path in sorted(DOCS_DIR.glob('*.json')):
    module_name = path.stem.replace('_', ' ')
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('item', []):
        extract_from_item(item, module_name, rows)

seen = set()
unique_rows = []
for row in rows:
    key = (row[0], row[1])
    if key in seen:
        continue
    seen.add(key)
    unique_rows.append(row)

unique_rows.sort(key=lambda r: (r[0], r[1]))

lines = [
    '# Endpoint Catalog',
    '',
    'Status: todo | wip | done',
    'Tests: unit | integration | fixture | live',
    '',
    '| Operation | Object/Module | SDK Method | Status | Tests |',
    '| --- | --- | --- | --- | --- |',
]

for operation, obj, method, status, tests in unique_rows:
    lines.append(f'| {operation} | {obj} | {method} | {status} | {tests} |')

lines.append('')
lines.append('## Notes')
lines.append('- Generated from Postman collections in `Docs/`. Review for accuracy before implementation.')

OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
