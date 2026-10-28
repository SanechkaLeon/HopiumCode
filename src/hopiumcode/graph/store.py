"""Хранилище графа за общим интерфейсом. Владелец: участник 3."""
from __future__ import annotations
from ..models import Node, Edge


class NetworkXStore:
    """Запасная реализация (в памяти + сохранение в файл)."""
    def add_nodes(self, nodes: list[Node]) -> None:
        raise NotImplementedError("участник 3")

    def add_edges(self, edges: list[Edge]) -> None:
        raise NotImplementedError("участник 3")

    def save(self) -> None:
        raise NotImplementedError("участник 3")

    def load(self) -> None:
        raise NotImplementedError("участник 3")


class KuzuStore(NetworkXStore):
    """Встраиваемая графовая БД Kuzu: если не установится, не реализуем."""
