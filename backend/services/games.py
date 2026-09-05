from sqlalchemy.orm import Session

from repositories.games import get_all_games
from repositories.games import get_game as get_game_repository
from repositories.games import create_game as create_game_repository
from repositories.games import delete_game as delete_game_repository
from repositories.games_keywords import add_game_keyword
from schemas.game import GameCreate, GameResponse

from services.keywords import get_or_create_keyword

import requests
import os

from pathlib import Path

ASSETS_DIR = "/home/edusilva/gamelib/assets"


def get_games(db: Session):
    games = get_all_games(db)

    return [
        game_to_response(game)
        for game in games
    ]


def get_game(game_id, db: Session):
    game = get_game_repository(game_id, db)

    return game_to_response(game)


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

        download_game_image(new_game.id, game.image_url)

        db.commit()
        db.refresh(new_game)

        return game_to_response(new_game)

    except Exception:
        db.rollback()
        raise


def download_game_image(game_id: str, game_url: str):
    directory = Path(ASSETS_DIR) / "images" / "games" / game_id
    filename = directory / "cover.jpg"

    directory.mkdir(parents=True, exist_ok=True)

    response = requests.get(game_url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)



def game_to_response(game):
    return GameResponse(
        id=game.id,
        name=game.name,
        publisher=game.publisher,
        developer=game.developer,
        cover_url=f"/assets/images/games/{game.id}/cover.jpg",
        keywords=[keyword.name for keyword in game.keywords],
        release_date=game.release_date,
        avg_time=game.avg_time,
        platforms=game.platforms,
        created_at=game.created_at,
        updated_at=game.updated_at,
        deleted_at=game.deleted_at,
    )


def delete_game(game_id: str, db: Session):
    try:
        deleted = delete_game_repository(game_id, db)

        if deleted == 0:
            raise HTTPException(
                status_code=404,
                detail="Game not found"
            )

        db.commit()

        return {"message": "Game deleted successfully"}

    except Exception:
        db.rollback()
        raise