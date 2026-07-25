import json

from app.agent.prompt import SYSTEM_PROMPT
from app.config import get_conf
from app.llm.base import LLMAdapter
from app.models.llm import Message
from app.memory.base import Memory
from app.tools.registry import ToolRegistry


class Agent:

    def __init__(
        self,
        llm: LLMAdapter,
        tools: ToolRegistry,
        memory: Memory,
    ):
        self.llm = llm
        self.tools = tools
        self.memory = memory

    def run(
        self,
        session_id: str,
        query: str,
    ) -> str:

        self.memory.add_message(
            session_id,
            Message(
                role="user",
                content=query,
            ),
        )

        for _ in range(get_conf().max_tool_iterations):

            messages = self.memory.get_messages(session_id)

            response = self.llm.complete(
                messages=messages,
                system=SYSTEM_PROMPT,
                tools=self.tools.definitions(),
            )

            if not response.tool_calls:

                answer = response.text or ""

                self.memory.add_message(
                    session_id,
                    Message(
                        role="assistant",
                        content=answer,
                    ),
                )

                return answer

            for call in response.tool_calls:

                result = self.tools.execute(
                    call.name,
                    call.arguments,
                )

                self.memory.add_message(
                    session_id,
                    Message(
                        role="tool",
                        content=json.dumps(
                            result,
                            default=str,
                        ),
                    ),
                )

        return "Maximum tool iterations reached."
