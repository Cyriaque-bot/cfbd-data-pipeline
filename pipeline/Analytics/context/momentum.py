import pandas as pd 


def compute_streaks(df): 
    df = df.sort_values(["team_id", "date"]).reset_index(drop = True)

    # Win streak (T, and L reset the streak)
    df["win_streak"] = (
        df.groupby("team_id")["result"]
          .transform(lambda x: x.eq("W").astype(int).groupby((x != "W").cumsum()).cumsum())
    )

    # Loss streak (T and W reset the streak)

    df["loss_streak"] = (
        df.groupby("team_id")["result"]
          .transform(lambda x: x.eq("L").astype(int).groupby((x != "L").cumsum()).cumsum())
    )

    # 

    return df



def compute_recent_margin(df, window = 3): 
    df = df.sort_values(["team_id", "date"]).reset_index(drop = True)

# gross margin 

    df["margin"] = df["points_for"] - df["points_against"]

# Average over the last N matches

    df["recent_margin"] = (
    df.groupby("team_id")["margin"]
      .transform(lambda x: x.rolling(window, min_periods = 1).mean())
    ) 
    return df


# creating a generic function 

def normalize_column(df, col): 
    col_min = df[col].min()
    col_max = df[col].max()
    if col_max == col_min: 
        return df[col] * 0
    return (df[col] - col_min) / (col_max - col_min)

# Now, we normalize the momentum features.

def normalize_column_features (df): 
    df["win_streak_norm"] = normalize_column(df, "win_streak")
    df["loss_streak_norm"] = normalize_column(df, "loss_streak")
    df["recent_margin_norm"] = normalize_column(df, "recent_margin")
    return df


def compute_momentum_score(df, w_streak = 0.4, w_margin = 0.3, w_loss = 0.3):
    # Combine win_streak, loss_streak et reent_margin en un score unique de momentum

    df["momentum_score"] = (
        w_streak * df["win_streak_norm"]
        + w_margin * df["recent_margin_norm"]
        - w_loss * df["loss_streak_norm"]
    )

    return df

# compute_momentum_differential()

def compute_momentum_differential(df): 
    # Our goal here is to show that one team is entering the match with better momentum than the others.
    # We create a df avec team -> momentum_score 
    opp = df[["team_id", "season", "week", "momentum_score"]].copy()
    opp = opp.rename(columns = {
        "team_id": "opponent_id", 
        "momentum_score": "opponent_momentum_score"
    })

    # we retrieved opponent
    df = df.merge(
        opp, 
        on = ["opponent_id", "season", "week"], 
        how = "left"
    )

    # On calcule le différentiel 
    df["momentum_differential"] = (df["momentum_score"] -  df ["opponent_momentum_score"]).fillna(0)

    return df


# new version of momentum with weathers

def adjust_momentum_with_wpi(df): 
    df["momentum_weather_adj"] =  df["momentum_score"] * (0.5 + 0.5 * df["WPI"].fillna(0))
    return df 