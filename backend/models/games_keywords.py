from sqlalchemy import Table, Column, String, ForeignKey, text

from database import Base


games_keywords = Table(
    "games_keywords",
    Base.metadata,

    Column(
        "id",
        String,
        primary_key=True
    ),

    Column(
        "game_id",
        String,
        ForeignKey("games.id"),
        nullable=False
    ),

    Column(
        "keyword_id",
        String,
        ForeignKey("keywords.id"),
        nullable=False
    ),

    Column(
        "created_at",
        String,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    ),

    Column(
        "updated_at",
        String,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    ),

    Column(
        "deleted_at",
        String,
        nullable=True
    )
)