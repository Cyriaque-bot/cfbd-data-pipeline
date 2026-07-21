import sys 
from pathlib import Path
import pandas as pd 
import numpy as np 

# Ajout de mon dossier dans sys.path
root_project = Path(__file__).resolve().parents[3]
sys.path.append(str(root_project))


def merge_team_matchup_with_games(df_matchup, df_games, df_team_stats)->pd.DataFrame: 
    
    # Normaliser les noms d'équipe dans df_matchup
    df_matchup["team_norm"] = df_matchup["team"].str.lower().str.replace(" ","")
    df_matchup["opponent_norm"] = df_matchup["opponent"].str.lower().str.replace(" ","")

    # normaliser les noms d'équipe pour matcher CFDB
    df_games["home_team_norm"] = df_games["home_team"].str.lower().str.replace(" ", "")
    df_games["away_team_norm"] = df_games["away_team"].str.lower().str.replace(" ", "")

       # Normalisation des types 
    df_matchup["season"] = df_matchup["season"].astype(int)
    df_matchup["week"] = df_matchup["week"].astype(int)

    df_games["season"] = df_games["season"].astype(int)
    df_games["week"] = df_games["week"].astype(int)


 
   
    # merge team + opponent + season + week

    merged = df_matchup.merge(
        df_games[[
                   "game_id", "season", "week", "season_type", "date",
                   "home_team_norm", "away_team_norm", 
                   "home_team", "away_team",
                   "home_points", "away_points",
                   "venue", "neutral_site"
                  ]], 
        left_on = ["team_norm", "opponent_norm", "season", "week"],
        right_on = ["home_team_norm", "away_team_norm", "season", "week"], 
        how = "left"
    )
  
    # Ajout de ma team_id 

    df_team_stats["team_norm"] =  df_team_stats["team"].str.lower().str.replace(" ", "")
    merged = merged.merge(
        df_team_stats[["team_norm", "team_id"]], 
        on = "team_norm", 
        how = "left"
    )
    
    # Ajouter opponent_id 
    merged = merged.merge(
        df_team_stats[["team_norm", "team_id"]].rename(columns = {"team_norm":"opponent_norm", "team_id": "opponent_id"}),
        on = "opponent_norm", 
        how = "left"
    )
    
    # Nettoyage 

    merged = merged.drop(columns = ["team_norm", "opponent_norm", "home_team_norm", "away_team_norm"], errors = "ignore")


    return merged


    


# la météo

def merge_team_matchup_with_weather(df, df_weather, df_team_stats): 
    
    # Normaliser les noms d'équipes pour matcher df_team_stats
    df_weather["home_team_norm"] = df_weather["home_team"].str.lower().str.replace(" ", "")
    df_weather["away_team_norm"] = df_weather["away_team"].str.lower().str.replace(" ", "")
  
    df_team_stats["team_norm"] = df_team_stats["team"].str.lower().str.replace(" ", "")
    # Associer la météo à l'équipe (team) via home_team / away_team
    # cas 1 : l'équipe est home_team
    weather_home = df_weather.rename(columns = {"home_team_norm": "team_norm"})
    weather_home = weather_home.drop(columns = ["away_team_norm"])

    # cas 2 : l'équipe est away_team
    weather_away = df_weather.rename(columns = {"away_team_norm": "team_norm"})
    weather_away = weather_away.drop(columns = ["home_team_norm"])

    # On combine les deux 
    df_weather_team = pd.concat([weather_home, weather_away], ignore_index = True)


    # Ajouter team_id via df_team_stats
    df_weather_team = df_weather_team.merge(
        df_team_stats[["team_norm", "team_id"]], 
        on = "team_norm", 
        how ="left"
    )
    # df_weather_team = df_weather_team.drop(columns = ["team"])
    # Merge principal 
    merged = df.merge(
        df_weather_team.drop(columns = ["team_norm"]), 
        on = ["game_id", "team_id"], 
        how = "left"
    )
    return merged
    ##### Assemble home et away #####

def assemble_home_away(df):
    # Reconstruction des colonnes game_id pour le merge 
    df["home_game_id"] = df["game_id"]
    df["away_game_id"] = df["game_id"]
    # separer home et away 

    home = df[df["is_home"] == 1].copy()
    away = df[df["is_away"] == 1].copy()
  

    # S'assurer que home_team / away_team existe avant le prefix 
    if "home_team" not in home.columns:
        home["home_team"] = home["team"]
    if "away_team" not in away.columns: 
        away["away_team"] = away["team"]
    # Renommer les colonnes 
    home = home.add_prefix("home_")
    away = away.add_prefix("away_")

    # print("=== COLONNES HOME ===")
    # print(home.columns.tolist())
    # print("=== COLONNES AWAY ===")
    # print(away.columns.tolist())
    # print(df.columns.tolist())

    # fusionner sur game_id

    final = home.merge(
        away, 
        left_on = "home_home_game_id", 
        right_on = "away_away_game_id", 
        how = "inner"
    )

       # Restaurer season et week
    final["season"] = final["home_season"]
    final["week"] = final["home_week"]
       # Restaurer team/opponent
    final["team"] = final["home_team"]
    final["opponent"] = final["away_team"]

       # Restaurer game_id
    final["game_id"] = final["home_game_id"]

    return final

def compute_all_differentials(df):
    # On recupère uniquement  les colonnes numériques 
    numeric_cols = df.select_dtypes(include = ["int64", "float64"]).columns

    # Ongarde uniquement les colonnes home_* et away_*
    home_cols = [c for c  in numeric_cols if c.startswith("home_")]
    away_cols = [c for c  in numeric_cols if c.startswith("away_")]
    
    # creation de mapping home -> away
    for home_col in home_cols: 
        base = home_col.replace("home_", "")
        away_col = f"away_{base}"
        
        if away_col in away_cols: 
            # differential automatique 
              df[f"diff_{base}"] = df[home_col]  - df[away_col]
    # print("=== DEBUG DIFFS ===")
    # print([c for c in df.columns if c.startswith("diff_")])
    return df 

def compute_matchup_score(df): 
    # Score final basé sur les différentiels les plus impotants 
    df["matchup_score"] = (
        0.25 * df.get("diff_momentum_weather_adj", 0) +
        0.20 * df.get("diff_pressure_index", 0) +
        0.20 * df.get("diff_schedule_difficulty_norm", 0) + 
        0.15 * df.get("diff_style_score", 0) + 
        0.10 * df.get("diff_weather_advantage", 0) + 
        0.10 * df.get("diff_rivalry_pressure", 0)
    )
    # row = df[df["game_id"] == 401520777.0].iloc[0]

    # print("=== DEBUG DIFF VALUES FOR ALABAMA–AUBURN ===")
    # for col in ["diff_momentum_weather_adj", "diff_pressure_index",
    #         "diff_schedule_difficulty_norm", "diff_style_score",
    #         "diff_weather_advantage", "diff_rivalry_pressure"]:
    #     print(col, "=", row[col])
    return df 

def compute_win_probability(df): 

    # Probabilité 
    df["win_probability_home"] = 1 / (1 + np.exp(-df["matchup_score"]))

    return df 

def team_matchup_final(df):
    # 1. Assemble Home/Away 
    df = assemble_home_away(df)
    # 2. Différentiel automaatique pour toutes les colonnes Home/Away
    df = compute_all_differentials(df)

    for col in df.columns: 
        if col.startswith("diff_"): 
            df[col] = df[col].fillna(0)
    # 3.Score Final 
    df = compute_matchup_score(df)
    # 4. Probabilité
    df = compute_win_probability(df)

    return df 
