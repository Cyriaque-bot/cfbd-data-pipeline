import pandas as pd 


def compute_streaks(df): 
    df = df.sort_values(["team", "date"]).reset_index(drop = True)

    # Win streak
    df["win_streak"] = (
        df.groupby("team")["result"]
          .transform(lambda x: x.eq("W").astype(int).groupby((x != "W").cumsum()).cumsum())
    )

    # Loss streak 

    df["loss_streak"] = (
        df.groupby("team")["result"]
          .transform(lambda x: x.eq("L").astype(int).groupby((x != "L").cumsum()).cumsum())
    )

    return df


# df_test = compute_streaks(final)
# print(df_test[["team", "date", "result", "win_streak", "loss_streak"]])

def compute_recent_margin(df, window = 3): 
    df = df.sort_values(["team", "date"]).reset_index(drop = True)

# Marge brute 

    df["margin"] = df["points_for"] - df["points_against"]

# Moyenne sur les N derniers matchs

    df["recent_margin"] = (
    df.groupby("team")["margin"]
      .transform(lambda x: x.rolling(window, min_periods = 1).mean())
    ) 
    return df


# Création d'une fonction générique 

def normalize_column(df, col): 
    col_min = df[col].min()
    col_max = df[col].max()
    if col_max == col_min: 
        return df[col] * 0
    return (df[col] - col_min) / (col_max - col_min)

# Maintenant on normalise les features momentum

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
    # notre objectif ici est de monter qu'une équipe arrive dans le match avec une meilleure dynamique que les autres.
    # On crée un df avec team -> momentum_score 
    opp = df[["team", "season", "week", "momentum_score"]].copy()
    opp = opp.rename(columns = {
        "team": "opponent", 
        "momentum_score": "opponent_momentum_score"
    })

    # On merge pour récupérer le momentum de l'adversaire
    df = df.merge(
        opp, 
        on = ["opponent", "season", "week"], 
        how = "left"
    )

    # On calcule le différentiel 
    df["momentum_differential"] = (df["momentum_score"] -  df ["opponent_momentum_score"]).fillna(0)

    return df


# Nouvelle version de notre momentum avec le facteur météo 

def adjust_momentum_with_wpi(df): 
    df["momentum_weather_adj"] =  df["momentum_score"] * (0.5 + 0.5 * df["WPI"].fillna(0))
    return df 