# hopiumcode: локальный ИИ-агент, помощник по кодовой базе

> Рабочее название пакета `hopiumcode`. Команда CopiumCore. Переименование проекта: `scripts/rename_project.sh НОВОЕ_ИМЯ`.

Агент отвечает на вопросы разработчика по небольшому открытому репозиторию (до 100 файлов) и в каждом утверждении
даёт ссылку `[путь:начало-конец]`. Всё работает локально: Ollama, Chroma, граф кода, MCP-сервер, без внешних API.

Архитектура и задания участников: см. `docs/architecture.md` и `OWNERS.md`. Полное ТЗ лежит в `docs/` (PDF).

## Быстрый старт

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env
ollama pull qwen3:8b && ollama pull nomic-embed-text    # модели можно менять в .env
git clone <URL репозитория-цели> data/repo               # выбирается на этапе Э0
make index          # индексация (участники 2 и 3)
make ask Q="Где обрабатывается ошибка подключения?"
make test
make eval           # сравнение режимов поиска (участник 5)
```

## Структура

| Папка | Что внутри | Владелец |
|---|---|---|
| `src/hopiumcode/` | Код агента | см. `OWNERS.md` |
| `src/hopiumcode/indexing/` | Загрузка, разбиение, эмбеддинги, векторная БД | Участник 2 |
| `src/hopiumcode/retrieval/` | BM25, слияние, гибридный ретривер | 2 и 3 |
| `src/hopiumcode/graph/` | Граф кода: извлечение, хранилище, запросы | Участник 3 |
| `src/hopiumcode/mcp_server/` | MCP-сервер с инструментами | Участник 4 |
| `eval/`, `tests/`, `docs/` | Оценка, тесты, документация | Участник 5 |
| `data/` | Репозиторий-цель и индексы (не коммитятся) | все |

Статус модулей: пока везде заглушки (`NotImplementedError`) с указанием владельца. Контракты зафиксированы в `src/hopiumcode/models.py` и `interfaces.py`.
