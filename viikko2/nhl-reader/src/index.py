from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    # Ask for nationality and season
    nationality = input("Enter the nationality (e.g., FIN): ").strip()
    season = input("Enter the season (e.g., 2023-24): ").strip()

    # Initialize PlayerReader with the selected season
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    
    # Get the top scorers based on nationality and season
    players = stats.top_scorers_by_nationality_and_season(nationality, season)

    # Create a rich table for formatted output
    console = Console()
    table = Table(title=f"Top Scorers from {nationality} in {season} Season")
    
    table.add_column("Name", justify="left")
    table.add_column("Team", justify="center")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")
    
    # Add rows to the table for each player
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points()))
    
    # Print the table to the console
    console.print(table)

if __name__ == "__main__":
    main()


