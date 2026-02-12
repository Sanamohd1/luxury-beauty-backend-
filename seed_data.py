import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / ".env")

mongo_url = os.environ.get("MONGO_URL")
db_name = os.environ.get("DB_NAME")

if not mongo_url or not db_name:
    raise RuntimeError("MONGO_URL or DB_NAME not found in .env")

client = AsyncIOMotorClient(mongo_url)
db = client[db_name]


products = [
    # SKINCARE PRODUCTS (10)
    {
        "id": "prod-1",
        "name": "Radiance Serum with Vitamin C",
        "description": "Brighten and even skin tone with this powerful vitamin C serum. Reduces dark spots and enhances natural glow.",
        "price": 89.99,
        "original_price": 120.00,
        "category": "Skincare",
        "brand": "LuxeDerm",
        "image": "https://images.unsplash.com/photo-1723951174326-2a97221d3b7f?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1723951174326-2a97221d3b7f?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=800&auto=format&fit=crop"
        ],
        "rating": 3.6,
        "reviews_count": 245,
        "stock": 50,
        "tags": ["brightening", "vitamin-c", "anti-aging"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-2",
        "name": "Hydrating Night Cream",
        "description": "Deep moisturizing cream with hyaluronic acid and peptides for overnight skin renewal.",
        "price": 125.00,
        "original_price": 165.00,
        "category": "Skincare",
        "brand": "Nuit Beauté",
        "image": "https://images.unsplash.com/photo-1629732097571-b042b35aa3ed?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1629732097571-b042b35aa3ed?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.9,
        "reviews_count": 312,
        "stock": 35,
        "tags": ["hydrating", "night-cream", "anti-aging"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-3",
        "name": "Retinol Treatment Serum",
        "description": "Professional-grade retinol serum for reducing fine lines and improving skin texture.",
        "price": 95.00,
        "original_price": 135.00,
        "category": "Skincare",
        "brand": "LuxeDerm",
        "image": "https://images.unsplash.com/photo-1768254636839-9a2d2619c861?q=80&w=1160&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1768254636839-9a2d2619c861?q=80&w=1160&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1590439471364-192aa70c0b53?w=800&auto=format&fit=crop"
        ],
        "rating": 4.7,
        "reviews_count": 189,
        "stock": 42,
        "tags": ["retinol", "anti-aging", "treatment"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-4",
        "name": "Gentle Cleansing Foam",
        "description": "Luxurious foaming cleanser that removes impurities while maintaining skin's natural moisture.",
        "price": 42.00,
        "original_price": 58.00,
        "category": "Skincare",
        "brand": "Pure Essence",
        "image": "https://images.unsplash.com/photo-1731577178007-d48d92fd30fc?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1731577178007-d48d92fd30fc?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1567721913486-6585f069b332?w=800&auto=format&fit=crop"
        ],
        "rating": 3.0,
        "reviews_count": 156,
        "stock": 65,
        "tags": ["cleanser", "gentle", "foam"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-5",
        "name": "Eye Revive Complex",
        "description": "Targeted eye cream with caffeine and peptides to reduce dark circles and puffiness.",
        "price": 78.00,
        "original_price": 98.00,
        "category": "Skincare",
        "brand": "Nuit Beauté",
        "image": "https://images.unsplash.com/photo-1602037299890-c593f4c81d47?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1602037299890-c593f4c81d47?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=800&auto=format&fit=crop"
        ],
        "rating": 4.8,
        "reviews_count": 203,
        "stock": 38,
        "tags": ["eye-cream", "dark-circles", "anti-aging"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-6",
        "name": "Exfoliating Toner",
        "description": "AHA/BHA toner that gently exfoliates and refines pores for smoother, clearer skin.",
        "price": 52.00,
        "original_price": 72.00,
        "category": "Skincare",
        "brand": "Pure Essence",
        "image": "https://images.unsplash.com/photo-1616986953793-2e6159b78580?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1616986953793-2e6159b78580?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1612817288484-6f916006741a?w=800&auto=format&fit=crop"
        ],
        "rating": 4.7,
        "reviews_count": 178,
        "stock": 55,
        "tags": ["toner", "exfoliating", "aha-bha"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-7",
        "name": "Niacinamide Brightening Serum",
        "description": "Multi-tasking serum with niacinamide to minimize pores and improve skin texture.",
        "price": 68.00,
        "original_price": 92.00,
        "category": "Skincare",
        "brand": "LuxeDerm",
        "image": "https://images.unsplash.com/photo-1766940095250-5c7715ab57ea?q=80&w=1160&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1766940095250-5c7715ab57ea?q=80&w=1160&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 2.0,
        "reviews_count": 267,
        "stock": 48,
        "tags": ["niacinamide", "brightening", "serum"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-8",
        "name": "Moisture Surge Gel",
        "description": "Lightweight gel moisturizer with hyaluronic acid for instant hydration.",
        "price": 58.00,
        "original_price": 78.00,
        "category": "Skincare",
        "brand": "Pure Essence",
        "image": "https://images.unsplash.com/photo-1673847401561-fcd75a7888c5?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1673847401561-fcd75a7888c5?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.6,
        "reviews_count": 192,
        "stock": 52,
        "tags": ["moisturizer", "gel", "hydrating"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-9",
        "name": "SPF 50 Invisible Sunscreen",
        "description": "Broad-spectrum sunscreen with invisible finish and antioxidant protection.",
        "price": 45.00,
        "original_price": 62.00,
        "category": "Skincare",
        "brand": "Nuit Beauté",
        "image": "https://images.unsplash.com/photo-1598662957563-ee4965d4d72c?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1598662957563-ee4965d4d72c?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 3.5,
        "reviews_count": 224,
        "stock": 70,
        "tags": ["sunscreen", "spf-50", "protection"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-10",
        "name": "Rose Water Face Mist",
        "description": "Refreshing face mist with pure rose water and botanical extracts for instant hydration.",
        "price": 38.00,
        "original_price": 52.00,
        "category": "Skincare",
        "brand": "Pure Essence",
        "image": "https://images.unsplash.com/photo-1599847935464-fde3827639c2?q=80&w=928&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1599847935464-fde3827639c2?q=80&w=928&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.5,
        "reviews_count": 143,
        "stock": 80,
        "tags": ["mist", "rose-water", "hydrating"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    # MAKEUP PRODUCTS (10)
    {
        "id": "prod-11",
        "name": "Velvet Matte Lipstick - Ruby Rouge",
        "description": "Long-lasting velvet matte lipstick with rich pigmentation and comfortable wear.",
        "price": 32.00,
        "original_price": 45.00,
        "category": "Makeup",
        "brand": "Glamour Paris",
        "image": "https://images.unsplash.com/photo-1600852306752-085ca3285361?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1600852306752-085ca3285361?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 2.5,
        "reviews_count": 198,
        "stock": 85,
        "tags": ["lipstick", "matte", "red"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-12",
        "name": "Flawless Foundation - Porcelain",
        "description": "Medium to full coverage foundation with natural finish and 24-hour wear.",
        "price": 58.00,
        "original_price": 78.00,
        "category": "Makeup",
        "brand": "Beauté Noir",
        "image": "https://images.unsplash.com/photo-1627885793933-584e53987c14?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1627885793933-584e53987c14?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.8,
        "reviews_count": 287,
        "stock": 62,
        "tags": ["foundation", "full-coverage", "long-lasting"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-13",
        "name": "Eyeshadow Palette - Sunset Dreams",
        "description": "12-shade eyeshadow palette with warm neutrals and shimmering metallics.",
        "price": 68.00,
        "original_price": 88.00,
        "category": "Makeup",
        "brand": "Glamour Paris",
        "image": "https://images.unsplash.com/photo-1547934659-7fa699ef3ce0?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1547934659-7fa699ef3ce0?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.9,
        "reviews_count": 342,
        "stock": 45,
        "tags": ["eyeshadow", "palette", "warm-tones"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-14",
        "name": "Volumizing Mascara",
        "description": "Dramatic volume and length mascara with smudge-proof formula.",
        "price": 28.00,
        "original_price": 38.00,
        "category": "Makeup",
        "brand": "Beauté Noir",
        "image": "https://images.unsplash.com/photo-1619406266880-7e130b6c65c0?q=80&w=770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1619406266880-7e130b6c65c0?q=80&w=770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.6,
        "reviews_count": 215,
        "stock": 95,
        "tags": ["mascara", "volumizing", "smudge-proof"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-15",
        "name": "Liquid Highlighter - Champagne Glow",
        "description": "Buildable liquid highlighter for a radiant, dewy finish.",
        "price": 42.00,
        "original_price": 58.00,
        "category": "Makeup",
        "brand": "Glamour Paris",
        "image": "https://images.unsplash.com/photo-1501728636520-11c972bd5e2e?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1501728636520-11c972bd5e2e?q=80&w=872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.8,
        "reviews_count": 176,
        "stock": 58,
        "tags": ["highlighter", "liquid", "glow"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-16",
        "name": "Brow Sculpting Pencil",
        "description": "Precision brow pencil with spoolie brush for natural-looking brows.",
        "price": 22.00,
        "original_price": 32.00,
        "category": "Makeup",
        "brand": "Beauté Noir",
        "image": "https://images.unsplash.com/photo-1597225244660-1cd128c64284?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1597225244660-1cd128c64284?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.7,
        "reviews_count": 164,
        "stock": 72,
        "tags": ["brow", "pencil", "sculpting"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-17",
        "name": "Blush Duo - Rose Petal",
        "description": "Silky powder blush duo for a natural flush of color.",
        "price": 38.00,
        "original_price": 52.00,
        "category": "Makeup",
        "brand": "Glamour Paris",
        "image": "https://images.unsplash.com/photo-1625093525885-282384697917?q=80&w=1602&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1625093525885-282384697917?q=80&w=1602&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.6,
        "reviews_count": 189,
        "stock": 64,
        "tags": ["blush", "powder", "duo"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-18",
        "name": "Setting Spray - All Day Lock",
        "description": "Makeup setting spray that keeps your look fresh for up to 16 hours.",
        "price": 35.00,
        "original_price": 48.00,
        "category": "Makeup",
        "brand": "Beauté Noir",
        "image": "https://images.unsplash.com/photo-1679973519230-10b9d160465a?q=80&w=854&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1679973519230-10b9d160465a?q=80&w=854&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.8,
        "reviews_count": 231,
        "stock": 78,
        "tags": ["setting-spray", "long-lasting", "finish"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-19",
        "name": "Lip Gloss - Crystal Shine",
        "description": "High-shine lip gloss with hydrating formula and non-sticky texture.",
        "price": 24.00,
        "original_price": 34.00,
        "category": "Makeup",
        "brand": "Glamour Paris",
        "image": "https://images.unsplash.com/photo-1640317372997-b76e600ee5ef?q=80&w=928&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1640317372997-b76e600ee5ef?q=80&w=928&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.5,
        "reviews_count": 152,
        "stock": 88,
        "tags": ["lip-gloss", "shine", "hydrating"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-20",
        "name": "Eyeliner Pen - Midnight Black",
        "description": "Precision felt-tip eyeliner for perfect winged looks every time.",
        "price": 26.00,
        "original_price": 36.00,
        "category": "Makeup",
        "brand": "Beauté Noir",
        "image": "https://images.unsplash.com/photo-1668255446079-b15fd061735d?q=80&w=930&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1668255446079-b15fd061735d?q=80&w=930&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.7,
        "reviews_count": 203,
        "stock": 82,
        "tags": ["eyeliner", "pen", "precision"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    # PERFUME PRODUCTS (10)
    {
        "id": "prod-21",
        "name": "Noir Elegance Eau de Parfum",
        "description": "Sophisticated oriental fragrance with notes of bergamot, jasmine, and sandalwood.",
        "price": 145.00,
        "original_price": 185.00,
        "category": "Perfume",
        "brand": "Maison de Luxe",
        "image": "https://images.unsplash.com/photo-1709095458514-573bc6277d3d?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1709095458514-573bc6277d3d?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.9,
        "reviews_count": 312,
        "stock": 35,
        "tags": ["perfume", "oriental", "luxury"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-22",
        "name": "Rose Garden Eau de Toilette",
        "description": "Fresh floral fragrance featuring rose, peony, and white musk.",
        "price": 98.00,
        "original_price": 128.00,
        "category": "Perfume",
        "brand": "Bloom Paris",
        "image": "https://images.unsplash.com/photo-1769038933775-305885b212c1?q=80&w=776&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1769038933775-305885b212c1?q=80&w=776&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1615634260167-c8cdede054de?w=800&auto=format&fit=crop"
        ],
        "rating": 4.7,
        "reviews_count": 245,
        "stock": 48,
        "tags": ["perfume", "floral", "rose"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-23",
        "name": "Midnight Oud Intense",
        "description": "Bold woody fragrance with oud, amber, and leather notes.",
        "price": 165.00,
        "original_price": 210.00,
        "category": "Perfume",
        "brand": "Maison de Luxe",
        "image": "https://images.unsplash.com/photo-1757313226065-f5e129c5f73f?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1757313226065-f5e129c5f73f?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1523293182086-7651a899d37f?w=800&auto=format&fit=crop"
        ],
        "rating": 4.8,
        "reviews_count": 189,
        "stock": 28,
        "tags": ["perfume", "woody", "oud"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-24",
        "name": "Citrus Breeze Fresh",
        "description": "Energizing citrus fragrance with lemon, grapefruit, and mint.",
        "price": 78.00,
        "original_price": 105.00,
        "category": "Perfume",
        "brand": "Bloom Paris",
        "image": "https://images.unsplash.com/photo-1757313231524-6504c839ca0b?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1757313231524-6504c839ca0b?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1563170351-be82bc888aa4?w=800&auto=format&fit=crop"
        ],
        "rating": 4.6,
        "reviews_count": 167,
        "stock": 55,
        "tags": ["perfume", "citrus", "fresh"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-25",
        "name": "Vanilla Velvet Eau de Parfum",
        "description": "Warm gourmand fragrance with vanilla, tonka bean, and caramel.",
        "price": 112.00,
        "original_price": 145.00,
        "category": "Perfume",
        "brand": "Maison de Luxe",
        "image": "https://images.unsplash.com/photo-1757313236346-d5d7ff5ffaab?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1757313236346-d5d7ff5ffaab?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.8,
        "reviews_count": 278,
        "stock": 42,
        "tags": ["perfume", "vanilla", "gourmand"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-26",
        "name": "Ocean Mist Eau de Toilette",
        "description": "Aquatic fragrance with sea salt, lavender, and cedarwood.",
        "price": 88.00,
        "original_price": 118.00,
        "category": "Perfume",
        "brand": "Bloom Paris",
        "image": "https://images.unsplash.com/photo-1760113559708-84e7a148ec68?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1760113559708-84e7a148ec68?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1587017539504-67cfbddac569?w=800&auto=format&fit=crop"
        ],
        "rating": 4.7,
        "reviews_count": 198,
        "stock": 52,
        "tags": ["perfume", "aquatic", "fresh"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-27",
        "name": "Amber Nights Intense",
        "description": "Rich amber fragrance with spices, tobacco, and patchouli.",
        "price": 155.00,
        "original_price": 195.00,
        "category": "Perfume",
        "brand": "Maison de Luxe",
        "image": "https://images.unsplash.com/photo-1680503504111-1bbc7fc2103e?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1680503504111-1bbc7fc2103e?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?w=800&auto=format&fit=crop"
        ],
        "rating": 4.9,
        "reviews_count": 234,
        "stock": 32,
        "tags": ["perfume", "amber", "spicy"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-28",
        "name": "Jasmine Dream Eau de Parfum",
        "description": "Romantic floral fragrance with jasmine, tuberose, and orange blossom.",
        "price": 125.00,
        "original_price": 162.00,
        "category": "Perfume",
        "brand": "Bloom Paris",
        "image": "https://images.unsplash.com/photo-1762518883925-cb26fdeb51cb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1762518883925-cb26fdeb51cb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.8,
        "reviews_count": 267,
        "stock": 38,
        "tags": ["perfume", "floral", "jasmine"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-29",
        "name": "Black Pepper & Vetiver",
        "description": "Contemporary spicy fragrance with black pepper, vetiver, and cedarwood.",
        "price": 135.00,
        "original_price": 172.00,
        "category": "Perfume",
        "brand": "Maison de Luxe",
        "image": "https://images.unsplash.com/photo-1759793500112-c588839cfc6e?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "images": [
            "https://images.unsplash.com/photo-1759793500112-c588839cfc6e?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ],
        "rating": 4.7,
        "reviews_count": 212,
        "stock": 44,
        "tags": ["perfume", "spicy", "woody"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    {
        "id": "prod-30",
        "name": "Cherry Blossom Bliss",
        "description": "Delicate floral fragrance with cherry blossom, magnolia, and sandalwood.",
        "price": 95.00,
        "original_price": 125.00,
        "category": "Perfume",
        "brand": "Bloom Paris",
        "image": "https://images.unsplash.com/photo-1563170351-be82bc888aa4?w=800&auto=format&fit=crop",
        "images": [
            "https://images.unsplash.com/photo-1563170351-be82bc888aa4?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1547887537-6158d64c35b3?w=800&auto=format&fit=crop"
        ],
        "rating": 4.6,
        "reviews_count": 186,
        "stock": 58,
        "tags": ["perfume", "floral", "cherry-blossom"],
        "created_at": datetime.now(timezone.utc).isoformat()
    },
    # HAIR TOOLS PRODUCTS (5)
    {
        "id": "prod-31",
        "name": "Professional Ceramic Hair Dryer",
        "description": "Ionic ceramic hair dryer with 3 heat settings and cool shot button for salon-quality results.",
        "price": 89.00,
        "original_price": 125.00,
        "category": "Hair Tools",
        "brand": "StylePro",
        "image": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?q=80&w=800&auto=format&fit=crop",
        "images": [
            "https://images.unsplash.com/photo-1522338140262-f46f5913618a?q=80&w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?w=800&auto=format&fit=crop",
                    ],
        "rating": 4.3,
        "reviews_count": 421,
        "stock": 45,
        "tags": ["hair-dryer", "ceramic", "ionic"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-32",
        "name": "Titanium Flat Iron Straightener",
        "description": "Professional titanium flat iron with adjustable temperature control up to 450°F for all hair types.",
        "price": 115.00,
        "original_price": 165.00,
        "category": "Hair Tools",
        "brand": "GlamTech",
        "image":             "https://plus.unsplash.com/premium_photo-1679165921201-1438892682ac?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",

        "images": [
            "https://images.unsplash.com/photo-1634449571010-02389ed0f9b0?w=800&auto=format&fit=crop",
        ],
        "rating": 2.8,
        "reviews_count": 356,
        "stock": 32,
        "tags": ["straightener", "flat-iron", "titanium"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-33",
        "name": "Automatic Curling Wand",
        "description": "Revolutionary auto-rotating curling wand with ceramic barrel for effortless curls in seconds.",
        "price": 78.00,
        "original_price": 105.00,
        "category": "Hair Tools",
        "brand": "StylePro",
        "image":             "https://plus.unsplash.com/premium_photo-1669675934616-5f1dadb467e7?q=80&w=792&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",

        "images": [
                        "https://plus.unsplash.com/premium_photo-1669675934616-5f1dadb467e7?q=80&w=792&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

        ],
        "rating": 3.9,
        "reviews_count": 289,
        "stock": 58,
        "tags": ["curling-wand", "automatic", "ceramic"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-34",
        "name": "Hot Air Styling Brush",
        "description": "2-in-1 hot air brush combines drying and styling for smooth, voluminous blowouts at home.",
        "price": 65.00,
        "original_price": 88.00,
        "category": "Hair Tools",
        "brand": "GlamTech",
        "image":             "https://images.unsplash.com/photo-1713180758582-9bac6bc62a26?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://images.unsplash.com/photo-1713180758582-9bac6bc62a26?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.5,
        "reviews_count": 512,
        "stock": 67,
        "tags": ["styling-brush", "hot-air", "volumizing"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-35",
        "name": "Travel Mini Hair Straightener",
        "description": "Compact dual voltage mini straightener perfect for travel with rapid heat-up technology.",
        "price": 38.00,
        "original_price": 52.00,
        "category": "Hair Tools",
        "brand": "StylePro",
        "image":             "https://images.unsplash.com/photo-1712481846921-d5df6dc4abfd?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://images.unsplash.com/photo-1582095133179-bfd08e2fc6b3?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1712481846921-d5df6dc4abfd?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 3.2,
        "reviews_count": 178,
        "stock": 95,
        "tags": ["travel", "mini", "straightener"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    # BRUSHES PRODUCTS (5)
    {
        "id": "prod-36",
        "name": "Detangling Paddle Brush",
        "description": "Wide paddle brush with flexible bristles that glide through tangles without pulling or breaking hair.",
        "price": 24.00,
        "original_price": 35.00,
        "category": "Brushes",
        "brand": "TresseTools",
        "image":            "https://plus.unsplash.com/premium_photo-1664544673682-ccddf20d1289?q=80&w=830&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://plus.unsplash.com/premium_photo-1664544673682-ccddf20d1289?q=80&w=830&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.6,
        "reviews_count": 534,
        "stock": 120,
        "tags": ["paddle-brush", "detangling", "flexible"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-37",
        "name": "Round Ceramic Blow Dry Brush",
        "description": "Professional round ceramic brush with boar bristles for perfect blowouts and added shine.",
        "price": 32.00,
        "original_price": 45.00,
        "category": "Brushes",
        "brand": "StylePro",
        "image":             "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
           
            "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 2.7,
        "reviews_count": 267,
        "stock": 78,
        "tags": ["round-brush", "ceramic", "blow-dry"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-38",
        "name": "Vented Quick-Dry Brush",
        "description": "Vented design accelerates drying time by allowing maximum airflow while styling.",
        "price": 28.00,
        "original_price": 38.00,
        "category": "Brushes",
        "brand": "TresseTools",
        "image": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?q=80&w=800&auto=format&fit=crop",
        "images": [
            "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?q=80&w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1703353288357-c7efb9e6573a?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.1,
        "reviews_count": 392,
        "stock": 88,
        "tags": ["vented", "quick-dry", "styling"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-39",
        "name": "Teasing & Volume Brush",
        "description": "Fine-tooth teasing brush for creating volume and backcombing with precision control.",
        "price": 18.00,
        "original_price": 26.00,
        "category": "Brushes",
        "brand": "StylePro",
        "image": "https://images.unsplash.com/photo-1621607512214-68297480165e?q=80&w=800&auto=format&fit=crop",
        "images": [
            "https://images.unsplash.com/photo-1621607512214-68297480165e?q=80&w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800&auto=format&fit=crop",
        ],
        "rating": 3.4,
        "reviews_count": 198,
        "stock": 142,
        "tags": ["teasing", "volume", "backcombing"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-40",
        "name": "Boar Bristle Finishing Brush",
        "description": "100% natural boar bristle brush that distributes oils and adds incredible shine to finished styles.",
        "price": 42.00,
        "original_price": 58.00,
        "category": "Brushes",
        "brand": "TresseTools",
        "image": "https://plus.unsplash.com/premium_photo-1759833579706-19478d0a7e53?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800&auto=format&fit=crop",
        ],
        "rating": 4.8,
        "reviews_count": 445,
        "stock": 65,
        "tags": ["boar-bristle", "finishing", "shine"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    # BATH & BODY PRODUCTS (5)
    {
        "id": "prod-41",
        "name": "Lavender Dreams Bath Soak",
        "description": "Luxurious mineral bath soak infused with lavender essential oil and Epsom salts for deep relaxation.",
        "price": 32.00,
        "original_price": 45.00,
        "category": "Bath and Body",
        "brand": "Serenity Spa",
        "image":             "https://images.unsplash.com/photo-1626897845060-c4c89a918f51?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://images.unsplash.com/photo-1626897845060-c4c89a918f51?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.7,
        "reviews_count": 328,
        "stock": 72,
        "tags": ["bath-soak", "lavender", "relaxation"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-42",
        "name": "Shea Butter Body Cream",
        "description": "Rich, nourishing body cream with pure shea butter and vitamin E for silky smooth skin.",
        "price": 28.00,
        "original_price": 38.00,
        "category": "Bath and Body",
        "brand": "Pure Radiance",
        "image":             "https://images.unsplash.com/photo-1703174323653-0455deaf7f11?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            
            "https://images.unsplash.com/photo-1703174323653-0455deaf7f11?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 2.9,
        "reviews_count": 486,
        "stock": 94,
        "tags": ["body-cream", "shea-butter", "moisturizing"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-43",
        "name": "Coconut Sugar Body Scrub",
        "description": "Exfoliating sugar scrub with coconut oil that buffs away dead skin and leaves you glowing.",
        "price": 35.00,
        "original_price": 48.00,
        "category": "Bath and Body",
        "brand": "Serenity Spa",
        "image":             "https://images.unsplash.com/photo-1677769237703-629d082d89bb?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
           
            "https://images.unsplash.com/photo-1677769237703-629d082d89bb?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.4,
        "reviews_count": 372,
        "stock": 68,
        "tags": ["body-scrub", "coconut", "exfoliating"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-44",
        "name": "Eucalyptus Shower Gel",
        "description": "Refreshing eucalyptus shower gel that cleanses and invigorates with cooling menthol notes.",
        "price": 22.00,
        "original_price": 32.00,
        "category": "Bath and Body",
        "brand": "Pure Radiance",
        "image": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?q=80&w=800&auto=format&fit=crop",
        "images": [
           "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?q=80&w=800&auto=format&fit=crop"
        ],
        "rating": 3.6,
        "reviews_count": 254,
        "stock": 110,
        "tags": ["shower-gel", "eucalyptus", "refreshing"],
        "created_at": "2026-02-12T00:00:00Z"
    },
    {
        "id": "prod-45",
        "name": "Vitamin C Body Oil",
        "description": "Brightening body oil with vitamin C and rosehip that nourishes and evens skin tone.",
        "price": 45.00,
        "original_price": 62.00,
        "category": "Bath and Body",
        "brand": "Serenity Spa",
        "image":"https://images.unsplash.com/photo-1556760544-74068565f05c?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
,
        "images": [
            "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop",
           
            "https://images.unsplash.com/photo-1556760544-74068565f05c?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        ],
        "rating": 4.2,
        "reviews_count": 219,
        "stock": 56,
        "tags": ["body-oil", "vitamin-c", "brightening"],
        "created_at": "2026-02-12T00:00:00Z"
    }
]

async def seed_database():
    print("Seeding database...")
    
    # Clear existing products
    await db.products.delete_many({})
    
    # Insert products
    await db.products.insert_many(products)
    
    print(f"Seeded {len(products)} products successfully!")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())