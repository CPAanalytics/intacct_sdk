from __future__ import annotations

from pathlib import Path
from typing import List


FIXTURE_ROOT = Path(__file__).resolve().parents[1] / "fixtures"


def read_fixture(name: str) -> bytes:
    return (FIXTURE_ROOT / name).read_bytes()


class SequenceTransport:
    def __init__(self, responses: List[bytes]) -> None:
        self._responses = list(responses)
        self.requests = []

    def post(self, url: str, body: bytes, headers=None) -> bytes:
        self.requests.append((url, body, headers))
        if not self._responses:
            raise AssertionError("No more fixture responses available")
        return self._responses.pop(0)
