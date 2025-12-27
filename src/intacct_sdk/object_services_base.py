from __future__ import annotations

from typing import Dict, Iterable, Optional, Union

from .models import QueryResult, ResultData
from .typed_models_base import BaseModel


class ObjectService:
    def __init__(self, session_client, object_name: str) -> None:
        self._session_client = session_client
        self._object_name = object_name.upper()

    def read_by_query(
        self,
        fields: Iterable[str],
        query: str = "",
        page_size: int = 100,
        offset: Optional[int] = None,
        control_id: Optional[str] = None,
    ) -> QueryResult:
        return self._session_client.read_by_query(
            self._object_name,
            fields,
            query=query,
            page_size=page_size,
            offset=offset,
            control_id=control_id,
        )

    def read(self, keys: Iterable[str], fields: Iterable[str], control_id: Optional[str] = None) -> ResultData:
        return self._session_client.read(self._object_name, keys, fields, control_id=control_id)

    def create(self, fields: Union[Dict[str, str], BaseModel], control_id: Optional[str] = None) -> ResultData:
        payload = fields.to_fields() if isinstance(fields, BaseModel) else fields
        return self._session_client.create(self._object_name, payload, control_id=control_id)

    def update(self, fields: Union[Dict[str, str], BaseModel], control_id: Optional[str] = None) -> ResultData:
        payload = fields.to_fields() if isinstance(fields, BaseModel) else fields
        return self._session_client.update(self._object_name, payload, control_id=control_id)

    def delete(self, key_field: str, key_value: str, control_id: Optional[str] = None) -> ResultData:
        return self._session_client.delete(self._object_name, key_field, key_value, control_id=control_id)
