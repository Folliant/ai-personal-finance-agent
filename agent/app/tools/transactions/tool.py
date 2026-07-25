from app.data.repository import load_transactions


def get_spending_by_category(
    category: str,
    month: str,
):
    df = load_transactions()

    filtered = df[
        (df["category"].str.lower() == category.lower())
        & (df["date"].str.startswith(month))
    ]

    return {
        "category": category,
        "month": month,
        "total": round(filtered["amount"].sum(), 2),
    }


def get_top_categories(
    month: str,
    limit: int = 3,
):
    df = load_transactions()

    filtered = df[df["date"].str.startswith(month)]

    totals = (
        filtered.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
    )

    return totals.to_dict()


def get_subscriptions():
    df = load_transactions()

    return df[df["category"] == "Subscription"].to_dict("records")


def compare_periods(
    month_a: str,
    month_b: str,
):
    df = load_transactions()

    total_a = df[df["date"].str.startswith(month_a)]["amount"].sum()

    total_b = df[df["date"].str.startswith(month_b)]["amount"].sum()

    return {
        "month_a": round(total_a, 2),
        "month_b": round(total_b, 2),
        "difference": round(total_b - total_a, 2),
    }
