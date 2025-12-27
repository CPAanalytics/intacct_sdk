from __future__ import annotations

from dataclasses import fields as dataclass_fields
from typing import Any, ClassVar, Dict, Iterable, Optional, Type, TypeVar

from .models import Record, ResultData


TModel = TypeVar("TModel", bound="BaseModel")


def _serialize_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


class BaseModel:
    _object_name: ClassVar[str]
    _field_map: ClassVar[Dict[str, str]]
    _field_id_to_attr: ClassVar[Dict[str, str]]
    _readonly_fields: ClassVar[set[str]]
    _required_fields: ClassVar[set[str]]

    def to_fields(self, include_readonly: bool = False) -> Dict[str, str]:
        payload: Dict[str, str] = {}
        for field in dataclass_fields(self):
            value = getattr(self, field.name)
            if value is None:
                continue
            if not include_readonly and field.name in self._readonly_fields:
                continue
            payload[self._field_map.get(field.name, field.name)] = _serialize_value(value)
        return payload

    @classmethod
    def from_fields(cls: Type[TModel], fields: Dict[str, str]) -> TModel:
        kwargs: Dict[str, Any] = {}
        for key, value in fields.items():
            attr = cls._field_id_to_attr.get(key, None)
            if attr:
                kwargs[attr] = value
        return cls(**kwargs)  # type: ignore[arg-type]

    @classmethod
    def from_record(cls: Type[TModel], record: Record) -> TModel:
        return cls.from_fields(record.fields)

    @classmethod
    def from_result(cls: Type[TModel], result: ResultData) -> TModel:
        return cls.from_fields(result.fields)

    @classmethod
    def missing_required(cls, instance: "BaseModel") -> Iterable[str]:
        missing = []
        for name in cls._required_fields:
            if getattr(instance, name, None) is None:
                missing.append(name)
        return missing
