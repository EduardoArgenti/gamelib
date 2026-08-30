from sqlalchemy import Column, String, text
from sqlalchemy.orm import relationship

from database import Base
from models.games_keywords import games_keywords


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    created_at = Column(
        String,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )

    updated_at = Column(
        String,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )

    deleted_at = Column(
        String,
        nullable=True
    )

    games = relationship(
        "Game",
        secondary=games_keywords,
        back_populates="keywords"
    )