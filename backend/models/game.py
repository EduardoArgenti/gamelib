from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship

from database import Base
from models.games_keywords import games_keywords


class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True)
    name = Column(String)
    publisher = Column(String)
    developer = Column(String)
    release_date = Column(String)
    avg_time = Column(Float)
    platforms = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    deleted_at = Column(String)

    keywords = relationship(
        "Keyword",
        secondary=games_keywords,
        back_populates="games"
    )