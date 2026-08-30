import uuid

from sqlalchemy.orm import Session, selectinload

from models.game import Game
from schemas.game import GameCreate


def get_all_games(db: Session):
    return (
        db.query(Game)
        .options(selectinload(Game.keywords))
        .all()
    )

def create_game(db: Session, game_data: GameCreate):
    new_game = Game(
        id = str(uuid.uuid4()),
        name=game_data.name,
        publisher=game_data.publisher,
        developer=game_data.developer,
        release_date=game_data.release_date,
        avg_time=game_data.avg_time,
        platforms=game_data.platforms
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game