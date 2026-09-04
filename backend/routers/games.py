from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.game import GameResponse, GameCreate
from services.games import get_games, get_game
from services.games import create_game as create_game_service
from services.games import delete_game as delete_game_service


router = APIRouter(prefix="/games")


@router.get("", response_model=List[GameResponse])
def games(db: Session = Depends(get_db)):
    return get_games(db)

@router.get("/{game_id}", response_model=GameResponse)
def games(game_id, db: Session = Depends(get_db)):
    return get_game(game_id, db)

@router.post("", response_model=GameResponse)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    return create_game_service(db, game)

@router.delete("")
def delete_game(game_id: str, db: Session = Depends(get_db)):
    return delete_game_service(game_id, db)