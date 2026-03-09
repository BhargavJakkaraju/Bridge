from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.database import Base, engine
from app.models import paper, search, user  # noqa: F401
from app.routers import auth, content, papers, profile, search as search_router

app = FastAPI(title=settings.app_name, debug=settings.app_debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(search_router.router, prefix=settings.api_v1_prefix)
app.include_router(papers.router, prefix=settings.api_v1_prefix)
app.include_router(content.router, prefix=settings.api_v1_prefix)
app.include_router(profile.router, prefix=settings.api_v1_prefix)


@app.on_event("startup")
def on_startup() -> None:
    if settings.skip_db_init:
        return
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
