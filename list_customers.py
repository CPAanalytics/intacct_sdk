#!/usr/bin/env python
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from typing import Optional, Tuple, List, Dict


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def post_xml(url: str, xml_body: str) -> str:
    data = xml_body.encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/xml"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")


def get_text(node: ET.Element, path: str) -> Optional[str]:
    found = node.find(path)
    return found.text.strip() if found is not None and found.text else None


def parse_session(response_xml: str) -> Tuple[str, str]:
    root = ET.fromstring(response_xml)
    control_status = get_text(root, "control/status")
    if control_status != "success":
        raise RuntimeError(f"Control status not success: {control_status}")

    auth_status = get_text(root, "operation/authentication/status")
    if auth_status != "success":
        raise RuntimeError(f"Authentication status not success: {auth_status}")

    result_status = get_text(root, "operation/result/status")
    if result_status != "success":
        raise RuntimeError(f"Result status not success: {result_status}")

    session_id = get_text(root, "operation/result/data/api/sessionid")
    endpoint = get_text(root, "operation/result/data/api/endpoint")
    if not session_id or not endpoint:
        raise RuntimeError("Missing sessionid/endpoint in response")
    return session_id, endpoint


def parse_customers(response_xml: str) -> List[Dict[str, str]]:
    root = ET.fromstring(response_xml)
    control_status = get_text(root, "control/status")
    if control_status != "success":
        raise RuntimeError(f"Control status not success: {control_status}")

    result_status = get_text(root, "operation/result/status")
    if result_status != "success":
        err = get_text(root, "operation/result/errormessage/error/description")
        raise RuntimeError(f"Result status not success: {result_status}. {err or ''}")

    data = root.find("operation/result/data")
    if data is None:
        return []

    candidates: List[ET.Element] = []
    candidates.extend(data.findall(".//CUSTOMER"))
    candidates.extend(data.findall(".//customer"))

    if not candidates:
        for elem in data.iter():
            has_customerid = elem.find("CUSTOMERID") is not None or elem.find("customerid") is not None
            has_name = elem.find("NAME") is not None or elem.find("name") is not None
            if has_customerid or has_name:
                candidates.append(elem)

    seen = set()
    customers = []
    for elem in candidates:
        customer_id = get_text(elem, "CUSTOMERID") or get_text(elem, "customerid") or ""
        name = get_text(elem, "NAME") or get_text(elem, "name") or ""
        recordno = get_text(elem, "RECORDNO") or get_text(elem, "recordno") or ""
        key = (customer_id, name, recordno)
        if key in seen:
            continue
        seen.add(key)
        if not (customer_id or name or recordno):
            continue
        customers.append({"customer_id": customer_id, "name": name, "recordno": recordno})
    return customers


def main() -> int:
    endpoint_url = "https://api.intacct.com/ia/xml/xmlgw.phtml"
    sender_id = "REI1309"
    sender_password = r"1br.\Q<6KkuPkWz0]Lm*"
    company_id = "REI1309-sandbox"
    user_id = "JChevalier"
    user_password = "y5e$iLRB7ugS@WK#"

    client_id = os.getenv("INTACCT_CLIENT_ID", "")
    entity_id = os.getenv("INTACCT_ENTITY_ID", "")
    slide_in = ""
    if client_id:
        slide_in += f"|{client_id}"
    if entity_id:
        slide_in += f"|{entity_id}"

    auth_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<request>
  <control>
    <senderid>{xml_escape(sender_id)}</senderid>
    <password>{xml_escape(sender_password)}</password>
    <controlid>auth</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
    <includewhitespace>false</includewhitespace>
  </control>
  <operation>
    <authentication>
      <login>
        <userid>{xml_escape(user_id)}</userid>
        <companyid>{xml_escape(company_id + slide_in)}</companyid>
        <password>{xml_escape(user_password)}</password>
      </login>
    </authentication>
    <content>
      <function controlid=\"get-session\">
        <getAPISession />
      </function>
    </content>
  </operation>
</request>
"""

    auth_response = post_xml(endpoint_url, auth_xml)
    session_id, session_endpoint = parse_session(auth_response)

    list_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<request>
  <control>
    <senderid>{xml_escape(sender_id)}</senderid>
    <password>{xml_escape(sender_password)}</password>
    <controlid>list-customers</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
    <includewhitespace>false</includewhitespace>
  </control>
  <operation>
    <authentication>
      <sessionid>{xml_escape(session_id)}</sessionid>
    </authentication>
    <content>
      <function controlid=\"list-customers\">
        <readByQuery>
          <object>CUSTOMER</object>
          <fields>RECORDNO,CUSTOMERID,NAME</fields>
          <query/>
          <pagesize>100</pagesize>
        </readByQuery>
      </function>
    </content>
  </operation>
</request>
"""

    list_response = post_xml(session_endpoint, list_xml)
    customers = parse_customers(list_response)

    if not customers:
        print("No customers returned.")
        return 0

    for customer in customers:
        recordno = customer.get("recordno", "")
        customer_id = customer.get("customer_id", "")
        name = customer.get("name", "")
        print(f"{recordno}\t{customer_id}\t{name}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
