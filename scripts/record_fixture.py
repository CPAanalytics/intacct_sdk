from __future__ import annotations

import argparse
from pathlib import Path

from intacct_sdk.config import IntacctConfig
from intacct_sdk.sanitize import sanitize_xml
from intacct_sdk.transport import HttpTransport


def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def main() -> int:
    parser = argparse.ArgumentParser(description="Record a sanitized fixture from a request XML file.")
    parser.add_argument("--request", required=True, help="Path to the request XML file")
    parser.add_argument("--output", required=True, help="Fixture name (without suffix)")
    args = parser.parse_args()

    request_path = Path(args.request)
    fixture_base = Path("fixtures") / args.output
    request_out = fixture_base.with_name(f"{fixture_base.name}_request.xml")
    response_out = fixture_base.with_name(f"{fixture_base.name}_response.xml")

    config = IntacctConfig.from_env()
    transport = HttpTransport(
        timeout_seconds=config.timeout_seconds,
        max_retries=config.max_retries,
        backoff_seconds=config.backoff_seconds,
        logger=config.logger,
    )

    request_xml = _read_bytes(request_path)
    response_xml = transport.post(config.endpoint_url, request_xml)

    sanitized_request = sanitize_xml(request_xml)
    sanitized_response = sanitize_xml(response_xml)

    request_out.write_bytes(sanitized_request)
    response_out.write_bytes(sanitized_response)

    print(f"Wrote fixtures to {request_out} and {response_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
