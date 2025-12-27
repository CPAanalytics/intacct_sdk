from __future__ import annotations

import json
import keyword
import re
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
LOOKUP_DIR = ROOT / "fixtures" / "lookup"
OUTPUT = ROOT / "src" / "intacct_sdk" / "typed_models_generated.py"


TYPE_MAP = {
    "TEXT": "str",
    "STRING": "str",
    "ID": "str",
    "INTEGER": "int",
    "NUMBER": "float",
    "DECIMAL": "float",
    "CURRENCY": "str",
    "DATE": "str",
    "TIMESTAMP": "str",
    "BOOLEAN": "bool",
}


def to_snake(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9]+", "_", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = name.lower().strip("_")
    if not name:
        name = "field"
    if name[0].isdigit():
        name = f"field_{name}"
    if keyword.iskeyword(name):
        name += "_"
    return name


def to_pascal(name: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", name)
    return "".join(part[:1].upper() + part[1:].lower() for part in parts if part)


def load_definitions() -> Dict[str, dict]:
    definitions: Dict[str, dict] = {}
    for path in sorted(LOOKUP_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        object_name = data.get("object_name") or path.stem
        definitions[object_name] = data
    return definitions


def resolve_type(datatype: str) -> str:
    return TYPE_MAP.get(datatype.upper(), "str")


def main() -> int:
    definitions = load_definitions()
    lines: List[str] = [
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass, field",
        "from typing import ClassVar, Dict, Optional",
        "",
        "from .typed_models_base import BaseModel",
        "",
    ]

    export_names: List[str] = ["BaseModel"]

    for object_name, data in sorted(definitions.items()):
        class_name = f"{to_pascal(object_name)}Model"
        export_names.append(class_name)
        fields = data.get("fields", [])

        field_entries = []
        field_map: Dict[str, str] = {}
        readonly_fields = []
        required_fields = []
        field_id_to_attr: Dict[str, str] = {}

        for field_info in fields:
            field_id = field_info.get("id", "")
            if not field_id:
                continue
            attr_name = to_snake(field_id)
            if attr_name in field_map:
                attr_name = f"{attr_name}_field"
            field_map[attr_name] = field_id
            field_id_to_attr[field_id] = attr_name

            datatype = resolve_type(field_info.get("datatype", ""))
            readonly = (field_info.get("readonly", "").lower() == "true")
            required = (field_info.get("required", "").lower() == "true")
            if readonly:
                readonly_fields.append(attr_name)
            if required:
                required_fields.append(attr_name)

            description = (field_info.get("description") or "").replace('"', "'")
            label = (field_info.get("label") or "").replace('"', "'")
            metadata = {
                "id": field_id,
                "datatype": datatype,
                "label": label,
                "description": description,
                "readonly": readonly,
                "required": required,
            }
            field_entries.append((attr_name, datatype, metadata))

        lines.append("")
        lines.append(f"@dataclass")
        lines.append(f"class {class_name}(BaseModel):")
        lines.append(f"    \"\"\"Typed model for {object_name}.\"\"\"")
        lines.append(f"    _object_name: ClassVar[str] = \"{object_name}\"")
        lines.append(f"    _field_map: ClassVar[Dict[str, str]] = {field_map!r}")
        lines.append(f"    _field_id_to_attr: ClassVar[Dict[str, str]] = {field_id_to_attr!r}")
        lines.append(f"    _readonly_fields: ClassVar[set[str]] = {set(readonly_fields)!r}")
        lines.append(f"    _required_fields: ClassVar[set[str]] = {set(required_fields)!r}")

        if not field_entries:
            lines.append("    placeholder: Optional[str] = None")
            continue

        for attr_name, datatype, metadata in field_entries:
            lines.append(
                f"    {attr_name}: Optional[{datatype}] = field(default=None, metadata={metadata!r})"
            )

    lines.append("")
    lines.append(f"__all__ = {export_names!r}")

    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
