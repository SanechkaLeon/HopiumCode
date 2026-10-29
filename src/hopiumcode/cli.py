"""Консоль. Владелец: участник 1.

python -m hopiumcode.cli ask "вопрос" [--mode hybrid] [--fake] [-v]
python -m hopiumcode.cli index
"""
from __future__ import annotations

import argparse
import logging


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="hopiumcode")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("ask", help="задать вопрос агенту")
    a.add_argument("question")
    a.add_argument("--mode", default="hybrid", choices=["vector", "vector+bm25", "hybrid"])
    a.add_argument("--fake", action="store_true", help="заглушки вместо Ollama, ретривера и MCP")
    a.add_argument("-v", "--verbose", action="store_true", help="журнал шагов в stderr")
    sub.add_parser("index", help="проиндексировать репозиторий (векторы и граф)")
    args = p.parse_args(argv)

    if args.cmd == "ask":
        if args.verbose:
            logging.basicConfig(level=logging.INFO, format="%(message)s")
        from .orchestrator import Agent, build_default_agent
        if args.fake:
            from .config import Config
            from .stubs import ScriptedChat, StubTools, stub_retrieve
            agent = Agent(ScriptedChat(), stub_retrieve, StubTools(), Config.from_env())
        else:
            agent = build_default_agent()
        res = agent.answer(args.question, mode=args.mode)
        print(res.text)
        print(f"\n[шагов модели: {res.steps}; инструменты: {', '.join(res.used_tools) or 'нет'}; {res.latency_s:.1f} c]")
    else:
        from .indexing.build import build_all
        build_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
