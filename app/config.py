from pathlib import Path
from dotenv import load_dotenv
import os


ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

MONGO_URL = os.environ["MONGO_URL"]
DB_NAME = os.environ["DB_NAME"]

JWT_SECRET = os.environ.get("JWT_SECRET", "change-this")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*").split(",")
