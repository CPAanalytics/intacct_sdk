# Sage Intacct XML API SDK

Python SDK for the Sage Intacct XML API with session authentication, CRUD/readByQuery helpers,
and generated operation helpers. It is designed to be used locally or installed in editable
mode during development.

## Install

```bash
pip install -e .
```

## Configure

Set environment variables (required unless noted):

- `INTACCT_ENDPOINT_URL`
- `INTACCT_SENDER_ID`
- `INTACCT_SENDER_PASSWORD`
- `INTACCT_COMPANY_ID`
- `INTACCT_USER_ID`
- `INTACCT_USER_PASSWORD`
- `INTACCT_CLIENT_ID` (optional)
- `INTACCT_ENTITY_ID` (optional)

## Quickstart: list customers

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
session = client.get_api_session()
api = client.session_client(session)

results = api.objects.customer.read_by_query(
    fields=["RECORDNO", "CUSTOMERID", "NAME"],
    page_size=100,
)

for record in results.records:
    print(record.fields)
```

## Read by query with paging

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

page_size = 100
offset = 0

while True:
    page = api.objects.customer.read_by_query(
        fields=["RECORDNO", "CUSTOMERID", "NAME"],
        page_size=page_size,
        offset=offset,
    )
    for record in page.records:
        print(record.fields)

    if not page.num_remaining:
        break
    offset += page_size
```

## CRUD via object services

`api.objects.<object>` gives an object-specific helper for common operations.
Object names are uppercased automatically.

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

# Read by keys
vendor = api.objects.vendor.read(keys=["VEND123"], fields=["VENDORID", "NAME"])
print(vendor.fields)

# Create/update/delete (required fields vary by object)
created = api.objects.department.create({"DEPARTMENTID": "ENG", "NAME": "Engineering"})
updated = api.objects.department.update({"DEPARTMENTID": "ENG", "NAME": "Engineering - HQ"})
api.objects.department.delete("DEPARTMENTID", "ENG")
```

## IDE docstrings for endpoints

Per-object CRUD services and generated operations include IDE-friendly docstrings
that list valid fields extracted from the `Docs/` XML samples. This makes
autocomplete and hover help show the fields you can pass.

```python
dept = api.objects.department
help(dept.create)  # Shows the field list for DEPARTMENT create

ops = api.operations
help(ops.update_apaccountlabel)  # Shows payload fields and operation attrs
```

## Typed models from live lookup

When `scripts/record_lookup_definitions.py` runs against Intacct, it records
object definitions and generates typed models. These models make create/update
payloads easier to construct and provide helpers for parsing responses.

```python
from intacct_sdk import IntacctClient, IntacctConfig, typed_models

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

dept = typed_models.DepartmentModel(
    departmentid="ENG",
    title="Engineering",
    status="active",
)
api.objects.department.create(dept)

dept_model = api.objects.department.read_model(keys=["ENG"], fields=["DEPARTMENTID", "TITLE", "STATUS"])
print(dept_model)

models = api.objects.department.read_by_query_models(fields=["DEPARTMENTID", "TITLE"])
print(models[0].departmentid)
```

## Generic operations and payloads

For non-CRUD operations, use `api.operations.<operation>()` or `api.execute()`.
Payloads are tuples of `(tag, value[, attrs])` and can be nested.

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

result = api.operations.update_apaccountlabel(
    payload=[("glaccountno", "6090", None)],
    operation_attrs={"accountlabel": "Travel Expenses"},
)
print(result.fields)

# Equivalent generic call
result = api.execute(
    "update_apaccountlabel",
    payload=[("glaccountno", "6090", None)],
    operation_attrs={"accountlabel": "Travel Expenses"},
)
```

## Lookup operation

Use `lookup` to retrieve an object definition (field list, types) from Intacct.

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

result = api.operations.lookup(
    payload=[("object", "DEPARTMENT", None)],
)
print(result.raw_xml)
```

## Module helpers

Some modules are exposed as dedicated helpers for convenience.

```python
from intacct_sdk import IntacctClient, IntacctConfig

config = IntacctConfig.from_env()
client = IntacctClient(config)
api = client.session_client(client.get_api_session())

ar = api.ar
result = ar.update_araccountlabel(
    payload=[("glaccountno", "6090", None)],
    operation_attrs={"accountlabel": "Travel Expenses"},
)
print(result.fields)
```

## Error handling

```python
from intacct_sdk import IntacctClient, IntacctConfig, IntacctError, TransportError

try:
    config = IntacctConfig.from_env()
    client = IntacctClient(config)
    session = client.get_api_session()
    api = client.session_client(session)
    api.objects.customer.read_by_query(fields=["RECORDNO"], page_size=1)
except IntacctError as exc:
    print(f"Intacct API error: {exc}")
except TransportError as exc:
    print(f"Transport error: {exc}")
```

## More docs and examples

- `Docs/usage.md` has a concise usage reference.
- `examples/list_customers.py` is a runnable script.
