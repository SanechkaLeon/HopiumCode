"""Обход репозитория. Владелец: участник 2."""
from __future__ import annotations
from pathlib import Path
from typing import Iterator

EXTENSIONS = {".py", ".md", ".rst", ".txt"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", "build", "dist"}
MAX_BYTES = 200_000


def iter_files(root: Path) -> Iterator[Path]:
    """Файлы репозитория для индексации (без служебных каталогов, бинарных и больших файлов)."""
    raise NotImplementedError("участник 2")
