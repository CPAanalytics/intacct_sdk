from intacct_sdk.sanitize import sanitize_xml


def test_sanitize_xml_redacts_sensitive_fields() -> None:
    xml = b"""
    <request>
      <control>
        <senderid>sender</senderid>
        <password>secret</password>
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

    sanitized = sanitize_xml(xml)
    assert b">sender<" not in sanitized
    assert b">secret<" not in sanitized
    assert b">userpass<" not in sanitized
    assert b">company<" not in sanitized
    assert b"***REDACTED***" in sanitized
