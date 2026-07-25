from types import SimpleNamespace
from unittest.mock import Mock

from app.agent.agent import Agent
from app.guards.guard import Guard
from app.memory.in_memory import InMemory
from app.orchestrator import Orchestrator
from app.tools.setup import create_tool_registry


def test_orchestrator_flow_without_tools():
    llm = Mock()

    llm.complete.return_value = SimpleNamespace(
        text="You spent $120 on groceries",
        tool_calls=[],
    )

    memory = InMemory()

    agent = Agent(
        llm=llm,
        tools=create_tool_registry(),
        memory=memory,
    )

    orchestrator = Orchestrator(
        agent=agent,
        guard=Guard(),
    )

    result = orchestrator.run(
        session_id="test-session",
        request="How much did I spend on groceries?",
    )

    assert result == "You spent $120 on groceries"

    messages = memory.storage["test-session"]

    assert len(messages) == 2

    assert messages[0].role == "user"
    assert messages[0].content == ("How much did I spend on groceries?")

    assert messages[1].role == "assistant"
    assert messages[1].content == ("You spent $120 on groceries")


def test_orchestrator_flow_with_transaction_tool_call():
    llm = Mock()

    llm.complete.side_effect = [
        SimpleNamespace(
            text=None,
            tool_calls=[
                SimpleNamespace(
                    name="get_spending_by_category",
                    arguments={
                        "category": "Groceries",
                        "month": "2025-06",
                    },
                )
            ],
        ),
        SimpleNamespace(
            text="You spent $92.50 on groceries in June.",
            tool_calls=[],
        ),
    ]

    memory = InMemory()

    agent = Agent(
        llm=llm,
        tools=create_tool_registry(),
        memory=memory,
    )

    orchestrator = Orchestrator(
        agent=agent,
        guard=Guard(),
    )

    result = orchestrator.run(
        session_id="test-session",
        request="How much did I spend on groceries in June?",
    )

    assert result == "You spent $92.50 on groceries in June."

    assert llm.complete.call_count == 2

    messages = memory.storage["test-session"]

    assert len(messages) == 3

    assert messages[0].role == "user"
    assert messages[0].content == ("How much did I spend on groceries in June?")

    assert messages[1].role == "tool"

    assert messages[2].role == "assistant"
    assert messages[2].content == ("You spent $92.50 on groceries in June.")
