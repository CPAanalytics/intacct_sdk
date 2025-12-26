from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class IntacctError(Exception):
    message: str
    error_number: Optional[str] = None
    description: Optional[str] = None
    correction: Optional[str] = None
    control_id: Optional[str] = None
    operation_id: Optional[str] = None
    http_status: Optional[int] = None

    def __str__(self) -> str:
        detail = self.message
        if self.error_number:
            detail += f" (error {self.error_number})"
        if self.description:
            detail += f": {self.description}"
        if self.correction:
            detail += f" | correction: {self.correction}"
        return detail


@dataclass
class TransportError(Exception):
    message: str
    http_status: Optional[int] = None

    def __str__(self) -> str:
        if self.http_status is not None:
            return f"{self.message} (HTTP {self.http_status})"
        return self.message
