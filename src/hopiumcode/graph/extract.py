"""Извлечение символов и связей из кода (без LLM). Владелец: участник 3."""
from __future__ import annotations
from pathlib import Path
from ..models import Node, Edge


def extract(root: Path) -> tuple[list[Node], list[Edge]]:
    """Узлы File/Class/Function/Doc и рёбра DEFINES/IMPORTS/INHERITS/CALLS/DOCUMENTS."""
    raise NotImplementedError("участник 3")
