from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)
    
    def sorted_by_points(self, player):
        return player.points

    def sorted_by_goals(self, player):
        return player.goals

    def sorted_by_assists(self, player):
        return player.assists
    
    def top(self, how_many, sort_by=SortBy.POINTS):
        if sort_by == SortBy.POINTS:
            order = self.sorted_by_points
        if sort_by == SortBy.GOALS:
            order = self.sorted_by_goals
        if sort_by == SortBy.ASSISTS:
            order = self.sorted_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=order
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
