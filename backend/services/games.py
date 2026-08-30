from sqlalchemy.orm import Session

from repositories.games import get_all_games


def get_games(db: Session):
    games = get_all_games(db)

    return [
        {
            "id": game.id,
            "name": game.name,
            "publisher": game.publisher,
            "developer": game.developer,
            "keywords": [keyword.name for keyword in game.keywords],
            "release_date": game.release_date,
            "avg_time": game.avg_time,
            "platforms": game.platforms,
            "created_at": game.created_at,
            "updated_at": game.updated_at,
            "deleted_at": game.deleted_at,
        }
        for game in games
    ]