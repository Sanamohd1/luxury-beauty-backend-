from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import CORS_ORIGINS
from app.database import close_db

from app.routes.auth import router as auth_router
from app.routes.products import router as products_router
from app.routes.cart import router as cart_router
from app.routes.orders import router as orders_router
from app.routes.reviews import router as reviews_router


# ✅ Create app
app = FastAPI(title="Luxury Beauty Ecommerce API")


# ✅ Include routers
app.include_router(auth_router)
app.include_router(auth_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(reviews_router, prefix="/api")


# ✅ CORS Middleware (single clean config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Root route
@app.get("/")
async def root():
    return {"message": "Luxury Beauty Ecommerce API"}


# ✅ Shutdown event
@app.on_event("shutdown")
async def shutdown():
    await close_db()
