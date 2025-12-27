from __future__ import annotations

import time
from typing import Dict, Optional
import urllib.error
import urllib.request

from .errors import TransportError
from .sanitize import sanitize_xml


class HttpTransport:
    def __init__(
        self,
        timeout_seconds: float,
        max_retries: int,
        backoff_seconds: float,
        debug_xml: bool,
        logger,
    ) -> None:
        self._timeout = timeout_seconds
        self._max_retries = max_retries
        self._backoff = backoff_seconds
        self._debug_xml = debug_xml
        self._logger = logger

    def post(self, url: str, body: bytes, headers: Optional[Dict[str, str]] = None) -> bytes:
        headers = headers or {"Content-Type": "application/xml"}
        attempt = 0
        if self._debug_xml:
            sanitized_request = sanitize_xml(body).decode("utf-8", errors="replace")
            self._logger.debug("Intacct request XML:\n%s", sanitized_request)

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
                    response_body = response.read()
                    if self._debug_xml:
                        sanitized_response = sanitize_xml(response_body).decode("utf-8", errors="replace")
                        self._logger.debug("Intacct response XML:\n%s", sanitized_response)
                    return response_body
            except urllib.error.HTTPError as exc:
                body_bytes = exc.read() if exc.fp is not None else None
                if body_bytes:
                    if self._debug_xml:
                        sanitized_response = sanitize_xml(body_bytes).decode("utf-8", errors="replace")
                        self._logger.debug("Intacct error response XML:\n%s", sanitized_response)
                    return body_bytes
                raise TransportError("HTTP error without body", http_status=exc.code) from exc
            except urllib.error.URLError as exc:
                if attempt > self._max_retries:
                    raise TransportError("Network error", http_status=None) from exc
                self._logger.warning("Retrying request after network error: %s", exc)
                time.sleep(self._backoff * attempt)
