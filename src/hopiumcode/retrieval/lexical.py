"""BM25 по фрагментам и слияние выдач. Владелец: участник 2."""
from __future__ import annotations
from ..models import Hit


class Lexical:
    def search(self, query: str, k: int) -> list[Hit]:
        raise NotImplementedError("участник 2")


def fuse(lists: list[list[Hit]], k: int = 60, top: int = 20) -> list[Hit]:
    """Reciprocal Rank Fusion; в via объединить источники через «+»."""
    raise NotImplementedError("участник 2")
