from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from typing import List

class CartItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    product_id: str
    quantity: int
    name: str
    price: float
    image: str

class Cart(BaseModel):
    model_config = ConfigDict(extra="ignore")

    user_id: str
    items: List[CartItem] = []
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


