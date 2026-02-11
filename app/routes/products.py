from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.database import db
from app.models.product import Product
from datetime import datetime

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("", response_model=List[Product])
async def get_products(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    search: Optional[str] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    preference: Optional[List[str]] = Query(None),
    ingredient: Optional[List[str]] = Query(None),
    benefit: Optional[List[str]] = Query(None),
    skin_type: Optional[List[str]] = Query(None),
    formulation: Optional[List[str]] = Query(None),
    spf: Optional[int] = None,
    minPrice: Optional[float] = None,
    maxPrice: Optional[float] = None,
):
    query = {}

    if category:
        query["category"] = category

    if brand:
        query["brand"] = brand

    if min_rating is not None or max_rating is not None:
        query["rating"] = {}
        if min_rating is not None:
            query["rating"]["$gte"] = min_rating
        if max_rating is not None:
            query["rating"]["$lt"] = max_rating

    if minPrice is not None or maxPrice is not None:
        query["price"] = {}
        if minPrice is not None:
            query["price"]["$gte"] = minPrice
        if maxPrice is not None:
            query["price"]["$lte"] = maxPrice

    # ✅ SIMPLE: Just search in name and description for all checkbox filters
    if preference and len(preference) > 0:
        query["$and"] = query.get("$and", [])
        for pref in preference:
            query["$and"].append({
                "$or": [
                    {"name": {"$regex": pref, "$options": "i"}},
                    {"description": {"$regex": pref, "$options": "i"}}
                ]
            })

    if ingredient and len(ingredient) > 0:
        query["$and"] = query.get("$and", [])
        for ing in ingredient:
            query["$and"].append({
                "$or": [
                    {"name": {"$regex": ing, "$options": "i"}},
                    {"description": {"$regex": ing, "$options": "i"}}
                ]
            })

    if benefit and len(benefit) > 0:
        query["$and"] = query.get("$and", [])
        for ben in benefit:
            query["$and"].append({
                "$or": [
                    {"name": {"$regex": ben, "$options": "i"}},
                    {"description": {"$regex": ben, "$options": "i"}}
                ]
            })

    if skin_type and len(skin_type) > 0:
        query["$and"] = query.get("$and", [])
        for st in skin_type:
            query["$and"].append({
                "$or": [
                    {"name": {"$regex": st, "$options": "i"}},
                    {"description": {"$regex": st, "$options": "i"}}
                ]
            })

    if formulation and len(formulation) > 0:
        query["$and"] = query.get("$and", [])
        for form in formulation:
            query["$and"].append({
                "$or": [
                    {"name": {"$regex": form, "$options": "i"}},
                    {"description": {"$regex": form, "$options": "i"}}
                ]
            })

    if spf is not None:
        query["$and"] = query.get("$and", [])
        query["$and"].append({
            "$or": [
                {"name": {"$regex": f"SPF {spf}", "$options": "i"}},
                {"description": {"$regex": f"SPF {spf}", "$options": "i"}}
            ]
        })

    if search:
        search_query = {
            "$or": [
                {"name": {"$regex": search, "$options": "i"}},
                {"description": {"$regex": search, "$options": "i"}},
                {"brand": {"$regex": search, "$options": "i"}},
                {"category": {"$regex": search, "$options": "i"}},
                {"tags": {"$regex": search, "$options": "i"}},
            ]
        }
        
        if "$and" in query:
            query["$and"].append(search_query)
        else:
            query.update(search_query)

    print("MongoDB Query:", query)
    products = await db.products.find(query).to_list(1000)

    for p in products:
        if isinstance(p.get("created_at"), str):
            p["created_at"] = datetime.fromisoformat(p["created_at"])

    return products


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = await db.products.find_one({"id": product_id})
    if not product:
        raise HTTPException(404, "Product not found")

    if isinstance(product.get("created_at"), str):
        product["created_at"] = datetime.fromisoformat(product["created_at"])

    return product