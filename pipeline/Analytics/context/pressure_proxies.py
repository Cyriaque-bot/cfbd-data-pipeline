import pandas as pd 
import numpy as np 
from pathlib import Path 
import sys
import os 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


# df = pd.DataFrame([
#     {
#         "team": "Alabama",
#         "opponent": "Auburn",
#         "season": 2023,
#         "week": 1,
#         "season_type": "regular",
#         "date": "2023-09-02",
#         "point_diff": 14,
#         "game_id": 401520000
#     },
#     {
#         "team": "Georgia",
#         "opponent": "UT Martin",
#         "season": 2023,
#         "week": 1,
#         "season_type": "regular",
#         "date": "2023-09-02",
#         "point_diff": 28,
#         "game_id": 401520001
#     }
# ])  



def merge_rivalries(df, rivalries_df): 
    # Convertir en DataFrame
    riv = pd.DataFrame(rivalries_df)
    # Merge direct (team vs opponent)
    df = df.merge(
        riv[["team", "opponent"]].assign(rivalry_pressure = 1), 
        on = ["team", "opponent"], 
        how = "left"
    )
    # Merge inverse (opponent vs team)
    rev_inv = riv.rename(columns = {"team": "opponent", "opponent": "team"})
    df = df.merge(
        rev_inv[["team", "opponent"]].assign(rivalry_pressure_inv = 1), 
        on = ["team", "opponent"], 
        how = "left"
    )

    # Fusionner les deux colonnes 
    df["rivalry_pressure"] = df[["rivalry_pressure", "rivalry_pressure_inv"]].max(axis = 1).fillna(0).astype(int)

    # Nettoyage 
    df = df.drop(columns = ["rivalry_pressure_inv"], errors = "ignore")
    return df 


def merge_prime_time(df, prime_df):
    prime = pd.DataFrame(prime_df)
    df = df.merge(
        prime, 
        on = 'game_id', 
        how =  "left"
    )
    df["is_prime_time"] = df["is_prime_time"].fillna(0).astype(int)
    return df 

    # Merge ranking
def merge_rankings(df, rankings_df): 
    rank = pd.DataFrame(rankings_df)
    
    # Team Rank 
    df = df.merge(
        rank.rename(columns = {"school": "team", "rank": "team_rank"})[["season", "week", "team", "team_rank"]], 
        on = ["season", "week", "team"], 
        how = "left"
    )
    # opponent rank 
    df = df.merge(
        rank.rename(columns = {"school": "opponent", "rank": "opponent_rank"})[["season", "week", "opponent", "opponent_rank"]], 
        on = ["season", "week", "opponent"],
        how = "left"
    )
    return df 

def compute_stakes_pressure(df):
    # Pression liée à l'enjeu du match 
    # bowl, playoffs, championship , rivalry week

    df["stakes_pressure"] = 0
    df.loc[df["season_type"].str.contains("championship", case = False, na = False), "stakes_pressure"] = 1
    df.loc[df["season_type"].str.contains("postseason", case = False, na = False), "stakes_pressure"] = 1
    df.loc[df["week"] >= 12,"stakes_pressure"] = 1 # fin de saison enjeux plus élévés

    return df
    
def compute_media_pressure(df): 
    # Pression liées à la médiatisation , prime time, Tv national , gros mtch(top 25) 
    df["media_pressure"] = 0

    # Si nous avons une colonne "is_prime_time" otu "tv_audience", nous pouvons l'utiliser 
    if "is_prime_time" in df.columns: 
        df["media_pressure"] =  df["media_pressure"] + df["is_prime_time"].fillna(0)

    # Si Proxy simple : match entre deux équipes 
    if "team_rank" in df.columns and "opponent_rank" in df.columns: 
        df["media_pressure"] = df["media_pressure"] + ((df["team_rank"] <= 25) & (df["opponent_rank"] <= 25)).astype(int)
    return df 

def compute_psychological_shock(df):
    # pression psychologique basées sur le match précédent : 
    # Grosse victoire -> pression de confirmer 
    # Grosse défaite  -> pressionde Rebondir 

    df = df.sort_values(["team", "date"]).reset_index(drop = True)
    df["prev_margin"] = df.groupby("team")["point_diff"].shift(1)
    max_abs = df["prev_margin"].abs().max()
    if pd.isna(max_abs) or max_abs == 0: 
        df["psychological_shock"] = 0
    else: 
        df["psychological_shock"] = df["prev_margin"].abs() / max_abs

    df["psychological_shock"] = df["psychological_shock"].fillna(0)

    return df

def compute_pressure_index(df, w_rivalry = 0.25, w_stakes = 0.25, w_media = 0.25, w_shock = 0.25): 
    # Score final deoression (0 à 1)
    df["pressure_index"] = (
        w_rivalry * df["rivalry_pressure"] + 
        w_stakes * df["stakes_pressure"] + 
        w_media  * df["media_pressure"] + 
        w_shock * df["psychological_shock"]
    )
    return df

def compute_pressure_proxies(df, rivalries_df , prime_df, rankings_df ): 
    df = merge_rivalries(df, rivalries_df)
    df = merge_prime_time(df, prime_df)
    df = merge_rankings(df, rankings_df)

    df = compute_stakes_pressure(df)
    df = compute_media_pressure(df)
    df = compute_psychological_shock(df)
    df = compute_pressure_index(df)

    return df

# if __name__ == "__name__":
# from pipeline.scrapers.prime_time import fetch_prime_time
# from pipeline.scrapers.rankings import fetch_rankings
# from pipeline.scrapers.rivalries import fetch_rivalries
# from pipeline.transformation.parse_rankings import parse_rankings
# from pipeline.transformation.parse_prime_time import parse_prime_time
# from pipeline.transformation.parse_rivalries import parse_rivalries

# valrivalries = fetch_rivalries()
# rivalries_df = parse_rivalries(valrivalries)

# valprime = fetch_prime_time()
# prime_df  = parse_prime_time(valprime)

# valranking = fetch_rankings(all)
# rankings_df = parse_rankings(valranking)

# df_with_pressure = compute_pressure_proxies(df, rivalries_df, prime_df, rankings_df )
# print(df_with_pressure.head())

# print(df_with_pressure.columns)