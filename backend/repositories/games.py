from sqlalchemy.orm import Session

from models.game import Game


def get_all_games(db: Session):
    return db.query(Game).all()