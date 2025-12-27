from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Optional
import uuid

from .config import IntacctConfig
from .models import QueryResult, ResultData, Session
from .parsing import parse_read_by_query, parse_result_data, parse_session
from .transport import HttpTransport
from . import xml as xml_builder
from .operations_generated import OperationMixin
from .object_services_base import ObjectService
from .object_services_generated import ObjectServices


@dataclass(frozen=True)
class ControlId:
    value: str


class IntacctClient:
    def __init__(self, config: IntacctConfig, transport: Optional[HttpTransport] = None) -> None:
        self._config = config
        self._transport = transport or HttpTransport(
            timeout_seconds=config.timeout_seconds,
            max_retries=config.max_retries,
            backoff_seconds=config.backoff_seconds,
            debug_xml=config.debug_xml,
            logger=config.logger,
        )

    def get_api_session(self, control_id: Optional[str] = None) -> Session:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._config.sender_id,
            self._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_login_auth(
            self._config.user_id,
            self._config.company_with_slide_in(),
            self._config.user_password,
        )
        function = xml_builder.build_function(control_id, xml_builder.build_get_api_session())
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._transport.post(self._config.endpoint_url, request_xml)
        return parse_session(response)

    def session_client(self, session: Session) -> "SessionClient":
        return SessionClient(self, session)


class SessionClient:
    def __init__(self, client: IntacctClient, session: Session) -> None:
        self._client = client
        self._session = session
        self.objects = ObjectServices(self)

    def read_by_query(
        self,
        object_name: str,
        fields: Iterable[str],
        query: str = "",
        page_size: int = 100,
        offset: Optional[int] = None,
        control_id: Optional[str] = None,
    ) -> QueryResult:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation = xml_builder.build_read_by_query(object_name, fields, query, page_size, offset)
        function = xml_builder.build_function(control_id, operation)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_read_by_query(response)

    def read(
        self,
        object_name: str,
        keys: Iterable[str],
        fields: Iterable[str],
        control_id: Optional[str] = None,
    ) -> ResultData:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation = xml_builder.build_read(object_name, keys, fields)
        function = xml_builder.build_function(control_id, operation)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_result_data(response)

    def create(
        self,
        object_name: str,
        fields: Dict[str, str],
        control_id: Optional[str] = None,
    ) -> ResultData:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation = xml_builder.build_create(object_name, fields)
        function = xml_builder.build_function(control_id, operation)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_result_data(response)

    def update(
        self,
        object_name: str,
        fields: Dict[str, str],
        control_id: Optional[str] = None,
    ) -> ResultData:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation = xml_builder.build_update(object_name, fields)
        function = xml_builder.build_function(control_id, operation)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_result_data(response)

    def delete(
        self,
        object_name: str,
        key_field: str,
        key_value: str,
        control_id: Optional[str] = None,
    ) -> ResultData:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation = xml_builder.build_delete(object_name, key_field, key_value)
        function = xml_builder.build_function(control_id, operation)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_result_data(response)

    def execute(
        self,
        operation: str,
        payload: Optional[xml_builder.Payload] = None,
        operation_attrs: Optional[Dict[str, str]] = None,
        control_id: Optional[str] = None,
    ) -> ResultData:
        control_id = control_id or _new_control_id()
        control = xml_builder.build_control(
            self._client._config.sender_id,
            self._client._config.sender_password,
            control_id,
        )
        authentication = xml_builder.build_session_auth(self._session.session_id)
        operation_node = xml_builder.build_operation(operation, payload, attrs=operation_attrs)
        function = xml_builder.build_function(control_id, operation_node)
        request_xml = xml_builder.build_request(control, authentication, function)

        response = self._client._transport.post(self._session.endpoint, request_xml)
        return parse_result_data(response)

    def object(self, object_name: str) -> "ObjectService":
        return ObjectService(self, object_name)

    @property
    def operations(self) -> "OperationClient":
        return OperationClient(self)



class OperationClient(OperationMixin):
    def __init__(self, session_client: SessionClient) -> None:
        self._session_client = session_client

    def execute(
        self,
        operation: str,
        payload: Optional[xml_builder.Payload] = None,
        operation_attrs: Optional[Dict[str, str]] = None,
        control_id: Optional[str] = None,
    ) -> ResultData:
        return self._session_client.execute(
            operation,
            payload=payload,
            operation_attrs=operation_attrs,
            control_id=control_id,
        )

    def __getattr__(self, name: str):
        raise AttributeError(
            f"Operation '{name}' is not defined. Use execute(operation, payload) if needed."
        )


def _new_control_id() -> str:
    return uuid.uuid4().hex
