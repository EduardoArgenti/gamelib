from sqlalchemy.orm import Session

from repositories.games import get_all_games
from repositories.games import create_game as create_game_repository
from repositories.games_keywords import add_game_keyword
from schemas.game import GameCreate

from services.keywords import get_or_create_keyword

def get_games(db: Session):
    games = get_all_games(db)

    return [
        {
            "id": game.id,
            "name": game.name,
            "publisher": game.publisher,
            "developer": game.developer,
            "keywords": [
                keyword.name
                for keyword in game.keywords
                if keyword.deleted_at is None
            ],
            "release_date": game.release_date,
            "avg_time": game.avg_time,
            "platforms": game.platforms,
            "created_at": game.created_at,
            "updated_at": game.updated_at,
            "deleted_at": game.deleted_at,
        }
        for game in games
    ]

def create_game(db: Session, game: GameCreate):
    try:
        keywords = []

        for keyword_name in game.keywords:
            keyword = get_or_create_keyword(
                db,
                keyword_name
            )

            keywords.append(keyword)

        new_game = create_game_repository(
            db,
            game
        )

        for keyword in keywords:
            add_game_keyword(
                db,
                new_game.id,
                keyword.id
            )

        db.commit()
        db.refresh(new_game)

        return new_game

    except Exception:
        db.rollback()
        raise