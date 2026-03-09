from pydantic import BaseModel


class PaperItem(BaseModel):
    paper_id: str
    title: str
    summary: str | None = None


class PaperListResponse(BaseModel):
    items: list[PaperItem]


class SavePaperRequest(BaseModel):
    paper_id: str


class SavePaperResponse(BaseModel):
    message: str
