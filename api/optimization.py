from itertools import chain
from random import shuffle, sample
from typing import List
from math import sqrt

from pydantic import BaseModel


class Player(BaseModel):
    id: str
    elo: int


class Fireteam(BaseModel):
    players: List[Player]

    def __getitem__(self, idx):
        return self.players[idx]

    @property
    def elo_mean(self):
        return sum([player.elo for player in self.players]) / len(self.players)

    @property
    def elo_var(self):
        mean = self.elo_mean
        return sum([(player.elo - mean) ** 2 for player in self.players]) / len(self.players)

    @property
    def elo_dev(self):
        return sqrt(self.elo_var)

    def mix(self, fireteam):
        all_players = self.players + fireteam.players
        shuffle(all_players)
        return Fireteam(all_players[:team_size])


class Solution:
    def __init__(self, players, team_size):
        self.team_size = team_size
        self.fireteams = [Fireteam(players=players[i:i + team_size]) for i in range(0, len(players), team_size)]

    def __getitem__(self, idx):
        return self.fireteams[idx]

    def __repr__(self):
        return str(self.fireteams)

    def mutate(self, n=1):
        all_players = list(chain(*[fireteam.players for fireteam in self.fireteams]))

        for _ in range(n):
            i, j = sample(list(range(len(all_players))), k=2)
            all_players[i], all_players[j] = all_players[j], all_players[i]

        return Solution(all_players, self.team_size)

    @property
    def elo_mean(self):
        return sum([fireteam.elo_mean for fireteam in self.fireteams]) / len(self.fireteams)

    @property
    def elo_var(self):
        elo_mean = self.elo_mean
        return sum([(fireteam.elo_mean - elo_mean) ** 2 for fireteam in self.fireteams]) / len(self.fireteams)

    @property
    def elo_dev(self):
        return sqrt(self.elo_var)

    @property
    def rank(self):
        return self.elo_dev


def find_fireteams(players: List[Player], team_size: int = 3, n_pop: int = 10, n_iter: int = 100, n_max_mutations: int = 2):
    solutions = [Solution(sample(players, k=len(players)), team_size) for _ in range(n_pop)]

    for _ in range(n_iter):
        solutions = list(chain(*[[solution.mutate(n=n_max_mutations) for solution in solutions] for _ in range(n_pop)]))
        solutions.sort(key=lambda sol: sol.rank)
        solutions = solutions[:n_pop]

    return solutions[0]
