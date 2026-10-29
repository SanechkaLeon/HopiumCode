"""Сравнение режимов retrieve: vector | vector+bm25 | hybrid. Владелец: участник 5."""
from __future__ import annotations

from pathlib import Path

import yaml

QUESTIONS_PATH = Path(__file__).with_name("questions.yaml")
QUESTION_TYPES = {"semantic", "graph", "history", "overview", "trap", "explain"}

# старое поле -> новое
_LEGACY_FIELDS = {"category": "type", "gold_files": "expected_files", "gold_answer": "reference_answer"}


def normalize_question(raw: dict) -> dict:
    """Приводит вопрос к новому формату; старые поля (category, gold_*) остаются читаемыми."""
    q = dict(raw)
    for old, new in _LEGACY_FIELDS.items():
        if old in q and new not in q:
            q[new] = q[old]
    q.setdefault("type", "semantic")
    for key in ("expected_files", "expected_symbols", "expected_ranges", "expected_commits"):
        q[key] = list(q.get(key) or [])
    q.setdefault("reference_answer", "")
    q.setdefault("notes", "")
    return q


def parse_range(ref: str) -> tuple[str, int, int]:
    """'путь:начало-конец' -> (путь, начало, конец)."""
    path, _, lines = ref.rpartition(":")
    start, _, end = lines.partition("-")
    return path, int(start), int(end or start)


def load_questions(path: Path = QUESTIONS_PATH) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    return [normalize_question(q) for q in data]


def main() -> None:
    raise NotImplementedError("участник 5")


if __name__ == "__main__":
    main()
