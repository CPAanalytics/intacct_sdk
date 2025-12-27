from intacct_sdk import IntacctClient, IntacctConfig


def main() -> int:
    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    session = client.get_api_session()
    api = client.session_client(session)

    definition = api.operations.lookup([("object", "DEPARTMENT", None)])
    results = api.objects.customer.read_by_query(
        fields=["*"],
        page_size=100,
    )

    for record in results.records:
        print(record)


if __name__ == "__main__":
    raise SystemExit(main())
