"""Векторная БД (Chroma). Владелец: участник 2."""
from __future__ import annotations
from ..models import Chunk, Hit


class VectorIndex:
    def add(self, chunks: list[Chunk]) -> None:
        raise NotImplementedError("участник 2")

    def search(self, query: str, k: int) -> list[Hit]:
        raise NotImplementedError("участник 2")

    def delete_by_path(self, path: str) -> None:
        raise NotImplementedError("участник 2")
