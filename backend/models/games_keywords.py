from sqlalchemy import Table, Column, String, ForeignKey

from database import Base


games_keywords = Table(
    "games_keywords",
    Base.metadata,
    Column(
        "game_id",
        String,
        ForeignKey("games.id"),
        primary_key=True
    ),
    Column(
        "keyword_id",
        String,
        ForeignKey("keywords.id"),
        primary_key=True
    ),
)