import requests
from player import Player

class PlayerReader:
    def __init__(self, season):
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"  

    def get_players(self, nationality):
    
        response = requests.get(self.url).json()
        players = []
        
        for dict in response:
            if dict.get('nationality') == nationality: 
                player = Player(dict)
                players.append(player)
        
        return players
