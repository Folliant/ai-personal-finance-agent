from app.models.llm import ToolDefinition

GET_SPENDING_BY_CATEGORY = ToolDefinition(
    name="get_spending_by_category",
    description="Returns total spending for a category in a given month.",
    parameters={
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
            },
            "month": {
                "type": "string",
                "description": "YYYY-MM",
            },
        },
        "required": [
            "category",
            "month",
        ],
    },
)


GET_TOP_CATEGORIES = ToolDefinition(
    name="get_top_categories",
    description="Returns the top spending categories for a given month.",
    parameters={
        "type": "object",
        "properties": {
            "month": {
                "type": "string",
            },
            "limit": {
                "type": "integer",
                "default": 3,
            },
        },
        "required": [
            "month",
        ],
    },
)


GET_SUBSCRIPTIONS = ToolDefinition(
    name="get_subscriptions",
    description="Returns recurring subscription payments.",
    parameters={
        "type": "object",
        "properties": {},
    },
)


COMPARE_PERIODS = ToolDefinition(
    name="compare_periods",
    description="Compares spending between two months.",
    parameters={
        "type": "object",
        "properties": {
            "month_a": {
                "type": "string",
            },
            "month_b": {
                "type": "string",
            },
        },
        "required": [
            "month_a",
            "month_b",
        ],
    },
)
