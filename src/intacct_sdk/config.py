from __future__ import annotations

from dataclasses import dataclass, field
import logging
import os


@dataclass(frozen=True)
class IntacctConfig:
    endpoint_url: str
    sender_id: str
    sender_password: str
    company_id: str
    user_id: str
    user_password: str
    client_id: str = ""
    entity_id: str = ""
    timeout_seconds: float = 30.0
    max_retries: int = 2
    backoff_seconds: float = 0.5
    logger: logging.Logger = field(default_factory=lambda: logging.getLogger("intacct_sdk"))

    @staticmethod
    def from_env() -> "IntacctConfig":
        return IntacctConfig(
            endpoint_url=_require_env("INTACCT_ENDPOINT_URL"),
            sender_id=_require_env("INTACCT_SENDER_ID"),
            sender_password=_require_env("INTACCT_SENDER_PASSWORD"),
            company_id=_require_env("INTACCT_COMPANY_ID"),
            user_id=_require_env("INTACCT_USER_ID"),
            user_password=_require_env("INTACCT_USER_PASSWORD"),
            client_id=os.getenv("INTACCT_CLIENT_ID", ""),
            entity_id=os.getenv("INTACCT_ENTITY_ID", ""),
        )

    def company_with_slide_in(self) -> str:
        slide_in = ""
        if self.client_id:
            slide_in += f"|{self.client_id}"
        if self.entity_id:
            slide_in += f"|{self.entity_id}"
        return f"{self.company_id}{slide_in}"


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
