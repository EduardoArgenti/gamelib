from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.game import GameResponse
from services.games import get_games


router = APIRouter(prefix="/games")


@router.get("", response_model=List[GameResponse])
def games(db: Session = Depends(get_db)):
    return get_games(db)