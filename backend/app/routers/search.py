import uuid
from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.auth.supabase_auth import CurrentUser
from app.schemas.search import SearchRequest, SearchResponse

router = APIRouter(prefix="/search", tags=["search"])


@router.post("", response_model=SearchResponse)
async def create_search(_payload: SearchRequest, _user: Mapping[str, Any] = CurrentUser) -> SearchResponse:
    return SearchResponse(
        request_id=str(uuid.uuid4()),
        status="queued",
        message="Search stub created. Retrieval and orchestration logic pending.",
    )
