from pydantic import BaseModel
from typing import List
from datetime import datetime


class OrderItem(BaseModel):
    product_id: str
    name: str
    image: str
    price: float
    quantity: int


class OrderCreate(BaseModel):
    shipping_address: dict
    payment_method: str


class Order(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    shipping_address: dict
    payment_method: str
    total: float
    created_at: datetime
