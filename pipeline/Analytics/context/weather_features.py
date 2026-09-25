# from pipeline.analytics.context.weather_impact import compute_weather_features
def compute_weather_schock(df):
    # sort chronologically by team
    df = df.sort_values(["team_id", "season", "week"]) 
    
    # Score weather last week
    df["weather_prev"] = df.groupby("team_id")["weather_score_norm"].shift(1)

    # Variation absolute
    df["weather_shock"] = (df["weather_score_norm"] - df["weather_prev"]).abs()

    # For a team's first week : no shock 
    df["weather_shock"] = df["weather_shock"].fillna(0)

    return df 

def compute_weather_familiarity(df, window = 5): 
    # sort by team, season , week 
    df = df.sort_values(["team_id", "season", "week"]) 
    # moving weather average 
    df["weather_familiarity"] = (
        df.groupby("team_id")["weather_score_norm"]
        .rolling(window = window, min_periods = 1)
        .mean()
        .reset_index(level = 0, drop = True)
    )

    return df 


def compute_weather_resilience(df): 
    # résilience = 1 - | météo du match  - habitude météo |
    df["weather_resilience"] = 1 - (df["weather_score_norm"] - df["weather_familiarity"]).abs()

    # On garde la valeur  entre 0 et 1 
    df["weather_resilience"] = df["weather_resilience"].clip(0, 1)
    # indoor -> perfect resilience 
    df.loc[df["game_indoors"] == True, "weather_resilience"] = 1

    return df


def compute_weather_advantage(df): 
    # retrieve score weather home and away 

    home = df[df["team_side"] == "home"][["game_id", "weather_resilience"]].rename(columns = {"weather_resilience": "resilience_home"})
    away = df[df["team_side"] == "away"][["game_id", "weather_resilience"]].rename(columns = {"weather_resilience": "resilience_away"})
  
    # Merge 
    df = df.merge(home, on = "game_id", how = "left")
    df = df.merge(away, on = "game_id", how = "left")

    # Calcul de l'avantage Meteo
    df["weather_advantage"] = df["resilience_away"].fillna(0) - df["resilience_home"].fillna(0)

    # indoor -> pas d'avantage météo
    df.loc[df["game_indoors"] == True, "weather_advantage"] = 0

    return df


def compute_weather_performance_index(df): 
    # weighted combination of the 5 weather dimensions
    df["WPI"] = (
        0.40 * df["weather_resilience"]
        + 0.20 * (1 - df["weather_score_norm"])
        + 0.20 * (1 - df["weather_shock"])
        + 0.20 * (1 +  df["weather_advantage"] )
    )
    df ["WPI"] = df ["WPI"].clip(0, 1)

    return df