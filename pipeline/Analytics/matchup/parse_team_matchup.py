import sys 
import os 
import datetime
import pandas as pd


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)





# from pipeline.scrapers.teams_matchups import fetch_load_team
############ For BI ############

def parse_team_matchup_bi(rawteammactup): 
    valistreammactup = []
    for i in rawteammactup: 
        daldictteammatchup = {
            "season": i["season"], 
            "week": i["week"], 
            "season_type": i["season_type"], 
            "date": i["date"], 
            "winner": i["winner"], 
            "loser": i["loser"], 
            "winner_points": i["winner_points"], 
            "loser_points": i["loser_points"]
        }
        valistreammactup.append(daldictteammatchup)
    
    return valistreammactup

########## End just for the BI ##############


def normalize_team_name(name: str)->str: 
    # normalise le nom d'équipe strip espace, title case, retire les variation inutiles 
    if not isinstance(name, str): 
        return None 
    name = name.strip().title()

    # Exemple de normalisation simple(nous pourrons toujours enrichir plus tard)
    replacements = {
        "St.": "State", 
        "Univ.": "University"
    }
    for old, new in replacements.items():
        name = name.replace(old, new)

    return name


def parse_date(date_str: str):
    # convertit une date brute en objet datetime.date, si la date est invalide retoune None
    if not isinstance(date_str,  str): 
       return None
    
    try:
        # Format CFDB typique : "2023-09-09T19:00:00.000Z"
        return datetime.datetime.fromisoformat(date_str.replace("Z", "")).date()
    except Exception: 
        return None 


def clean_team_matchup(raw_data: list)-> list: 
    # Nettoie les données brutes du Json team_matchup
    # retourne une liste de dictionnaire nettoyés

    cleaned = []
    for entry in raw_data:
        #vérification minimal
        if "winner" not in entry or "loser" not in entry: 
            continue
        # 1 Normalisation des noms

        winner = normalize_team_name(entry.get("winner"))
        loser = normalize_team_name(entry.get("loser"))
        

        # 2 Conversion numérique sécurisée
        try: 
            week = int(entry.get("week", 0))
        except: 
            week = None
       
        try:
            winner_points = int(entry.get("winner_points", 0))
            loser_points = int(entry.get("loser_points", 0))
            # cyriaque = int(entry.get("cyriaque_est_un_genie", 0))
        except: 
            continue # si les scores sont invalides -> on skip
        
        # 3. Conversion date
        date = parse_date(entry.get("date"))

        # 4. Nettoyage du type de saison 
        season_type = entry.get("season_type", "").lower().strip()


        # 5. Construction de l'entrée nettoyée 
        cleaned.append({
            "season": entry.get("season"), 
            "winner_conference": entry.get("winner_conference"), 
            "loser_conference": entry.get("loser_conference"), 
            "neutral_site": entry.get("neutral_site"), 
            "week": week, 
            "season_type": season_type, 
            "date": date,
            "winner": winner, 
            "loser": loser, 
            "winner_points": winner_points, 
            "loser_points": loser_points, 
            "point_diff": winner_points - loser_points
            # "cyriaque": cyriaque
        })
    return cleaned


