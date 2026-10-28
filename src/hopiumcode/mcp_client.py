"""MCP-клиент для цикла оркестратора. Владельцы: участники 4 и 1."""
from __future__ import annotations


class McpClient:
    def start(self) -> None:
        raise NotImplementedError("участник 4")

    def list_tools_for_ollama(self) -> list[dict]:
        raise NotImplementedError("участник 4")

    def call_tool(self, name: str, args: dict) -> str:
        raise NotImplementedError("участник 4")

    def close(self) -> None:
        raise NotImplementedError("участник 4")
