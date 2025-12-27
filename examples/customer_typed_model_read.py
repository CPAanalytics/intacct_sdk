from intacct_sdk import IntacctClient, IntacctConfig


def main() -> int:
    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    api = client.session_client(client.get_api_session())

    customers = api.objects.customer.read_by_query_models(
        fields=["*"],
        query="STATUS = 'T'",
        page_size=100,
    )
    print(f"Fetched {len(customers)} active customers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
