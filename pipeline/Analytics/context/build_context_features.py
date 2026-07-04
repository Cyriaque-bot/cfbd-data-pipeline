import pandas as pd 
from pathlib import Path
import sys 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.analytics.context.style_of_play import compute_style_of_play
from pipeline.analytics.context.weather_impact import compute_weather_features
from pipeline.analytics.context.weather_features import compute_weather_schock, compute_weather_familiarity, compute_weather_resilience
from pipeline.analytics.context.weather_features import compute_weather_advantage, compute_weather_performance_index
from pipeline.analytics.context.recent_offense_defense import compute_recent_offense_defense
from pipeline.analytics.context.injuries_proxies import compute_injuries_proxies
from pipeline.analytics.context.pressure_proxies import compute_pressure_proxies
from pipeline.analytics.context.momentum import compute_streaks, compute_recent_margin, normalize_column_features, compute_momentum_score
from pipeline.analytics.context.momentum import compute_momentum_differential, adjust_momentum_with_wpi
from pipeline.analytics.context.schedule_difficulty import compute_schedule_difficulty, compute_schedule_difficulty_rolling,compute_schedule_difficulty_weighted 


def build_context_features(
        df, 
        df_weather, 
        df_style, 
        df_team_stats, 
        df_rivalries, 
        df_prime_games, 
        df_rankings, 
        df_conf_strength
): 
    # tri initial 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    # style de jeu (run/pass/balanced + 3rd/4th  down)
    df_style = compute_style_of_play(df_style)

    # Meteo (weather_score_norm + impacts + WPI)
    df_weather_features =  compute_weather_features(df_weather, df_style, df_team_stats)
    df = df.merge(
        df_weather_features[
            ["game_id", "team_id", "wind_impact", "rain_impact", "temperature_impact", "humidity_impact",
              "weather_score_raw", "weather_score_norm", "weather_sensitivity"]
        ], 
        on = ["game_id", "team_id"], 
        how = "left"
    )

    # weather shock / familiarity / resilience / advantage / WPI

    df = compute_weather_schock(df)
    df = compute_weather_familiarity(df)
    df = compute_weather_resilience(df)
    df = compute_weather_advantage(df)
    df = compute_weather_performance_index(df)

    # recent offense & defense 
    df = compute_recent_offense_defense(df)

    # injuries proxies
    df = compute_injuries_proxies(df)

    # pressure proxies
    df = compute_pressure_proxies(df, df_rivalries , df_prime_games, df_rankings)

    # momentum
    df = compute_streaks(df)
    df = compute_recent_margin(df)
    df = normalize_column_features(df)
    df = compute_momentum_score(df)
    df = compute_momentum_differential(df)
    df = adjust_momentum_with_wpi(df)
    
    # schedule difficulty
    df = compute_schedule_difficulty(df)
    df = compute_schedule_difficulty_rolling(df)
    df = compute_schedule_difficulty_weighted(df)

    return df 