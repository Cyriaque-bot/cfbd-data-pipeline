
# recent point for
def compute_recent_points_for(df, window = 3): 
    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)

    df["recent_points_for"] = (
        df.groupby("team_id")["team_points"]
        .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df

# recent points againts 
def compute_recent_points_against(df, window = 3): 
    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)

    df["recent_points_against"] = ( 
        df.groupby("team_id")["opponent_points"]
          .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df 

# recent margin 

def compute_recent_margin(df, window = 3): 
    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)
    df["margin"] = df["team_points"] - df["opponent_points"]
    df["recent_margin"] = (
        df.groupby("team_id")["margin"]
          .transform(lambda x:x.rolling(window, min_periods = 1).mean())
    )

    return df

# momentum score 
def compute_momentum_score(df):
    # Momentum = points_for - points_against (normalisé)
    df["momentum_score"] = df["team_points"] - df["opponent_points"]
    return df

def compute_recent_momentum(df, window = 3): 
    df["recent_momentum"] = (df.groupby("team_id")["momentum_score"]
                             .transform(lambda x:x.rolling(window, min_periods = 1).mean()))
    return df

def compute_offense_defense_shocks(df): 
    df["offense_drop"] = df["recent_points_for"] - df["team_points"]
    df["defense_collapse"] =  df["opponent_points"] - df["recent_points_against"]
    df["margin_shock"] =  df["recent_margin"] - df["margin"]
    df["momentum_shock"] = df["momentum_score"] -  df["recent_momentum"]
    return df

def compute_recent_offense_defense(df , window = 3): 
    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)

    df = compute_recent_points_for(df, window = window)
    df = compute_recent_points_against(df, window = window)
    df = compute_recent_margin(df, window = window)
    df = compute_momentum_score(df)
    df = compute_recent_momentum(df)
    df = compute_offense_defense_shocks(df)

    return df 