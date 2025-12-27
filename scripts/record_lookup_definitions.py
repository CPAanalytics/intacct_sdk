from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, Iterable, List
from xml.etree import ElementTree as ET

from intacct_sdk import IntacctClient, IntacctConfig, IntacctError
from intacct_sdk.sanitize import sanitize_xml


ROOT = Path(__file__).resolve().parents[1]
OBJECT_SERVICES = ROOT / "src" / "intacct_sdk" / "object_services_generated.py"
OUTPUT_DIR = ROOT / "fixtures" / "lookup"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def ensure_endpoint_env() -> None:
    if "INTACCT_ENDPOINT_URL" not in os.environ and "INTACCT_ENDPOINT_URl" in os.environ:
        os.environ["INTACCT_ENDPOINT_URL"] = os.environ["INTACCT_ENDPOINT_URl"]


def extract_object_names() -> List[str]:
    text = OBJECT_SERVICES.read_text(encoding="utf-8")
    pattern = r'super\(\).__init__\(session_client, "([A-Z0-9_]+)"\)'
    names = re.findall(pattern, text)
    return sorted(set(names))


def parse_lookup_xml(raw_xml: str) -> Dict[str, object]:
    root = ET.fromstring(raw_xml)
    type_node = root.find("Type")
    if type_node is None:
        return {"fields": [], "relationships": []}

    fields = []
    for field_node in type_node.findall("./Fields/Field"):
        field: Dict[str, object] = {}
        for child in list(field_node):
            if child.tag == "VALIDVALUES":
                field["valid_values"] = [val.text or "" for val in child.findall("VALIDVALUE")]
                continue
            field[child.tag.lower()] = (child.text or "").strip()
        fields.append(field)

    relationships = []
    for rel_node in type_node.findall("./Relationships/Relationship"):
        rel: Dict[str, object] = {}
        for child in list(rel_node):
            rel[child.tag.lower()] = (child.text or "").strip()
        relationships.append(rel)

    return {
        "object_name": type_node.attrib.get("Name"),
        "fields": fields,
        "relationships": relationships,
    }


def write_lookup(object_name: str, xml_body: str, parsed: Dict[str, object]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    xml_path = OUTPUT_DIR / f"{object_name}.xml"
    json_path = OUTPUT_DIR / f"{object_name}.json"

    sanitized = sanitize_xml(xml_body.encode("utf-8"))
    xml_path.write_bytes(sanitized)
    json_path.write_text(json.dumps(parsed, indent=2, sort_keys=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Refresh existing definitions")
    args = parser.parse_args()

    load_env(ROOT / ".env")
    ensure_endpoint_env()

    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    api = client.session_client(client.get_api_session())

    object_names = extract_object_names()
    failures: List[str] = []

    for index, object_name in enumerate(object_names, start=1):
        xml_path = OUTPUT_DIR / f"{object_name}.xml"
        if xml_path.exists() and not args.refresh:
            continue
        try:
            result = api.operations.lookup(payload=[("object", object_name, None)])
            if not result.raw_xml:
                failures.append(object_name)
                continue
            parsed = parse_lookup_xml(result.raw_xml)
            write_lookup(object_name, result.raw_xml, parsed)
        except IntacctError:
            failures.append(object_name)
        if index % 20 == 0:
            print(f"Processed {index}/{len(object_names)} objects...")

    if failures:
        print("Lookup failures:", ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
