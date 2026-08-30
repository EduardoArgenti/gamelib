from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import Base
from models.games_keywords import games_keywords


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(String, primary_key=True)
    name = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    deleted_at = Column(String)

    games = relationship(
        "Game",
        secondary=games_keywords,
        back_populates="keywords"
    )