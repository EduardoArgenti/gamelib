from typing import List, Optional

from pydantic import BaseModel


class GameCreate(BaseModel):
    name: str
    publisher: str
    developer: str
    keywords: List[str]
    release_date: str
    avg_time: Optional[float] = None
    platforms: Optional[str] = None

class GameResponse(BaseModel):
    id: str
    name: str
    publisher: str
    developer: str
    keywords: List[str]
    release_date: str
    avg_time: Optional[float] = None
    platforms: Optional[str] = None

    class Config:
        orm_mode = True