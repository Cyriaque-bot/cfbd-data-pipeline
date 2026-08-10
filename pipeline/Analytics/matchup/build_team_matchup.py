import pandas as pd 
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


# import des modules du pipeline 

# parsing 
from pipeline.analytics.matchup.parse_team_matchup import parse_team_matchup
# Conference Strength
from pipeline.transformation.cfbd.parse_conference_matchup import parse_conference_strength
# team_stat 
from pipeline.transformation.cfbd.parse_team_game_stats import parse_team_game_stats
# parse_games
from pipeline.transformation.cfbd.parse_games import parse_games
# weather
from pipeline.transformation.cfbd.parse_weathers import parse_weathers
# rivalries 
from pipeline.transformation.cfbd.parse_rivalries import parse_rivalries
# rankings
from pipeline.transformation.cfbd.parse_rankings import parse_rankings
# prime_time 
from pipeline.transformation.cfbd.parse_prime_times import parse_prime_time

# Context Features
from pipeline.analytics.matchup.build_context_features import build_context_features
from pipeline.analytics.context.style_of_play import compute_style_of_play

# Team matchup (merge + assemble + différentiels + final)
from analytics.matchup.team_matchup import (
    merge_team_matchup_with_games, 
    merge_team_matchup_with_weather, 
    team_matchup_final
)

# Scrapers 
from pipeline.scrapers.cfbd.teams_matchups import fetch_load_team
from pipeline.scrapers.cfbd.team_game_stat import fetch_teams_stat
from pipeline.scrapers.cfbd.conferences import fetch_conference
from pipeline.scrapers.cfbd.games import fetch_games
from pipeline.scrapers.cfbd.weathers import fetch_weather
from pipeline.scrapers.cfbd.rivalries import fetch_rivalries
from pipeline.scrapers.cfbd.prime_times import fetch_prime_time
from pipeline.scrapers.cfbd.rankings import fetch_rankings

# teste 
from pipeline.analytics.matchup.team_matchup import  assemble_home_away

# pipeline global  build_team_matchup

def build_team_matchup(
                        df_team_raw : list,
                        df_games: pd.DataFrame,
                        df_weather: pd.DataFrame,
                        df_style: pd.DataFrame, 
                        df_team_stats: pd.DataFrame, 
                        df_rivalries: pd.DataFrame, 
                        df_prime_games: pd.DataFrame, 
                        df_rankings: pd.DataFrame, 
                        df_conf_strength: pd.DataFrame
                        )-> pd.DataFrame:
    # final dataset
    # Parsing de mon team_matchup brut 
    df = parse_team_matchup(df_team_raw)

    # ajout de la force des conférences 
    df = parse_conference_strength(df)

    # ajout des informations de games (game_id, home/ away)
    df = merge_team_matchup_with_games(df, df_games, df_team_stats)

    # ajout des donnée météos brutes
    df = merge_team_matchup_with_weather(df, df_weather, df_team_stats)

    
    # Normalisation season
    if "season_x" in df.columns:
        df["season"] = df["season_x"]
    elif "season_y" in df.columns:
        df["season"] = df["season_y"]
    elif "season" in df.columns:
        df["season"] = df["season"]
    else:
        raise ValueError("Aucune colonne season trouvée après merge games.")

    # Normalisation week
    if "week_x" in df.columns:
        df["week"] = df["week_x"]
    elif "week_y" in df.columns:
        df["week"] = df["week_y"]
    elif "week" in df.columns:
        df["week"] = df["week"]
    else:
        raise ValueError("Aucune colonne week trouvée après merge games.")

    # normalisation de la colonne date avant build_context_features 

    if "date" in df.columns: 
        df["date"] = pd.to_datetime(df["date"])
    elif "date_x" in df.columns: 
        df["date"] =  pd.to_datetime(df["date_x"])
    elif "date_y" in df.columns: 
        df["date"] =  pd.to_datetime(df["date_y"])
    elif "start_date_x" in df.columns: 
        df["date"] =  pd.to_datetime(df["start_date_x"])
    elif "start_date_y" in df.columns: 
        df["date"] =  pd.to_datetime(df["start_date_y"])
    else: 
        raise ValueError("Aucune colonne date trouvée pour compute_psychological_shock")
    
    


    # ajout des features contextuelles (momentum, pressure, weather_impact, etc)
    df = build_context_features(
         df,   
         df_weather, 
         df_style, 
         df_team_stats, 
         df_rivalries, 
         df_prime_games, 
         df_rankings, 
         df_conf_strength
         )

    # normalisation des colonnes home/away avant team_matchup final

    df["home_team"] = df.get(["home_team"], df.get("home_team_x", None))
    df["away_team"] = df.get(["away_team"], df.get("away_team_x", None))

# Nettoyage des colonnes parasites 
    df = df.drop(columns = ["home_team_x", "home_team_y", "away_team_x", "away_team_y"], errors = "ignore")


# Reconstruction is_home/ is_away / is_neutral
  
    df["is_home"] = (df["team"] == df["home_team"]).astype(int)
    df["is_away"] = (df["team"] == df["away_team"]).astype(int)

 # Reconstruction home/away pour les lignes inversées
    mask_inverse = (df["is_home"] == 0) & (df["is_away"] == 0)

    df.loc[mask_inverse, "home_team"] = df.loc[mask_inverse, "opponent"]
    df.loc[mask_inverse, "away_team"] = df.loc[mask_inverse, "team"]

    # Recalcul final
    df["is_home"] = (df["team"] == df["home_team"]).astype(int)
    df["is_away"] = (df["team"] == df["away_team"]).astype(int)

# Gestion des matchs neutres avec possibilité de (neutral_site potentiellement suffixé)
    neutral_col = None 
    for col in ["neutral_site", "neutral_site_x", "neutral_site_y"]: 
        if col in df.columns: 
            neutral_col = col 
            break 
    if neutral_col: 
        df["is_neutral"] = df[neutral_col].fillna(0).astype(int)
    else: 
        df["is_neutral"] = 0


# Ajout de la ligne inversées
    df["game_id"] = df.groupby(["season", "week"])["game_id"].transform("max")

    # Assemblage final home/away + différentels + score provisoire
    df = team_matchup_final(df)

    # Nettoyage final des colonnes parasites 

    df = df.drop(
        columns = [col for col in df.columns if col.endswith("_x") or col.endswith("_y")], errors = "ignore"
    )

    return df




vall = fetch_load_team()
df_team_raw = vall 


df_games = pd.DataFrame(parse_games(fetch_games(all)))
df_weather = pd.DataFrame(parse_weathers(fetch_weather(all)))
df_team_stats = pd.DataFrame(parse_team_game_stats(fetch_teams_stat(all)))
df_rivalries = pd.DataFrame(parse_rivalries(fetch_rivalries()))
df_prime_games = pd.DataFrame(parse_prime_time(fetch_prime_time()))
df_rankings = pd.DataFrame(parse_rankings(fetch_rankings(all)))
df_conf_strength = parse_conference_strength(parse_team_matchup(vall))

# Style of Play
df_style_raw = fetch_teams_stat(all)
df_style = compute_style_of_play(pd.DataFrame(parse_team_game_stats(df_style_raw)))

#Appel final de mon pipeline 
df_final = build_team_matchup(
       df_team_raw, 
       df_games, 
       df_weather, 
       df_style, 
       df_team_stats, 
       df_rivalries, 
       df_prime_games, 
       df_rankings, 
       df_conf_strength
)
print(df_final)

print(df_final.columns.tolist())