import sys 
import os 
# add project_root to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from cfbd_client import get_calendar, get_game_player_stats

def fetch_all_game_player_stats(year): 
    # retrieve player's stat for one seans
    # 1, retrieving available weeks 
    calendar = get_calendar(year)
    if not  calendar:
        print("Impossible de récupérer le calendrier")
        return []
    
    # 2 _ Extraction week's number 

    weeks = sorted({entry["week"] for entry in calendar if "week" in entry})
    all_stars = []

    # 3 loop on each weeks 

    for week in weeks: 
        print(f"Récupération des stats de joueurs pour la semaine {week} ...")
        week_starts = get_game_player_stats(year, week)
        if week_starts:
           all_stars.extend(week_starts)
    return all_stars

if __name__ == "__main__":
    stats = fetch_all_game_player_stats(2023)
    print(f"Nombre total d'entrées récupérées : {len(stats)}")
    print(stats[0])
        

