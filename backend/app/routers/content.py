from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.auth.supabase_auth import CurrentUser
from app.schemas.content import ContentCard, FeedResponse

router = APIRouter(prefix="/content", tags=["content"])


@router.get("/feed", response_model=FeedResponse)
async def get_feed(_user: Mapping[str, Any] = CurrentUser) -> FeedResponse:
    return FeedResponse(
        cards=[
            ContentCard(
                card_id="stub-card-1",
                text_summary="This is a placeholder summary card.",
                video_url=None,
                audio_url=None,
                applet_url=None,
            )
        ]
    )
