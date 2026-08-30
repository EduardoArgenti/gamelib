import uuid

from sqlalchemy.orm import Session

from models.games_keywords import games_keywords


def add_game_keyword(
    db: Session,
    game_id: str,
    keyword_id: str
):
    db.execute(
        games_keywords.insert().values(
            id = str(uuid.uuid4()),
            game_id=game_id,
            keyword_id=keyword_id
        )
    )