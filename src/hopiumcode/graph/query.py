"""Запросы к графу и обход. Владелец: участник 3."""
from __future__ import annotations


def callers(symbol: str, depth: int = 1) -> list[str]:
    raise NotImplementedError("участник 3")


def callees(symbol: str, depth: int = 1) -> list[str]:
    raise NotImplementedError("участник 3")


def expand(seed_ids: list[str], seed_scores: dict[str, float], hops: int = 2) -> list[tuple[str, float, str]]:
    """Вес соседа = вес родителя * w(тип ребра) / (1 + 0.15 * (степень - 1)). Вернуть (id, вес, причина)."""
    raise NotImplementedError("участник 3")
