class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality_and_season(self, nationality, season):
        players = self.reader.get_players(nationality)
        
        sorted_players = sorted(players, key=lambda player: player.points(), reverse=True)
        
        return sorted_players


