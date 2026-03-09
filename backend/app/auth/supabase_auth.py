from collections.abc import Mapping
from typing import Any

import httpx
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from app.core.config import settings

bearer_scheme = HTTPBearer(auto_error=True)


class SupabaseJWTValidator:
    def __init__(self) -> None:
        self._jwks: dict[str, Any] | None = None

    async def _load_jwks(self) -> dict[str, Any]:
        if self._jwks is not None:
            return self._jwks

        if not settings.supabase_jwks_url:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="SUPABASE_JWKS_URL is not configured",
            )

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(settings.supabase_jwks_url)
            response.raise_for_status()
            self._jwks = response.json()
            return self._jwks

    async def validate_token(self, token: str) -> dict[str, Any]:
        if not settings.supabase_jwt_secret and not settings.supabase_jwks_url:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Supabase JWT settings are not configured",
            )

        try:
            if settings.supabase_jwt_secret:
                payload = jwt.decode(token, settings.supabase_jwt_secret, algorithms=["HS256"], options={"verify_aud": False})
                return payload

            headers = jwt.get_unverified_header(token)
            kid = headers.get("kid")
            jwks = await self._load_jwks()
            keys = jwks.get("keys", [])
            key_data = next((key for key in keys if key.get("kid") == kid), None)
            if key_data is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token key id")

            payload = jwt.decode(token, key_data, algorithms=["RS256"], options={"verify_aud": False})
            return payload
        except JWTError as exc:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
        except httpx.HTTPError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Unable to fetch Supabase JWKS",
            ) from exc


validator = SupabaseJWTValidator()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme),
) -> Mapping[str, Any]:
    token = credentials.credentials
    payload = await validator.validate_token(token)

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing subject")

    return payload


CurrentUser = Depends(get_current_user)
