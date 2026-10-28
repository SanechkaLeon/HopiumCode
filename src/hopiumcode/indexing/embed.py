"""Эмбеддинги через Ollama с кэшем. Владелец: участник 2."""
from __future__ import annotations


class OllamaEmbedder:
    def __init__(self, model: str = "nomic-embed-text") -> None:
        self.model = model

    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError("участник 2")
