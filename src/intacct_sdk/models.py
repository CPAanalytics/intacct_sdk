from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Session:
    session_id: str
    endpoint: str


@dataclass(frozen=True)
class Record:
    fields: Dict[str, str]
    raw: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class QueryResult:
    records: List[Record]
    result_id: Optional[str]
    num_remaining: Optional[int]
    total_count: Optional[int]


@dataclass(frozen=True)
class ResultData:
    fields: Dict[str, str]
    raw_xml: Optional[str] = None
