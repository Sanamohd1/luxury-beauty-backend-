from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import db
from app.models.user import User, UserCreate, UserLogin
from app.auth.jwt import create_token, decode_token
from datetime import datetime, timezone
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBearer()


def hash_password(p: str) -> str:
    return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()


def verify_password(p: str, h: str) -> bool:
    return bcrypt.checkpw(p.encode(), h.encode())


@router.post("/register")
async def register(data: UserCreate):
    if await db.users.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(email=data.email, name=data.name)

    doc = user.model_dump()
    doc["password"] = hash_password(data.password)
    doc["created_at"] = datetime.now(timezone.utc)

    await db.users.insert_one(doc)

    return {
        "token": create_token(user.id),
        "user": user
    }


@router.post("/login")
async def login(data: UserLogin):
    user = await db.users.find_one({"email": data.email}, {"_id": 0})

    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "token": create_token(user["id"]),
        "user": User(**user)
    }


@router.get("/me")
async def get_me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("user_id")

    user = await db.users.find_one(
        {"id": user_id},
        {"_id": 0, "password": 0}
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
