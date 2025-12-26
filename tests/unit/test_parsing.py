import pytest

from intacct_sdk.parsing import parse_read_by_query, parse_result_data, parse_session
from tests.utils import read_fixture


def test_parse_session() -> None:
    response = read_fixture("get_api_session_response.xml")
    session = parse_session(response)
    assert session.session_id == "SESSION123"
    assert session.endpoint.endswith("xmlgw.phtml")


def test_parse_read_by_query() -> None:
    response = read_fixture("read_by_query_response.xml")
    result = parse_read_by_query(response)
    assert result.total_count == 2
    assert len(result.records) == 2
    assert result.records[0].fields["CUSTOMERID"] == "CUST-1"


def test_parse_error_response() -> None:
    xml = b"""
    <response>
      <control>
        <status>success</status>
        <controlid>ctrl-3</controlid>
      </control>
      <operation>
        <result>
          <status>failure</status>
          <controlid>ctrl-3</controlid>
          <errormessage>
            <error>
              <errorno>123</errorno>
              <description>Bad request</description>
              <correction>Fix it</correction>
            </error>
          </errormessage>
        </result>
      </operation>
    </response>
    """

    with pytest.raises(Exception) as excinfo:
        parse_result_data(xml)

    assert "Bad request" in str(excinfo.value)


def test_parse_result_data_success() -> None:
    xml = b"""
    <response>
      <control>
        <status>success</status>
        <controlid>ctrl-4</controlid>
      </control>
      <operation>
        <result>
          <status>success</status>
          <controlid>ctrl-4</controlid>
          <data>
            <key>123</key>
            <recordno>456</recordno>
          </data>
        </result>
      </operation>
    </response>
    """

    result = parse_result_data(xml)
    assert result.fields["key"] == "123"
