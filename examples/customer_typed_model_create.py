from intacct_sdk import IntacctClient, IntacctConfig
from intacct_sdk.typed_models import CustomerModel,ClassModel


def main() -> int:
    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    api = client.session_client(client.get_api_session())

    customer = CustomerModel(
        customerid="CUST-001",
        company='1002 - REPS',
        cust_cost_center='Saas',
        name="Example Customer",
        status="active",
        classes='202--SAAS-PRO',
        customer_peoaso='PRO',

    )
    result = api.objects.customer.create(customer)
    print(result.fields)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
