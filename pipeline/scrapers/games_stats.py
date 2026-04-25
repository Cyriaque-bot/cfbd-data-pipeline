import sys
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


# from cfbd_client import get_calendar, get_game_team_stats
from pipeline.loaders.load_games_stats import load_games_stat
from pipeline.loaders.load_calendar import load_calendar
def fecth_all_game_team_stat(year): 
    """récupère toutes les stats d'équipe pour une saison complète """
    # Récupérer les semaines disponibles 
    calendar = load_calendar(year)
    if not calendar: 
        print("Impossible de récuperer le calendrier")
        return []
    
    # Extraire les numéros de semaine
    weeks = sorted({entry["week"] for entry in calendar if "week" in entry})
    All_stats = []

    #2) Boucler sur chaque semaines 
    for week in weeks: 
        print(f"Récupération des stats pour la semaine {week} ...")
        week_stats = load_games_stat(year, week)
        if week_stats:
            All_stats.extend(week_stats)
    return All_stats


# test manuel 
# if __name__ == "__main__": 
# stats = fecth_all_game_team_stat(2023)
#rint(fecth_all_game_team_stat(2023))
#     print(f"Nombre total d'entrée récupérées: {len(stats)}")
#     print(stats[:1])