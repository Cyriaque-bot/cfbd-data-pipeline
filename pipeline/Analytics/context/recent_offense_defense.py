import pandas as pd 

# recent point for
def compute_recent_points_for(df, window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df["recent_points_for"] = (
        df.groupby("team")["points_for"]
        .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df

# recent points againts 
def compute_recent_points_against(df, window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df["recent_points_against"] = ( 
        df.groupby("team")["points_against"]
          .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df 

# recent margin 

def compute_recent_margin(df, window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)
    df["margin"] = df["points_for"] - df["points_against"]
    df["recent_margin"] = (
        df.groupby("team")["margin"]
          .transform(lambda x:x.rolling(window, min_periods = 1).mean())
    )

    return df

# momentum score 
def compute_momentum_score(df):
    # Momentum = points_for - points_against (normalisé)
    df["momentum_score"] = df["points_for"] - df["points_against"]
    return df

def compute_offense_defense_shocks(df): 
    df["offense_drop"] = df["recent_points_for"] - df["points_for"]
    df["defense_collapse"] =  df["points_against"] - df["recent_points_against"]
    df["magin_shock"] =  df["recent_margin"] - df["margin"]
    df["momentum_shock"] = df["momentum_score"] -  df["recent_margin"]
    return df

def compute_recent_offense_defense(df , window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df = compute_recent_points_for(df, window = window)
    df = compute_recent_points_against(df, window = window)
    df = compute_recent_margin(df, window = window)
    df = compute_momentum_score(df)

    df = compute_offense_defense_shocks(df)

    return df 