from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.game import GameResponse, GameCreate
from services.games import get_games
from services.games import create_game as create_game_service


router = APIRouter(prefix="/games")


@router.get("", response_model=List[GameResponse])
def games(db: Session = Depends(get_db)):
    return get_games(db)

@router.post("", response_model=GameResponse)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    return create_game_service(db, game)