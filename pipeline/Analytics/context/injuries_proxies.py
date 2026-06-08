
def compute_offense_drop(df): 
    df["offense_drop"] = df["recent_points_for"] - df["points_for"]
    return df


def compute_defense_collapse(df): 
    df["defense_collapse"] = df["points_against"] - df["recent_points_against"]
    return df 


def compute_margin_shock(df): 
    df["margin_shock"] = df["recent_margin"] - df["margin"]
    return df 

def compute_momentum_shock(df): 
    df = df.sort_values( by = ["team", "season", "week"])
    
    df["momentum_prev"] = df.groupby("team")["momentum_score"].shift(1)

    df["momentum_shock"] = df["momentum_score"] - df["momentum_prev"]

    # remplacer les NaN du premier match par 0
    df["momentum_shock"] = df["momentum_shock"].fillna(0)

    return df 

def compute_injury_proxy_score(df): 
    df["injury_proxy_raw"] = (
        0.4 * df["offense_drop"] + 
        0.3 * df["defense_collapse"] + 
        0.2 * df["margin_shock"] + 
        0.1 * df["momentum_shock"]
    )

    return df


def normalize_injury_proxy(df): 
    min_val = df["injury_proxy_raw"].min()
    max_val = df["injury_proxy_raw"].max()

    df["injury_proxy_norm"] = (
      (df["injury_proxy_raw"] - min_val) / (max_val - min_val)
    )

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
    # 4) Mementum Schock 
    df = compute_momentum_shock(df)
    # 5) Score global pondéré
    df = compute_injury_proxy_score(df)
    # 6) Normalisation 
    df = normalize_injury_proxy(df)

    return df 