from fastapi import FastAPI

from models import Game, Keyword
from routers.games import router as games_router

app = FastAPI()

app.include_router(games_router)