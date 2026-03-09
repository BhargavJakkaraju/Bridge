from pydantic import BaseModel


class SearchRequest(BaseModel):
    domain: str
    domain_custom: str | None = None
    ai_expertise: str


class SearchResponse(BaseModel):
    request_id: str
    status: str
    message: str
