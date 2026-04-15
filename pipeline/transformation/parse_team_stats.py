
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



# Normalisation des nom de colonnes (renommage des categories): 
COLUMN_RENAMES = {
    "netPassingYards": "passingYards",
    "totalYards": "yardsTotal", 
    "rushingYards": "yardsRushing", 
    "rushingAttempts": "attemptsRushing",
    "completionAttempts": "passingCompAtt", 
    "thirdDownEff": "thirdDown", 
    "fourthDownEff": "fourthDown"
}

# Classification offense / defense / special teams 

OFFENSE_CATEGORIES = {
    "passingYards", "yardsRushing", "yardsTotal", "passingCompAtt", "attemptsRushing", "yardsPerPass", "yardsPerRushAttempt", "firstDowns"
}

DEFENSE_CATEGORIES = {
    "interceptions", "passesIntercepted", "fumblesRecovered", "fumblesLost", "turnovers", "interceptionYards", "interceptionTDs"
}

SPECIAL_TEAMS_CATEGORIES = {
    "kickReturns", "kickReturnYards", "kickReturnTDs", "puntReturns", "puntReturnsYards", "puntReturnTDs", "kickingPoints"
}


# création de notre fonction utlitaire pour l'intégration dans mon  parseparse_team_stats
def normalize_values(value): 
    if value is None: 
        return None 
    # 1) Entier naturel 
    if value.isdigit(): 
        return int(value)

    # 2) float
    try: 
        return float(value)
    except: 
        pass
    # ratio "7-12"
    if "-"in value and value.replace("-", "").isdigit():
        num, den = value.split("-")
        return {"made": int(num), "attempts": int(den)}
    # Durée "29:44"
    if ":" in value and value.replace(":", "").isdigit(): 
        minutes, seconds = value.split(":")
        return int(minutes) * 60 + int(seconds)
    return value


def parse_team_stats(raws_stats): 
    """ 
     Transforme les stats d'équipe brutes en une table propre.
     chaque entrée brute devient une ligne avec colonnes normalisées
    """

    parsed = []
    for entry in raws_stats:
        game_id = entry.get("id")

        # Chaque match contient 2 équipes 
        for team_entry in entry.get("teams", []): 
            base = {
                    "gameId": game_id, 
                    "teamId": team_entry.get("teamId"), 
                    "team": team_entry.get("team"),
                    "conference": team_entry.get("conference"), 
                    "homeAway": team_entry.get("homeAway"),
                    "points": team_entry.get("points"), 
                    "unit": None
               }
        # On initialise l'unit par défaut
            # base["unit"] = None

        # Aplatir la liste des stats: 
            for stat in team_entry.get("stats", []):
                category = stat.get("category") 
                value = stat.get("stat")
       
                  # Renommage
                if category in COLUMN_RENAMES:
                   category = COLUMN_RENAMES[category]

                  # Normalisation
                value = normalize_values(value)
        # Renommage propres des catégories
                if category in OFFENSE_CATEGORIES:
                     base["unit"] = "offense"
                elif category in DEFENSE_CATEGORIES: 
                     base["unit"] = "defense"
                elif category in SPECIAL_TEAMS_CATEGORIES:
                     base["unit"] = "special"   

                base[category] = value     

        
        # Colonne dérivées 
        # Third down %   
            td = base.get("thirdDown")
            if isinstance(td, dict) and td.get("attempts", 0) > 0:
               base["thirdDowmnPct"] = td["made"] / td["attempts"]

        # fourth down % 
            fd = base.get("fourthDown")
            if isinstance(fd, dict) and fd.get("attempts", 0) >0:
               base["fourthDownPct"] = fd["made"] / fd["attempts"]

        # Passing completion % 
            pc = base.get("passingCompAtt")
            if isinstance(pc, dict) and pc.get("attempts", 0) >0: 
               base["passingPct"] = pc["made"] / pc["attempts"]
        
        # Yards per play
            plays = 0
            if isinstance(pc, dict):
                plays = plays  + pc.get("attempts", 0)
            plays =  plays + base.get("attemptsRushing", 0)
            
            if plays > 0 and base.get("yardsTotal") is not None: 
                base["yardsPerPlay"] = base["yardsTotal"] / plays
  

            parsed.append(base)
    return parsed





# if category in COLUMN_RENAMES:
#     category = COLUMN_RENAMES[category]
 # test manuel 

if __name__ == "__main__": 
       from pipeline.scrapers.games_stats import fecth_all_game_team_stat
       raw = fecth_all_game_team_stat(2023)
       parsed = parse_team_stats(raw)
       print(f"Entrées brutes : {len(raw)}")
       print(f"Entrées transformées: {len(parsed)}")
       print(parsed[:2])

#     #    print("Exemple brut :")
#        print(raw[0].keys())
