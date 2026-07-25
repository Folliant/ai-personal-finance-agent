from abc import ABC, abstractmethod
from app.models.llm import LLMResponse, Message, ToolDefinition


class LLMAdapter(ABC):
    @abstractmethod
    def complete(
        self,
        messages: list[Message],
        system: str,
        tools: list[ToolDefinition],
    ) -> LLMResponse:
        raise NotImplementedError
