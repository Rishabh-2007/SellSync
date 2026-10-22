from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.db.session import engine, Base, SessionLocal
from app.api.router import api_router
from app.services.seed_service import SeedService
from app.models.channel import Channel
from fastapi.staticfiles import StaticFiles
from pathlib import Path

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Auto-seed if database is empty
    db = SessionLocal()
    try:
        channel_count = db.query(Channel).count()
        if channel_count == 0 or settings.AUTO_SEED:
            SeedService.reset_and_seed_database(db)
    finally:
        db.close()
        
    yield

app = FastAPI(
    title="SellSync API",
    description="Unified Commerce Management Platform API for Micro-Sellers",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


# Serve the compiled React app from the same service in production.
# API routes above take precedence; all other paths fall back to the SPA.
_frontend_dist = Path(__file__).resolve().parents[2] / "frontend-dist"
if _frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(_frontend_dist), html=True), name="frontend")
