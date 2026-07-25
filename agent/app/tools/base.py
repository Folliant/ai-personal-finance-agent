from abc import ABC, abstractmethod

from app.models.llm import ToolDefinition


class ToolProvider(ABC):
    @abstractmethod
    def definitions(self) -> list[ToolDefinition]:
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        name: str,
        arguments: dict,
    ) -> object:
        raise NotImplementedError
