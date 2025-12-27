from __future__ import annotations

import logging
import os
from typing import Dict

from intacct_sdk import IntacctClient, IntacctConfig, IntacctError, TransportError


REQUIRED_ENV = (
    "INTACCT_ENDPOINT_URL",
    "INTACCT_SENDER_ID",
    "INTACCT_SENDER_PASSWORD",
    "INTACCT_COMPANY_ID",
    "INTACCT_USER_ID",
    "INTACCT_USER_PASSWORD",
)


def _require_env() -> Dict[str, str]:
    values: Dict[str, str] = {}
    missing = []
    for name in REQUIRED_ENV:
        value = os.getenv(name)
        if not value:
            missing.append(name)
        else:
            values[name] = value
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
    return values


def main() -> int:
    logging.basicConfig(level=logging.DEBUG)
    env = _require_env()

    config = IntacctConfig(
        endpoint_url=env["INTACCT_ENDPOINT_URL"],
        sender_id=env["INTACCT_SENDER_ID"],
        sender_password=env["INTACCT_SENDER_PASSWORD"],
        company_id=env["INTACCT_COMPANY_ID"],
        user_id=env["INTACCT_USER_ID"],
        user_password=env["INTACCT_USER_PASSWORD"],
        client_id=os.getenv("INTACCT_CLIENT_ID", ""),
        entity_id=os.getenv("INTACCT_ENTITY_ID", ""),
        debug_xml=True,
        logger=logging.getLogger("intacct_sdk"),
    )

    client = IntacctClient(config)
    try:
        session = client.get_api_session()
        print(f"Session OK. Endpoint={session.endpoint} SessionID length={len(session.session_id)}")
        return 0
    except IntacctError as exc:
        print("IntacctError:")
        print(f"  message: {exc}")
        print(f"  error_number: {exc.error_number}")
        print(f"  description: {exc.description}")
        print(f"  correction: {exc.correction}")
        print(f"  control_id: {exc.control_id}")
        print(f"  operation_id: {exc.operation_id}")
        return 1
    except TransportError as exc:
        print("TransportError:")
        print(f"  message: {exc}")
        print(f"  http_status: {exc.http_status}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
