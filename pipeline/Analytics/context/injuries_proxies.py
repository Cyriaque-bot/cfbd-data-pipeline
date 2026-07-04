import pandas as pd

# Offense Drop

def compute_offense_drop(df): 
    raw = df["recent_points_for"] - df["points_for"]

    # Normalisation par la valeurs absolue max 
    max_abs = raw.abs().max()
    if pd.isna(max_abs) or max_abs == 0: 
       df["defense_collapse"] = 0
    else: 
       df["defense_collapse"] =  raw.abs()/ max_abs
    return df

# defense collapse
def compute_defense_collapse(df): 
    raw = df["points_against"] - df["recent_points_against"]
    max_abs = raw.abs().max()
    if pd.isna(max_abs) or max_abs == 0: 
        df["defense_collapse"] = 0
    else: 
        df["defense_collapse"] =  raw.abs() / max_abs
    return df 

# margin shock
def compute_margin_shock(df): 
    raw = df["recent_margin"] - df["margin"]
    max_abs = raw.abs().max()
    if pd.isna(max_abs) or max_abs == 0: 
        df["margin_shock"] = 0
    else: 
        df["margin_shock"] = raw.abs() /  max_abs
    return df 

# momentum shock
def compute_momentum_shock(df): 
    df = df.sort_values( by = ["team", "season", "week"])
    
    df["momentum_prev"] = df.groupby("team")["momentum_score"].shift(1)

    raw = df["momentum_score"] - df["momentum_prev"]

    raw  =  raw.fillna(0)

    max_abs = raw.abs().max()
    if pd.isna(max_abs) or max_abs == 0: 
        df["momentum_shock"]  = 0
    else: 
        df["momentum_shock"] = raw.abs() / max_abs
    return df 


def compute_injury_proxy_score(df): 
    df["injury_proxy_raw"] = (
        0.3 * df["offense_drop"] + 
        0.3 * df["defense_collapse"] + 
        0.2 * df["margin_shock"] + 
        0.2 * df["momentum_shock"]
    )
    return df


def normalize_injury_proxy(df): 
    min_val = df["injury_proxy_raw"].min()
    max_val = df["injury_proxy_raw"].max()

    if min_val == max_val: 
         df["injury_proxy_norm"] = 0
    else: 
         df["injury_proxy_norm"] = (df["injury_proxy_raw"] - min_val) / (max_val - min_val)

    return df 


def compute_injuries_proxies(df): 
    # Tri chronologique indispensable 

    df = df.sort_values(by = ["team", "season", "week"])

    # 1) offense Drop
    df = compute_offense_drop(df) 
    # 2) defense collapse 
    df = compute_defense_collapse(df)
    # 3) margin shock
    df = compute_margin_shock(df)
    # 4) mementum schock 
    df = compute_momentum_shock(df)

    # 5) score global pondéré
    df = compute_injury_proxy_score(df)
    # 6) Normalisation 
    df = normalize_injury_proxy(df)

    return df 