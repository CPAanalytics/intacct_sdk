#!/usr/bin/env python
import os
import sys
from dataclasses import dataclass
from typing import List
import urllib.request
from lxml import etree


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def post_xml(url: str, xml_body: bytes) -> bytes:
    req = urllib.request.Request(
        url,
        data=xml_body,
        headers={"Content-Type": "application/xml"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return resp.read()


@dataclass(frozen=True)
class IntacctConfig:
    endpoint_url: str
    sender_id: str
    sender_password: str
    company_id: str
    user_id: str
    user_password: str
    client_id: str = ""
    entity_id: str = ""

    @staticmethod
    def from_env() -> "IntacctConfig":
        return IntacctConfig(
            endpoint_url=require_env("INTACCT_ENDPOINT_URL"),
            sender_id=require_env("INTACCT_SENDER_ID"),
            sender_password=require_env("INTACCT_SENDER_PASSWORD"),
            company_id=require_env("INTACCT_COMPANY_ID"),
            user_id=require_env("INTACCT_USER_ID"),
            user_password=require_env("INTACCT_USER_PASSWORD"),
            client_id=os.getenv("INTACCT_CLIENT_ID", ""),
            entity_id=os.getenv("INTACCT_ENTITY_ID", ""),
        )

    def company_with_slide_in(self) -> str:
        slide_in = ""
        if self.client_id:
            slide_in += f"|{self.client_id}"
        if self.entity_id:
            slide_in += f"|{self.entity_id}"
        return f"{self.company_id}{slide_in}"


@dataclass(frozen=True)
class IntacctSession:
    session_id: str
    endpoint: str


@dataclass(frozen=True)
class Customer:
    recordno: str
    customerid: str
    name: str


class IntacctClient:
    def __init__(self, config: IntacctConfig) -> None:
        self._config = config

    def authenticate(self) -> IntacctSession:
        request_xml = self._build_auth_request()
        response_xml = post_xml(self._config.endpoint_url, request_xml)
        return self._parse_session(response_xml)

    def _build_auth_request(self) -> bytes:
        root = etree.Element("request")

        control = etree.SubElement(root, "control")
        etree.SubElement(control, "senderid").text = self._config.sender_id
        etree.SubElement(control, "password").text = self._config.sender_password
        etree.SubElement(control, "controlid").text = "auth"
        etree.SubElement(control, "uniqueid").text = "false"
        etree.SubElement(control, "dtdversion").text = "3.0"
        etree.SubElement(control, "includewhitespace").text = "false"

        operation = etree.SubElement(root, "operation")
        authentication = etree.SubElement(operation, "authentication")
        login = etree.SubElement(authentication, "login")
        etree.SubElement(login, "userid").text = self._config.user_id
        etree.SubElement(login, "companyid").text = self._config.company_with_slide_in()
        etree.SubElement(login, "password").text = self._config.user_password

        content = etree.SubElement(operation, "content")
        function = etree.SubElement(content, "function", controlid="get-session")
        etree.SubElement(function, "getAPISession")

        return etree.tostring(root, xml_declaration=True, encoding="UTF-8")

    @staticmethod
    def _parse_session(response_xml: bytes) -> IntacctSession:
        root = etree.fromstring(response_xml)

        control_status = root.findtext("control/status")
        if control_status != "success":
            raise RuntimeError(f"Control status not success: {control_status}")

        auth_status = root.findtext("operation/authentication/status")
        if auth_status != "success":
            raise RuntimeError(f"Authentication status not success: {auth_status}")

        result_status = root.findtext("operation/result/status")
        if result_status != "success":
            raise RuntimeError(f"Result status not success: {result_status}")

        session_id = root.findtext("operation/result/data/api/sessionid")
        endpoint = root.findtext("operation/result/data/api/endpoint")
        if not session_id or not endpoint:
            raise RuntimeError("Missing sessionid/endpoint in response")

        return IntacctSession(session_id=session_id, endpoint=endpoint)


class CustomerListApi:
    def __init__(self, client: IntacctClient, session: IntacctSession) -> None:
        self._client = client
        self._session = session

    def list_customers(self, pagesize: int = 100) -> List[Customer]:
        request_xml = self._build_list_request(pagesize)
        response_xml = post_xml(self._session.endpoint, request_xml)
        return self._parse_customers(response_xml)

    def _build_list_request(self, pagesize: int) -> bytes:
        root = etree.Element("request")

        control = etree.SubElement(root, "control")
        etree.SubElement(control, "senderid").text = self._client._config.sender_id
        etree.SubElement(control, "password").text = self._client._config.sender_password
        etree.SubElement(control, "controlid").text = "list-customers"
        etree.SubElement(control, "uniqueid").text = "false"
        etree.SubElement(control, "dtdversion").text = "3.0"
        etree.SubElement(control, "includewhitespace").text = "false"

        operation = etree.SubElement(root, "operation")
        authentication = etree.SubElement(operation, "authentication")
        etree.SubElement(authentication, "sessionid").text = self._session.session_id

        content = etree.SubElement(operation, "content")
        function = etree.SubElement(content, "function", controlid="list-customers")
        read_by_query = etree.SubElement(function, "readByQuery")
        etree.SubElement(read_by_query, "object").text = "CUSTOMER"
        etree.SubElement(read_by_query, "fields").text = "RECORDNO,CUSTOMERID,NAME"
        etree.SubElement(read_by_query, "query")
        etree.SubElement(read_by_query, "pagesize").text = str(pagesize)

        return etree.tostring(root, xml_declaration=True, encoding="UTF-8")

    @staticmethod
    def _parse_customers(response_xml: bytes) -> List[Customer]:
        root = etree.fromstring(response_xml)

        control_status = root.findtext("control/status")
        if control_status != "success":
            raise RuntimeError(f"Control status not success: {control_status}")

        result_status = root.findtext("operation/result/status")
        if result_status != "success":
            error_desc = root.findtext("operation/result/errormessage/error/description")
            raise RuntimeError(f"Result status not success: {result_status}. {error_desc or ''}")

        customers = []
        for elem in root.xpath("//operation/result/data//CUSTOMER"):
            recordno = elem.findtext("RECORDNO") or ""
            customerid = elem.findtext("CUSTOMERID") or ""
            name = elem.findtext("NAME") or ""
            if recordno or customerid or name:
                customers.append(Customer(recordno=recordno, customerid=customerid, name=name))

        return customers


def main() -> int:
    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    session = client.authenticate()
    customers = CustomerListApi(client, session).list_customers()

    if not customers:
        print("No customers returned.")
        return 0

    for customer in customers:
        print(customer)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
