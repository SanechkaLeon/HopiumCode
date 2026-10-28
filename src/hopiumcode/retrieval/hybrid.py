"""Гибридный ретривер: вектор + BM25 + обход графа. Владелец: участник 3."""
from __future__ import annotations
from ..models import Hit


def retrieve(question: str, k: int = 8, mode: str = "hybrid") -> list[Hit]:
    """mode: "vector" | "vector+bm25" | "hybrid" (с графом). Режимы нужны для сравнения в eval."""
    raise NotImplementedError("участник 3")
