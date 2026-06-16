import pandas as pd 
import numpy as np 

def compute_rivalry_pressue(df, rivalry_list = None): 
    # rivalry_list: liste de Tuples (team, opponent)
    # Exemple : [("Alabame", "Auburn"), ("Texas", "Oklahoma")]

    if rivalry_list is None: 
        rivalry_list = []

    df["rivalry_pressure"] = df.apply(
        lambda row : 1 if (row["team"], row["opponent"]) in rivalry_list or (row["opponent"], row["team"]) in rivalry_list
                      else 0,
                      axis = 1
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
        df["media_pressure"] =  df["media_pressure"] + df["media_pressure"].fillna(0)

    # Si Proxy simple : match entre deux équipes 
    if "team_rank" in df.columns and "opponent_rank" in df.columns: 
        df["media_pressure"] = df["media_pressure"]((df["team_rank"] <= 25) & (df["opponent_rank"] <= 25)).astype(int)
    return df 

def compute_psychological_shock(df):
    # pression psychologique basées sur le match précédent : 
    # Grosse victoire -> pression de confirmer 
    # Grosse défaite  -> pressionde Rebondir 

    df = df.sort_values(["team", "date"]).reset_index(drop = True)
    df["prev_margin"] = df.groupby("team")["point_diff"].shift(1)
    df["psychological_shock"] = df["prev_margin"].abs() / df["prev_margin"].abs().max()
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

def compute_pressure_proxies(df, rivalry_list = None): 
    df = compute_rivalry_pressue(df, rivalry_list)
    df = compute_stakes_pressure(df)
    df = compute_stakes_pressure(df)
    df = compute_psychological_shock(df)
    df = compute_pressure_index(df)

    return df