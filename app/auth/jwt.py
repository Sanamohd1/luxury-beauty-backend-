from datetime import datetime, timezone, timedelta
import jwt
from app.config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_HOURS


def create_token(user_id: str) -> str:
    expiration = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS)
    return jwt.encode(
        {"user_id": user_id, "exp": expiration},
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM]
    )
