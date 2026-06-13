import sys 
from pathlib import Path
import json 
import datetime
import pandas as pd 
import os 
# Ajout de mon dossier dans sys.path
root_project = Path(__file__).resolve().parents[3]
sys.path.append(str(root_project))

from pipeline.analytics.context.momentum import compute_streaks, compute_recent_margin, normalize_column_features, compute_momentum_score, compute_momentum_differential
from pipeline.analytics.context.schedule_difficulty import compute_schedule_difficulty, compute_schedule_difficulty_rolling
from pipeline.analytics.context.recent_offense_defense import compute_recent_offense_defense
from pipeline.analytics.context.injuries_proxies import compute_injuries_proxies
from pipeline.transformation.parse_games import parse_games
from pipeline.scrapers.games import fetch_games
from pipeline.transformation.parse_weathers import parse_weathers
from pipeline.scrapers.weather import fetch_weather
from pipeline.analytics.context.weather_impact import compute_weather_features 

def load_raw_team_matchup(path: str = "data/raw/team_matchup_sample.json")-> list: 

    with open(path, "r" , encoding ="utf-8") as f : 
        data = json.load(f)
    return data

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
            "point_diff": winner_points - loser_points, 
        })
    return cleaned

def structure_team_matchup(cleaned_data: list)->list:
    # transforme les données nettotyées en un format structuré: 
    # Une ligne par équipe et par match 
    # Ajoute team, opponent, result, points_for, points_against

    structured = []
    for entry in cleaned_data:
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



def compute_conference_strength(structure_df: pd.DataFrame)->pd.DataFrame: 
    # Calcule de la force de chaque conférence en utilisant Opponent STrength 
    conference_strength = structure_df.groupby("team_conference").agg({
        "opponent_win_rate": "mean", 
        "opponent_avg_margin": "mean"
    }).reset_index()
    conference_strength = conference_strength.rename(columns = {
        "team_conference": "conference",
        "opponent_win_rate": "conference_avg_opponent_win_rate", 
        "opponent_avg_margin": "conference_avg_opponent_margin"
    })
    return conference_strength


def add_conference_strength(structure_df: pd.DataFrame, conference_strength_df: pd.DataFrame)->pd.DataFrame: 
    # Ajoute la force de la conférence de l'équipe Et de la conférence de l'adversaire.

    # Force de la conférence de l'équipe 
    merged = structure_df.merge(
        conference_strength_df, 
        left_on = "team_conference", 
        right_on = "conference", 
        how = "left"
    ).drop(columns = ["conference"])

    merged = merged.rename(columns = {
    "conference_avg_opponent_win_rate":"team_conference_strength_win_rate", 
    "conference_avg_opponent_margin": "team_conference_strength_margin"
    })

    # Force de la conference de l'adversaire 
    merged = merged.merge(
       conference_strength_df, 
       left_on = "opponent_conference", 
       right_on = "conference", 
       how = "left"
    ).drop(columns = ["conference"])
    
    merged = merged.rename(columns = {
        "conference_avg_opponent_win_rate": "opponent_conference_strength_win_rate", 
        "conference_avg_opponent_margin": "opponent_conference_strength_margin"
    })
 
    return merged

valgames = fetch_games(all)
vallgames = parse_games(valgames)
games_df = pd.DataFrame(vallgames)

valweather = fetch_weather(all)
vallweather = parse_weathers(valweather)
weathers_df = pd.DataFrame(vallweather)
   
def merge_team_matchup_with_games(structure_df: pd.DataFrame, games_df: pd.DataFrame)->pd.DataFrame: 

    merge1 = structure_df.merge(
        games_df[["season", "week", "home_team", "away_team", "game_id"]], 
        left_on = ["season", "week", "team", "opponent"], 
        right_on = ["season", "week", "home_team", "away_team"], 
        how = "left"
    )
    
    merge2 = structure_df.merge(
        games_df[["season", "week", "home_team", "away_team", "game_id"]], 
        left_on = ["season", "week", "team", "opponent"], 
        right_on = ["season", "week", "away_team", "home_team"], 
        how = "left"
    )
    
    df_games_merged = merge1.combine_first(merge2)
    df_games_merged["game_id"] = df_games_merged["game_id"].astype("Int64")
    # to regive good value to my is_home, is_away, is_neutral values 
    df_games_merged["is_home"] = (df_games_merged["team"] == df_games_merged["home_team"]).astype(int)
    df_games_merged["is_away"] = (df_games_merged["team"] == df_games_merged["away_team"]).astype(int)
    df_games_merged["is_neutral"] = (df_games_merged["home_team"] == 0) & (df_games_merged["away_team"] == 0).astype(int)

    df_games_merged["location"] = df_games_merged.apply(
        lambda row : "home" if row["is_home"] == 1
        else "away" if row["is_away"] == 1
        else "neutral", 
        axis = 1
    )

    return df_games_merged


def merge_team_matchup_with_weather(structure_df: pd.DataFrame, weathers_df: pd.DataFrame)->pd.DataFrame: 
    mergeweather = structure_df.merge(
        weathers_df[["game_id","temperature", "humidity", "precipitation", "wind_speed", "wind_direction", "pressure", "condition"]], 
        left_on = ["game_id"], 
        right_on = ["game_id"], 
        how = "left"
    )
    return mergeweather


raw = load_raw_team_matchup()
clean = clean_team_matchup(raw)
structured = structure_team_matchup(clean)
stats = compute_team_matchup_stats(structured)
with_opponent = add_opponent_strength(pd.DataFrame(structured), stats)
conf_strength = compute_conference_strength(with_opponent)
final = add_conference_strength(with_opponent, conf_strength)
finalcs = compute_streaks(final)
finalcrm = compute_recent_margin(finalcs)
finalncf = normalize_column_features(finalcrm)
finalcms = compute_momentum_score(finalncf)
finalcmd = compute_momentum_differential(finalcms)
finalcsd = compute_schedule_difficulty(finalcmd)
finalcsdr = compute_schedule_difficulty_rolling(finalcsd)
finalcrod = compute_recent_offense_defense(finalcsdr)
finalcip = compute_injuries_proxies(finalcrod)
finalmtmwg = merge_team_matchup_with_games(finalcip, games_df)
finalmtmww = merge_team_matchup_with_weather(finalmtmwg, weathers_df)
print(compute_weather_features(finalmtmww))
# finalmega = merge_games(finalcip, vallgames_df)

# print(compute_injuries_proxies(finalcrod))
print(list(finalcsd.columns))


def  build_team_matchup_dataset(raw_path:str , output_path: str)-> pd.DataFrame:
    # pipeline complet:
    # - Charge les données 
    # - nettoie
    # - structure
    # - calcule les stats 
    # - sauvegarde le dataset final 

    # 1. Charger les données brutes 
    raw_data = load_raw_team_matchup(raw_path)

    # 2.Nettoyer
    cleaned = clean_team_matchup(raw_data)

    # 3.Structurer
    structured = structure_team_matchup(cleaned)

    # 4. Convertir en dataFrame 
    structured_df = pd.DataFrame(structured)

    # 5. calculer les stats 
    stats = compute_team_matchup_stats(structured)

    # 6 opponent Strength
    structured = add_opponent_strength(structured_df , stats) 

    # 7 conference_strength
    conference_strength = compute_conference_strength(structured)
    structure_df = add_conference_strength(structured, conference_strength)
    # 8 Sauvegarder dans data /final

    os.makedirs(os.path.dirname(output_path), exist_ok = True)
    stats.to_csv(output_path, index = False)

    return stats

# tester chacune de mes fonctions 

