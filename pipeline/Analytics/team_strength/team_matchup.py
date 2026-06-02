import json 
import datetime
import pandas as pd 
import os 



def load_raw_team_matchup(path: str = "data/raw/team_matchup_sample.json")-> list: 

    with open(path, "r" , encoding ="utf-8") as f : 
        data = json.load(f)
    return data


# if __name__ == "__main__":
#     raw = load_raw_team_matchup()
#     print(raw[0])

def normalize_team_name(name: str)->str: 
    # normalise le nom d'équpe strip espace, title case, retire les variation inutiles 
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
            week = int(entry.get("winner", 0))
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
            "week": week, 
            "season_type": season_type, 
            "date": date,
            "winner": winner, 
            "loser": loser, 
            "winner_points": winner_points, 
            "loser_points": loser_points, 
            "point_diff": winner_points - loser_points
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
        date = entry["Date"]
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
              "location": "neutral" if entry ["neutral_site"] else "away", 
              "is_home": 0, 
              "is_away": 1 if not entry["neutral_site"] else 0, 
              "is_neutral": 1 if entry["neutral_site"] else 0
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
              "location": "neutral" if entry["neutral_site"] else "away", 
              "is_home": 0, 
              "is_away": 1 if not entry["neutral_site"] else 0, 
              "is_neutral": 1 if entry["neutral_site"] else 0
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

    # remet "team" comme colonne
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
        "avg_points_against": "apponent_avg_points_against"
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
       how = "left", 
       suffixes = ("", "_opp_conf")
    ).drop(columns = ["conference"])
    
    merged = merged.rename(columns = {
        "conference_avg_opponent_win_rate_opp_conf": "opponent_conference_strength_win_rate", 
        "conference_avg_opponent_margin_opp_conf": "opponent_conference_strength_margin"
    })
 
    return merged


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