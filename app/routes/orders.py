from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.models.order import OrderCreate
from app.auth.dependencies import get_current_user
from datetime import datetime
import uuid

router = APIRouter(prefix="/orders", tags=["Orders"])


# -------------------------
# CREATE ORDER
# -------------------------
@router.post("")
async def create_order(
    data: OrderCreate,
    user = Depends(get_current_user)
):
    cart = await db.carts.find_one({"user_id": user["id"]})
    print("🔥 USER ID:", user["id"])
    print("🔥 CART FOUND:", cart)

    if not cart or not cart.get("items"):
        raise HTTPException(status_code=400, detail="Cart is empty")

    items = []
    for item in cart["items"]:
        item.pop("_id", None)
        items.append(item)

    total = sum(item["price"] * item["quantity"] for item in items)

    order = {
        "id": str(uuid.uuid4()),
        "user_id": user["id"],
        "items": items,
        "shipping_address": data.shipping_address,
        "payment_method": data.payment_method,
        "total": total,
        "created_at": datetime.utcnow()
    }

    await db.orders.insert_one(order)
    await db.carts.delete_one({"user_id": user["id"]})

    return {
        "id": order["id"],
        "user_id": order["user_id"],
        "items": order["items"],
        "shipping_address": order["shipping_address"],
        "payment_method": order["payment_method"],
        "total": order["total"],
        "created_at": order["created_at"].isoformat()
    }


# -------------------------
# GET USER ORDERS  ✅ REQUIRED
# -------------------------
@router.get("")
async def get_orders(user = Depends(get_current_user)):
    orders = await db.orders.find(
        {"user_id": user["id"]},
        {"_id": 0}
    ).to_list(100)

    return orders
