from intacct_sdk import IntacctClient, IntacctConfig
from tests.utils import SequenceTransport, read_fixture


def test_read_by_query_fixture() -> None:
    transport = SequenceTransport(
        [
            read_fixture("get_api_session_response.xml"),
            read_fixture("read_by_query_response.xml"),
        ]
    )

    config = IntacctConfig(
        endpoint_url="https://api.intacct.com/ia/xml/xmlgw.phtml",
        sender_id="sender",
        sender_password="password",
        company_id="company",
        user_id="user",
        user_password="userpass",
    )

    client = IntacctClient(config, transport=transport)
    session = client.get_api_session(control_id="auth")
    api = client.session_client(session)

    results = api.objects.customer.read_by_query(fields=["RECORDNO", "CUSTOMERID", "NAME"])

    assert len(results.records) == 2
    assert results.records[1].fields["NAME"] == "Beta Co"
