from xml.etree import ElementTree as ET

from intacct_sdk import xml as xml_builder


def _strip_whitespace(element: ET.Element) -> None:
    if element.text is not None and element.text.strip() == "":
        element.text = None
    if element.tail is not None and element.tail.strip() == "":
        element.tail = None
    for child in list(element):
        _strip_whitespace(child)


def _normalize(xml_bytes: bytes | ET.Element) -> str:
    if isinstance(xml_bytes, ET.Element):
        root = xml_bytes
    else:
        root = ET.fromstring(xml_bytes)
    _strip_whitespace(root)
    return ET.tostring(root, encoding="unicode")


def test_build_get_api_session_request() -> None:
    control = xml_builder.build_control("sender", "password", "ctrl-1")
    auth = xml_builder.build_login_auth("user", "company", "userpass")
    function = xml_builder.build_function("ctrl-1", xml_builder.build_get_api_session())
    request = xml_builder.build_request(control, auth, function)

    expected = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-1</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <login>
            <userid>user</userid>
            <companyid>company</companyid>
            <password>userpass</password>
          </login>
        </authentication>
        <content>
          <function controlid="ctrl-1">
            <getAPISession />
          </function>
        </content>
      </operation>
    </request>
    """

    assert _normalize(request) == _normalize(expected.encode("utf-8"))


def test_build_read_by_query_request() -> None:
    control = xml_builder.build_control("sender", "password", "ctrl-2")
    auth = xml_builder.build_session_auth("session")
    operation = xml_builder.build_read_by_query("CUSTOMER", ["RECORDNO", "CUSTOMERID"], "", 50, 10)
    function = xml_builder.build_function("ctrl-2", operation)
    request = xml_builder.build_request(control, auth, function)

    expected = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-2</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <sessionid>session</sessionid>
        </authentication>
        <content>
          <function controlid="ctrl-2">
            <readByQuery>
              <object>CUSTOMER</object>
              <fields>RECORDNO,CUSTOMERID</fields>
              <query />
              <pagesize>50</pagesize>
              <offset>10</offset>
            </readByQuery>
          </function>
        </content>
      </operation>
    </request>
    """

    assert _normalize(request) == _normalize(expected.encode("utf-8"))


def test_build_create_update_delete_request() -> None:
    control = xml_builder.build_control("sender", "password", "ctrl-3")
    auth = xml_builder.build_session_auth("session")
    create_op = xml_builder.build_create("CUSTOMER", {"CUSTOMERID": "C-1", "NAME": "Name"})
    create_request = xml_builder.build_request(
        control,
        auth,
        xml_builder.build_function("ctrl-3", create_op),
    )

    expected_create = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-3</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <sessionid>session</sessionid>
        </authentication>
        <content>
          <function controlid="ctrl-3">
            <create>
              <CUSTOMER>
                <CUSTOMERID>C-1</CUSTOMERID>
                <NAME>Name</NAME>
              </CUSTOMER>
            </create>
          </function>
        </content>
      </operation>
    </request>
    """
    assert _normalize(create_request) == _normalize(expected_create.encode("utf-8"))

    update_op = xml_builder.build_update("CUSTOMER", {"RECORDNO": "10", "NAME": "New"})
    update_request = xml_builder.build_request(
        control,
        auth,
        xml_builder.build_function("ctrl-3", update_op),
    )
    expected_update = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-3</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <sessionid>session</sessionid>
        </authentication>
        <content>
          <function controlid="ctrl-3">
            <update>
              <CUSTOMER>
                <RECORDNO>10</RECORDNO>
                <NAME>New</NAME>
              </CUSTOMER>
            </update>
          </function>
        </content>
      </operation>
    </request>
    """
    assert _normalize(update_request) == _normalize(expected_update.encode("utf-8"))

    delete_op = xml_builder.build_delete("CUSTOMER", "RECORDNO", "10")
    delete_request = xml_builder.build_request(
        control,
        auth,
        xml_builder.build_function("ctrl-3", delete_op),
    )
    expected_delete = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-3</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <sessionid>session</sessionid>
        </authentication>
        <content>
          <function controlid="ctrl-3">
            <delete>
              <CUSTOMER>
                <RECORDNO>10</RECORDNO>
              </CUSTOMER>
            </delete>
          </function>
        </content>
      </operation>
    </request>
    """
    assert _normalize(delete_request) == _normalize(expected_delete.encode("utf-8"))


def test_build_read_request() -> None:
    control = xml_builder.build_control("sender", "password", "ctrl-4")
    auth = xml_builder.build_session_auth("session")
    read_op = xml_builder.build_read("CUSTOMER", ["1001"], ["RECORDNO", "NAME"])
    request = xml_builder.build_request(control, auth, xml_builder.build_function("ctrl-4", read_op))

    expected = """
    <request>
      <control>
        <senderid>sender</senderid>
        <password>password</password>
        <controlid>ctrl-4</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
        <includewhitespace>false</includewhitespace>
      </control>
      <operation>
        <authentication>
          <sessionid>session</sessionid>
        </authentication>
        <content>
          <function controlid="ctrl-4">
            <read>
              <object>CUSTOMER</object>
              <keys>
                <key>1001</key>
              </keys>
              <fields>RECORDNO,NAME</fields>
            </read>
          </function>
        </content>
      </operation>
    </request>
    """

    assert _normalize(request) == _normalize(expected.encode("utf-8"))


def test_build_operation_with_attributes() -> None:
    payload = [("glaccountno", "6090", None)]
    operation = xml_builder.build_operation(
        "update_apaccountlabel",
        payload,
        attrs={"accountlabel": "Travel Expenses"},
    )
    expected = """
    <update_apaccountlabel accountlabel="Travel Expenses">
      <glaccountno>6090</glaccountno>
    </update_apaccountlabel>
    """
    assert _normalize(operation) == _normalize(expected.encode("utf-8"))
