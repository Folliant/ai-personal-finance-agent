from app.agent.agent import Agent
from app.config import get_conf
from app.guards.guard import Guard
from app.llm.providers.mock import MockLLMAdapter
from app.llm.providers.openai import OpenAIAdapter
from app.memory.in_memory import InMemory
from app.orchestrator import Orchestrator

from app.tools.setup import create_tool_registry


def create_llm():
    config = get_conf()

    if config.llm_provider == "openai":
        return OpenAIAdapter()

    return MockLLMAdapter()


def create_orchestrator() -> Orchestrator:
    tools = create_tool_registry()
    llm = create_llm()

    agent = Agent(
        llm=llm,
        tools=tools,
        memory=InMemory(),
    )

    return Orchestrator(
        agent=agent,
        guard=Guard(),
    )
