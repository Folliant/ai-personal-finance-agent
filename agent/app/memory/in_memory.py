from collections import defaultdict

from app.models.llm import Message
from app.memory.base import Memory


class InMemory(Memory):
    def __init__(self):
        self.storage = defaultdict(list)

    def get_messages(
        self,
        session_id: str,
    ) -> list[Message]:
        return self.storage[session_id]

    def add_message(
        self,
        session_id: str,
        message: Message,
    ) -> None:
        self.storage[session_id].append(message)
