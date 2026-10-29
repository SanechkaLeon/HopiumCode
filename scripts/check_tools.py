"""Проверка локальной модели: отвечает ли и вызывает ли инструменты. Запуск: python scripts/check_tools.py [модель]
Результат запишите в docs/models.md. Владелец: участник 1."""
import sys
import time

import ollama

MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen3:8b"
TOOLS = [{"type": "function", "function": {
    "name": "read_file", "description": "Прочитать файл репозитория",
    "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}}]
CASES = [
    "Покажи содержимое файла README.md",
    "Что находится в файле setup.py?",
    "Привет! Как дела?",  # здесь инструмент НЕ нужен
]

ok = 0
for q in CASES:
    t = time.perf_counter()
    r = ollama.chat(model=MODEL, messages=[{"role": "user", "content": q}], tools=TOOLS, options={"temperature": 0})
    dt = time.perf_counter() - t
    msg = r["message"] if isinstance(r, dict) else r.message
    calls = (msg.get("tool_calls") if isinstance(msg, dict) else msg.tool_calls) or []
    names = [(c["function"]["name"] if isinstance(c, dict) else c.function.name) for c in calls]
    expected_tool = "Привет" not in q
    good = bool(names) == expected_tool
    ok += good
    print(f"{'OK ' if good else 'FAIL'} {dt:5.1f} c | {q!r} -> {names or 'без инструмента'}")
print(f"\nМодель {MODEL}: {ok}/{len(CASES)} верно. Если FAIL на первых двух, вызывайте инструменты правилами оркестратора.")
