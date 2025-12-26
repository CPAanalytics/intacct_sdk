from __future__ import annotations

import time
from typing import Dict, Optional
import urllib.error
import urllib.request

from .errors import TransportError


class HttpTransport:
    def __init__(
        self,
        timeout_seconds: float,
        max_retries: int,
        backoff_seconds: float,
        logger,
    ) -> None:
        self._timeout = timeout_seconds
        self._max_retries = max_retries
        self._backoff = backoff_seconds
        self._logger = logger

    def post(self, url: str, body: bytes, headers: Optional[Dict[str, str]] = None) -> bytes:
        headers = headers or {"Content-Type": "application/xml"}
        attempt = 0

        while True:
            attempt += 1
            try:
                request = urllib.request.Request(
                    url,
                    data=body,
                    headers=headers,
                    method="POST",
                )
                with urllib.request.urlopen(request, timeout=self._timeout) as response:
                    return response.read()
            except urllib.error.HTTPError as exc:
                body_bytes = exc.read() if exc.fp is not None else None
                if body_bytes:
                    return body_bytes
                raise TransportError("HTTP error without body", http_status=exc.code) from exc
            except urllib.error.URLError as exc:
                if attempt > self._max_retries:
                    raise TransportError("Network error", http_status=None) from exc
                self._logger.warning("Retrying request after network error: %s", exc)
                time.sleep(self._backoff * attempt)
