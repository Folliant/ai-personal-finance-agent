from functools import lru_cache

import pandas as pd


@lru_cache
def load_transactions() -> pd.DataFrame:
    return pd.read_csv("app/data/transactions.csv")
