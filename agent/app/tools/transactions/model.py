from pydantic import BaseModel
from datetime import date


class Transaction(BaseModel):
    date: date
    merchant: str
    amount: float
    category: str
