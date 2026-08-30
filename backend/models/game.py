from sqlalchemy import Column, String, Float, text
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

    keywords = relationship(
        "Keyword",
        secondary=games_keywords,
        back_populates="games"
    )