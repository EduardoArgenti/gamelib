from typing import List, Optional

from pydantic import BaseModel


class GameResponse(BaseModel):
    id: str
    name: str
    publisher: str
    developer: str
    keywords: List[str]
    release_date: str
    avg_time: float
    platforms: Optional[str]
    created_at: str
    updated_at: str
    deleted_at: str

    class Config:
        orm_mode = True