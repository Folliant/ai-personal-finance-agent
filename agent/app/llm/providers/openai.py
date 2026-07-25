import json
from typing import Any

from openai import OpenAI
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionToolParam,
    ChatCompletionUserMessageParam,
)

from app.config import get_conf
from app.llm.base import LLMAdapter
from app.models.llm import (
    LLMResponse,
    Message,
    ToolCall,
    ToolDefinition,
)


class OpenAIAdapter(LLMAdapter):
    def __init__(self):
        config = get_conf()

        self.client = OpenAI(
            api_key=config.openai_api_key,
        )

        self.model = config.model

    def complete(
        self,
        messages: list[Message],
        system: str,
        tools: list[ToolDefinition],
    ) -> LLMResponse:
        params: dict[str, Any] = {
            "model": self.model,
            "messages": self._build_messages(
                messages,
                system,
            ),
        }

        converted_tools = self._convert_tools(tools)

        if converted_tools:
            params["tools"] = converted_tools

        response = self.client.chat.completions.create(
            **params,
        )

        choice = response.choices[0]

        return LLMResponse(
            text=choice.message.content or "",
            tool_calls=self._convert_tool_calls(
                choice.message.tool_calls,
            ),
        )

    def _build_messages(
        self,
        messages: list[Message],
        system: str,
    ) -> list[ChatCompletionMessageParam]:

        result: list[ChatCompletionMessageParam] = []

        result.append(
            ChatCompletionSystemMessageParam(
                role="system",
                content=system,
            )
        )

        for message in messages:
            if message.role == "user":
                result.append(
                    ChatCompletionUserMessageParam(
                        role="user",
                        content=message.content,
                    )
                )

            elif message.role == "assistant":
                result.append(
                    ChatCompletionAssistantMessageParam(
                        role="assistant",
                        content=message.content,
                    )
                )

        return result

    def _convert_tools(
        self,
        tools: list[ToolDefinition],
    ) -> list[ChatCompletionToolParam]:

        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.parameters,
                },
            }
            for tool in tools
        ]

    def _convert_tool_calls(
        self,
        tool_calls,
    ) -> list[ToolCall]:

        if not tool_calls:
            return []

        return [
            ToolCall(
                id=call.id,
                name=call.function.name,
                arguments=json.loads(
                    call.function.arguments,
                ),
            )
            for call in tool_calls
        ]
