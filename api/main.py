from typing import List

from fastapi import FastAPI

from .optimization import Player, Fireteam, find_fireteams


app = FastAPI()


@app.post("/", response_model=List[Fireteam])
def matchmake(players: List[Player]):
    solution = find_fireteams(players)
    return solution.fireteams