def structure_team_matchup(raw_team_matchup): 

    # transforme les données nettotyées en un format structuré: 
    # Une ligne par équipe et par match 
    # Ajoute team, opponent, result, points_for, points_against
    

    structured = []
    for entry in raw_team_matchup:
        season = entry["season"]
        week = entry["week"]
        date = entry["date"]
        season_type = entry["season_type"]

        winner = entry["winner"]
        loser = entry["loser"]
        wp = entry["winner_points"]
        lp = entry["loser_points"]

        # Conference Extraites du Json
        winner_conf = entry["winner_conference"]
        loser_conf = entry["loser_conference"]

        # cyriaque = entry["cyriaque"]

        # --- Ligne pour le gagnant --- #
        structured.append({ 
              "season" : season,
              "week" : week, 
              "season_type": season_type, 
              "date": date, 
              "team": winner, 
              "team_conference": winner_conf, 
              "opponent": loser, 
              "opponent_conference": loser_conf,
              "result": "W",
              "points_for": wp, 
              "points_against": lp, 
              "point_diff": wp - lp, 
              "is_home": None, 
              "is_away": None, 
              "is_neutral": None
            #   "cyriaque": cyriaque
        })
        # --- Ligne pour le perdant  --- #

        structured.append({ 
              "season" : season,
              "week" : week, 
              "season_type": season_type, 
              "date": date, 
              "team": loser, 
              "team_conference": loser_conf, 
              "opponent": winner, 
              "opponent_conference": winner_conf,
              "result": "L",
              "points_for": lp, 
              "points_against": wp, 
              "point_diff": lp - wp, 
              "is_home": None, 
              "is_away": None, 
              "is_neutral": None
            #   "cyriaque": cyriaque
        })

    
    return structured

def compute_team_matchup_stats(structured_data: list)->pd.DataFrame:
    # Calcule les statistiques de matchup pour chaque équipe 
    # Retourne un DataFrame
    # total_games
    # wins
    # losses
    # points_for
    # points_against
    # avg_points_for
    # avg_points_against
    # avg_margin

    # Convertir la liste en DataFrame
    df = pd.DataFrame(structured_data)

    # sécurit minimale 
    if df.empty: 
        return pd.DataFrame()
    
    # Groupement par équipe 

    grouped = df.groupby("team")

    # Calcul des stats globales 
    stats = pd.DataFrame({
        "total_games": grouped.size(), 
        "wins": grouped.apply(lambda x:(x["result"] == "W").sum()), 
        "losses": grouped.apply(lambda x:(x["result"] == "L").sum()), 
        "points_for": grouped["points_for"].sum(),
        "points_against": grouped["points_against"].sum(), 
        "avg_points_for": grouped["points_for"].mean(),
        "avg_points_against": grouped["points_against"].mean(),
        "avg_margin": grouped["point_diff"].mean()
    })

    # Win rate 
    stats["win_rate"] = stats["wins"] / stats["total_games"]

    stats = stats.reset_index()

    return stats


def add_opponent_strength(structured_df: pd.DataFrame, stats: pd.DataFrame)-> pd.DataFrame:
    # Ajouter les statistique de l'adversaire(opponent strength) à chaque ligne du datasetstructuré.
    # Opponent_win_rate
    # Opponent_avg_margin
    # Opponent_points_against


    # Renommer la colonne 'team' dans stats_df pour éviter les collisions
    opponent_stats = stats.rename(columns = {
        "team": "opponent", 
        "win_rate": "opponent_win_rate", 
        "avg_margin": "opponent_avg_margin", 
        "points_for": "opponent_points_for",
        "points_against": "opponent_points_against",
        "avg_points_for": "opponent_avg_points_for", 
        "avg_points_against": "opponent_avg_points_against"
    })

    # Fusion: ajoute les stats de l'adversaire à chaque ligne
    merged = structured_df.merge(
          opponent_stats, 
          on = "opponent", 
          how = "left"
    )

    return merged



def parse_team_matchup(df_team_raw: list)->pd.DataFrame: 
    # chargement des données 

    # Nettoyage
    clean = clean_team_matchup(df_team_raw)
    # Structurer
    structured = structure_team_matchup(clean)
    structured_df = pd.DataFrame(structured)
    # Global statistique
    stats_df = compute_team_matchup_stats(structured)
    # opponent strength
    finaldf = add_opponent_strength(structured_df, stats_df)
    
    return finaldf


# from pipeline.loaders.load_team_matchup import team_matchups
# from pipeline.scrapers.teams_matchups import fetch_load_team

# valrawfet = fetch_load_team()
# valrawfetparse = parse_team_matchup(valrawfet)
# print(type(parse_team_matchup(valrawfet)))

