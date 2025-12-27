# Usage

## Install

This repo is a local SDK. Use it directly or install it in editable mode.

## Configure

Set environment variables:

- `INTACCT_ENDPOINT_URL`
- `INTACCT_SENDER_ID`
- `INTACCT_SENDER_PASSWORD`
- `INTACCT_COMPANY_ID`
- `INTACCT_USER_ID`
- `INTACCT_USER_PASSWORD`
- `INTACCT_CLIENT_ID` (optional)
- `INTACCT_ENTITY_ID` (optional)

## Example

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
session = client.get_api_session()
api = client.session_client(session)

customers = api.objects.customer.read_by_query(
    fields=["RECORDNO", "CUSTOMERID", "NAME"],
    page_size=100,
)

for record in customers.records:
    print(record.fields)
```

## Generic operations

Use the generated operation methods for named API functions beyond CRUD/query.

```python
result = api.operations.update_apaccountlabel(
    payload=[("glaccountno", "6090", None)],
    operation_attrs={"accountlabel": "Travel Expenses"},
)
print(result.fields)
```

## Typed models

Typed models are generated from live lookup definitions and provide convenience
methods for create/update and response parsing.

```python
from intacct_sdk import typed_models

dept = typed_models.DepartmentModel(
    departmentid="ENG",
    title="Engineering",
)
api.objects.department.create(dept)

dept_model = api.objects.department.read_model(keys=["ENG"], fields=["DEPARTMENTID", "TITLE"])
print(dept_model)
```

## Accounts Receivable (AR)

```python
ar = api.ar
result = ar.update_araccountlabel(
    payload=[("glaccountno", "6090", None)],
    operation_attrs={"accountlabel": "Travel Expenses"},
)
print(result.fields)
```

## Recording fixtures

Fixtures can be recorded from a request XML file (sanitized on disk):

```bash
python scripts/record_fixture.py --request path/to/request.xml --output my_fixture
```
