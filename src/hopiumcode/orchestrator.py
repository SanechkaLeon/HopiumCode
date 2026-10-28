"""Цикл ответа: вопрос -> ретривер -> промпт -> LLM -> инструменты -> проверка ссылок. Владелец: участник 1."""
from __future__ import annotations
from .models import Answer


def classify(question: str) -> str:
    """Тип вопроса: semantic | graph | history | other."""
    raise NotImplementedError("участник 1")


def answer(question: str, mode: str = "hybrid") -> Answer:
    """Главная функция агента. Используется консолью и скриптом оценки."""
    raise NotImplementedError("участник 1")


def verify_citations(answer_text: str, allowed_refs: list[tuple[str, int, int]]):
    """Проверка ссылок [путь:начало-конец] по списку допустимых (путь, начало, конец)."""
    raise NotImplementedError("участник 1")
