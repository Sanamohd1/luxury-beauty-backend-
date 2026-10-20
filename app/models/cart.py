from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, timezone
from typing import List

class CartAdd(BaseModel):
    product_id: str = Field(min_length=1)
    quantity: int = Field(default=1, gt=0, strict=True)

class CartUpdate(BaseModel):
    quantity: int = Field(gt=0, strict=True)

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


