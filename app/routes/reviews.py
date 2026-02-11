from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.database import db
from app.auth.deps import get_current_user
from app.models.review import Review, ReviewCreate
from datetime import datetime

router = APIRouter(prefix="/reviews", tags=["Reviews"])

# ✅ ADD THIS - GET reviews for a product
@router.get("", response_model=List[Review])
async def get_reviews(product_id: str):
    reviews = await db.reviews.find({"product_id": product_id}).sort("created_at", -1).to_list(100)
    
    for r in reviews:
        if isinstance(r.get("created_at"), str):
            r["created_at"] = datetime.fromisoformat(r["created_at"])
    
    return reviews

# ✅ EXISTING - POST create a review
@router.post("", response_model=Review)
async def create_review(data: ReviewCreate, user=Depends(get_current_user)):
    product = await db.products.find_one({"id": data.product_id})
    if not product:
        raise HTTPException(404, "Product not found")

    review = Review(
        product_id=data.product_id,
        user_id=user.id,
        user_name=user.name,
        rating=data.rating,
        comment=data.comment
    )

    doc = review.model_dump()
    doc["created_at"] = doc["created_at"].isoformat()
    await db.reviews.insert_one(doc)
    return review