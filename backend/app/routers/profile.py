from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.auth.supabase_auth import CurrentUser
from app.schemas.profile import ProfileResponse, ProfileUpdateRequest

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("", response_model=ProfileResponse)
async def get_profile(user: Mapping[str, Any] = CurrentUser) -> ProfileResponse:
    return ProfileResponse(email=user.get("email"), full_name=None, preferred_domain=None, ai_expertise=None)


@router.put("", response_model=ProfileResponse)
async def update_profile(payload: ProfileUpdateRequest, user: Mapping[str, Any] = CurrentUser) -> ProfileResponse:
    return ProfileResponse(
        email=user.get("email"),
        full_name=payload.full_name,
        preferred_domain=payload.preferred_domain,
        ai_expertise=payload.ai_expertise,
    )
