"""Консоль. Владелец: участник 1.  python -m hopiumcode.cli ask "вопрос" | index"""
from __future__ import annotations
import argparse


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="hopiumcode")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("ask", help="задать вопрос агенту")
    a.add_argument("question")
    a.add_argument("--mode", default="hybrid", choices=["vector", "vector+bm25", "hybrid"])
    sub.add_parser("index", help="проиндексировать репозиторий (векторы и граф)")
    args = p.parse_args(argv)
    if args.cmd == "ask":
        from .orchestrator import answer
        print(answer(args.question, mode=args.mode).text)
    else:
        from .indexing.build import build_all
        build_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
