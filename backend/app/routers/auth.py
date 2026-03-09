from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.auth.supabase_auth import CurrentUser
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest, SessionResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=AuthResponse)
async def register(_payload: RegisterRequest) -> AuthResponse:
    return AuthResponse(message="Registration stub ready. Wire Supabase sign-up flow here.")


@router.post("/login", response_model=AuthResponse)
async def login(_payload: LoginRequest) -> AuthResponse:
    return AuthResponse(message="Login stub ready. Wire Supabase sign-in flow here.")


@router.post("/logout", response_model=AuthResponse)
async def logout(_user: Mapping[str, Any] = CurrentUser) -> AuthResponse:
    return AuthResponse(message="Logout stub ready. Revoke/clear session logic can be added here.")


@router.get("/session", response_model=SessionResponse)
async def session(user: Mapping[str, Any] = CurrentUser) -> SessionResponse:
    return SessionResponse(user_id=str(user.get("sub")), email=user.get("email"))
