from __future__ import annotations
from dataclasses import dataclass

class ProtocolError(ValueError):
    pass

@dataclass(frozen=True)
class Request:
    op: str
    key: str
    value: str | None

def _validate_key(key: str) -> None:
    if not key or " " in key:
        raise ProtocolError("invalid key")
    if len(key) > 999:
        raise ProtocolError("key too long")

def _validate_value(value: str) -> None:
    if len(value) > 999:
        raise ProtocolError("value too long")