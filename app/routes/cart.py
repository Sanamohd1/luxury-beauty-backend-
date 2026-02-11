from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.auth.deps import get_current_user
from app.models.cart import Cart
from datetime import datetime, timezone

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("/")
async def get_cart(user=Depends(get_current_user)):
    cart = await db.carts.find_one({"user_id": user.id}, {"_id": 0})

    if not cart:
        cart = Cart(user_id=user.id).model_dump()
        cart["updated_at"] = cart["updated_at"].isoformat()
        await db.carts.insert_one(cart)

    return cart


@router.post("/")
async def add_to_cart(data: dict, user=Depends(get_current_user)):
    product = await db.products.find_one({"id": data["product_id"]}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = await db.carts.find_one({"user_id": user.id})
    if not cart:
        cart = {"user_id": user.id, "items": []}

    for item in cart["items"]:
        if item["product_id"] == data["product_id"]:
            item["quantity"] += data.get("quantity", 1)
            break
    else:
        cart["items"].append({
            "product_id": product["id"],
            "quantity": data.get("quantity", 1),
            "name": product["name"],
            "price": product["price"],
            "image": product["image"]
        })

    cart["updated_at"] = datetime.now(timezone.utc).isoformat()

    await db.carts.update_one(
        {"user_id": user.id},
        {"$set": cart},
        upsert=True
    )

    return {"message": "Added to cart"}


@router.put("/{product_id}")
async def update_cart_quantity(
    product_id: str,
    data: dict,
    user=Depends(get_current_user)
):
    cart = await db.carts.find_one({"user_id": user.id})
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    for item in cart["items"]:
        if item["product_id"] == product_id:
            item["quantity"] = max(1, data.get("quantity", item["quantity"]))
            break
    else:
        raise HTTPException(status_code=404, detail="Item not in cart")

    cart["updated_at"] = datetime.now(timezone.utc).isoformat()

    await db.carts.update_one(
        {"user_id": user.id},
        {"$set": cart}
    )

    return {"message": "Quantity updated"}


@router.delete("/{product_id}")
async def remove_from_cart(product_id: str, user=Depends(get_current_user)):
    cart = await db.carts.find_one({"user_id": user.id})
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    cart["items"] = [
        item for item in cart["items"]
        if item["product_id"] != product_id
    ]

    cart["updated_at"] = datetime.now(timezone.utc).isoformat()

    await db.carts.update_one(
        {"user_id": user.id},
        {"$set": cart}
    )

    return {"message": "Item removed"}
