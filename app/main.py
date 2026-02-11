from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.config import CORS_ORIGINS
from app.database import close_db

from app.routes.auth import router as auth_router
from app.routes.products import router as products_router
from app.routes.cart import router as cart_router
from app.routes.orders import router as orders_router
from app.routes.reviews import router as reviews_router



from dotenv import load_dotenv
load_dotenv()
import os
print("Cloud name:", os.getenv("CLOUDINARY_CLOUD_NAME"))

# ✅ 1. Create app FIRST
app = FastAPI(title="Luxury Beauty Ecommerce API")

 
# ✅ 2. Include routers
app.include_router(auth_router)
app.include_router(auth_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(reviews_router, prefix="/api")


# ✅ 3. Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],                      # IMPORTANT for DELETE
    allow_headers=["*"],
)


# ✅ 4. Root route
@app.get("/")
async def root():
    return {"message": "Luxury Beauty Ecommerce API"}


# ✅ 5. Shutdown event
@app.on_event("shutdown")
async def shutdown():
    await close_db()
