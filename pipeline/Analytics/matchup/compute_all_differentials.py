import pandas as pd 


def compute_all_differentals(df: pd.DataFrame)-> pd.DataFrame: 
    
    # Calcules différentiels entre team et opponent pour les  colonnes clés.

    # colonne pour lesquelles on veut un différentiel
    # je reviendrais la dessu plus tard 

    diff_columns = [
        "team_strength", 
        "avg_points_for", 
        "avg_points_against", 
        "avg_margin", 
        "win_rate", 
        "momentum", 
        "pressure_index", 
        "weather_advantage", 
        "style_score", 
        "schedule_difficulty_norm", 
        "coach_advantage"
    ]
    return df