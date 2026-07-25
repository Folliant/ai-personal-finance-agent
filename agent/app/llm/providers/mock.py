from typing import Any
import json

from app.llm.base import LLMAdapter
from app.models.llm import (
    LLMResponse,
    Message,
    ToolDefinition,
    ToolCall,
)


class MockLLMAdapter(LLMAdapter):
    def __init__(self):
        self.pending_tool: str | None = None

    def complete(
        self,
        messages: list[Message],
        system: str,
        tools: list[ToolDefinition],
    ) -> LLMResponse:

        last_message = messages[-1] if messages else None

        # Second pass after our own tool call
        if (
            last_message
            and last_message.role == "tool"
            and self.pending_tool is not None
        ):
            return LLMResponse(
                text=self._build_answer(
                    last_message.content,
                    self.pending_tool,
                ),
                tool_calls=[],
            )

        query = self._get_user_query(messages)

        if self._contains_any(
            query,
            "grocery",
            "groceries",
            "food",
        ):
            return self._tool_call(
                name="get_spending_by_category",
                arguments={
                    "category": "Groceries",
                    "month": "2025-06",
                },
            )

        if "top" in query and "categor" in query:
            return self._tool_call(
                name="get_top_categories",
                arguments={
                    "month": "2025-06",
                    "limit": 3,
                },
            )

        if "subscription" in query or "subscriptions" in query:
            return self._tool_call(
                name="get_subscriptions",
                arguments={},
            )

        if "compare" in query or ("this month" in query and "last month" in query):
            return self._tool_call(
                name="compare_periods",
                arguments={
                    "month_a": "2025-06",
                    "month_b": "2025-07",
                },
            )

        return LLMResponse(
            text=(
                "Hi! I'm Penny, your personal "
                "finance assistant. "
                "Ask me about your spending."
            ),
            tool_calls=[],
        )

    def _get_user_query(
        self,
        messages: list[Message],
    ) -> str:

        for message in reversed(messages):

            if message.role == "user" and isinstance(message.content, str):
                return message.content.lower()

        return ""

    def _contains_any(
        self,
        text: str,
        *words: str,
    ) -> bool:

        return any(word in text for word in words)

    def _tool_call(
        self,
        name: str,
        arguments: dict[str, Any],
    ) -> LLMResponse:

        self.pending_tool = name

        return LLMResponse(
            text=None,
            tool_calls=[
                ToolCall(
                    id="mock-call-1",
                    name=name,
                    arguments=arguments,
                )
            ],
        )

    def _build_answer(
        self,
        content: Any,
        tool_name: str,
    ) -> str:

        if not isinstance(content, str):
            return str(content)

        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            return str(content)

        if tool_name == "get_spending_by_category":

            return (
                f"You spent ${float(result['total']):.2f} "
                f"on {result['category'].lower()} "
                f"in {result['month']}."
            )

        if tool_name == "get_top_categories":

            categories = []

            for name, amount in result.items():
                categories.append(f"{name} (${float(amount):.2f})")

            return "Your top categories this month are " f"{', '.join(categories)}."

        if tool_name == "get_subscriptions":

            subscriptions = []

            for item in result:

                subscriptions.append(
                    f"{item['merchant']} " f"(${float(item['amount']):.2f})"
                )

            return "Your subscriptions are " f"{', '.join(subscriptions)}."

        if tool_name == "compare_periods":

            difference = float(result["difference"])

            if difference < 0:
                return (
                    "Your spending decreased by "
                    f"${abs(difference):.2f} "
                    "compared with the previous period."
                )

            return (
                "Your spending increased by "
                f"${difference:.2f} "
                "compared with the previous period."
            )

        return str(result)
