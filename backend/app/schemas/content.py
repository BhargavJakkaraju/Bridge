from pydantic import BaseModel


class ContentCard(BaseModel):
    card_id: str
    text_summary: str
    video_url: str | None = None
    audio_url: str | None = None
    applet_url: str | None = None


class FeedResponse(BaseModel):
    cards: list[ContentCard]
