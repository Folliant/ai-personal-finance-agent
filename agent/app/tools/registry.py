from collections.abc import Callable
from app.models.llm import ToolDefinition
from app.tools.base import ToolProvider


class ToolRegistry(ToolProvider):
    def __init__(self):
        self._tools: dict[str, Callable] = {}
        self._schemas: list[ToolDefinition] = []

    def register(
        self,
        name: str,
        function: Callable,
        schema: ToolDefinition,
    ) -> None:
        self._tools[name] = function
        self._schemas.append(schema)

    def definitions(self) -> list[ToolDefinition]:
        return self._schemas

    def execute(
        self,
        name: str,
        arguments: dict,
    ) -> object:
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")

        tool = self._tools[name]

        return tool(**arguments)
