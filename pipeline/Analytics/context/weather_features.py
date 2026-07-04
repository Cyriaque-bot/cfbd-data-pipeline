# from pipeline.analytics.context.weather_impact import compute_weather_features
def compute_weather_schock(df):
    # Trier par équipe et chronologie
    df = df.sort_values(["team", "season", "week"]) 
    # Score meteo de la semaine précédente 
    df["weather_prev"] = df.groupby("team")["weather_score_norm"].shift(1)

    # Variation absolue 
    df["weather_shock"] = (df["weather_score_norm"] - df["weather_prev"]).abs()

    # Pour la première semaine d'une équipe : pas de choc 
    df["weather_shock"] = df["weather_shock"].fillna(0)

    return df 

def compute_weather_familiarity(df, window = 5): 
    # Trier par équipe, saison, semaine 
    df = df.sort_values(["team", "season", "week"]) 
    # Calculer le moyenne glissante du score météo
    df["weather_familiarity"] = (
        df.groupby("team")["weather_score_norm"]
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

    return df


def compute_weather_advantage(df): 
    # retrieve score weather home and away 
    home = df[df["is_home"] == 1][["game_id", "weather_resilience"]].rename(columns = {"weather_resilience": "resilience_home"})
    away = df[df["is_away"] == 1][["game_id", "weather_resilience"]].rename(columns = {"weather_resilience": "resilience_away"})
  
    # Merge 
    df = df.merge(home, on = "game_id", how = "left")
    df = df.merge(away, on = "game_id", how = "left")

    # Calcul de l'avantage Meteo
    df["weather_advantage"] = df["resilience_away"].fillna(0) - df["resilience_home"].fillna(0)


    return df


def compute_weather_performance_index(df): 
    # comnibinnaison pondérées des 5 dimensions météo
    df["WPI"] = (
        0.40 * df["weather_resilience"]
        + 0.20 * (1 - df["weather_score_norm"])
        + 0.20 * (1 - df["weather_shock"])
        + 0.20 * (1 +  df["weather_advantage"] )
    )
    df ["WPI"] = df ["WPI"].clip(0, 1)

    return df