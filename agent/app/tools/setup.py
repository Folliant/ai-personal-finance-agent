from app.tools.registry import ToolRegistry

from app.tools.transactions.definition import (
    COMPARE_PERIODS,
    GET_SPENDING_BY_CATEGORY,
    GET_SUBSCRIPTIONS,
    GET_TOP_CATEGORIES,
)
from app.tools.transactions.tool import (
    compare_periods,
    get_spending_by_category,
    get_subscriptions,
    get_top_categories,
)


def create_tool_registry() -> ToolRegistry:
    registry = ToolRegistry()

    registry.register(
        name="get_spending_by_category",
        function=get_spending_by_category,
        schema=GET_SPENDING_BY_CATEGORY,
    )

    registry.register(
        name="get_top_categories",
        function=get_top_categories,
        schema=GET_TOP_CATEGORIES,
    )

    registry.register(
        name="get_subscriptions",
        function=get_subscriptions,
        schema=GET_SUBSCRIPTIONS,
    )

    registry.register(
        name="compare_periods",
        function=compare_periods,
        schema=COMPARE_PERIODS,
    )

    return registry
