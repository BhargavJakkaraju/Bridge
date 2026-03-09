from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.auth.supabase_auth import CurrentUser
from app.schemas.paper import PaperItem, PaperListResponse, SavePaperRequest, SavePaperResponse

router = APIRouter(prefix="/papers", tags=["papers"])


@router.get("", response_model=PaperListResponse)
async def list_papers(_user: Mapping[str, Any] = CurrentUser) -> PaperListResponse:
    return PaperListResponse(items=[PaperItem(paper_id="stub-paper-1", title="Stub Paper", summary="Placeholder summary")])


@router.get("/{paper_id}", response_model=PaperItem)
async def get_paper(paper_id: str, _user: Mapping[str, Any] = CurrentUser) -> PaperItem:
    return PaperItem(paper_id=paper_id, title="Stub Paper Detail", summary="Detailed paper endpoint stub.")


@router.post("/save", response_model=SavePaperResponse)
async def save_paper(_payload: SavePaperRequest, _user: Mapping[str, Any] = CurrentUser) -> SavePaperResponse:
    return SavePaperResponse(message="Save paper stub ready.")
