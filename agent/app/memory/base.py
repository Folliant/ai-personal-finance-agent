from abc import ABC, abstractmethod

from app.models.llm import Message


class Memory(ABC):
    @abstractmethod
    def get_messages(
        self,
        session_id: str,
    ) -> list[Message]:
        raise NotImplementedError

    @abstractmethod
    def add_message(
        self,
        session_id: str,
        message: Message,
    ) -> None:
        raise NotImplementedError
