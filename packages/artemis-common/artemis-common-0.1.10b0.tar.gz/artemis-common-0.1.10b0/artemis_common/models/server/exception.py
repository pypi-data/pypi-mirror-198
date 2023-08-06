from __future__ import annotations

from pydantic import BaseModel


class ServerExceptionModel(BaseModel):
    message: str
    error: str
    status_code: int
    url: str
    path: str
    params: dict


__all__ = [
    ServerExceptionModel.__name__,
]
