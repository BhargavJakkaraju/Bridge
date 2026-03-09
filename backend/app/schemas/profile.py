from pydantic import BaseModel


class ProfileResponse(BaseModel):
    email: str | None = None
    full_name: str | None = None
    preferred_domain: str | None = None
    ai_expertise: str | None = None


class ProfileUpdateRequest(BaseModel):
    full_name: str | None = None
    preferred_domain: str | None = None
    ai_expertise: str | None = None
