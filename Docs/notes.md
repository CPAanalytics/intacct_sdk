# Notes

- Responses may contain optional fields; parsing preserves unknown fields in `Record.raw`.
- If the API returns undocumented fields or unexpected structures, add a fixture and document here.
- The endpoint catalog previously included `Inventory Control` as an object for `SessionClient.create` and `SessionClient.update`. This is a module label, not a valid XML object tag, so those two rows were removed from `Docs/endpoints.md`.
