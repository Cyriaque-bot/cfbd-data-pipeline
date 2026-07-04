import pandas as pd 
from pathlib import Path
import os 
import sys

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def compute_weather_features(df_weather, df_style, df_team_stats): 

    # combine les données météo avec le style de jeu pour produire : 
    # -  wind_impact 
    # -  rain_impact 
    # -  temperature_impact
    # -  humidity_impact
    # -  weather_score_raw
    # -  weather_score_norm
    # -  weather_sensivity

    # conversion de mon weather en Dataframe parce que c'est une liste 
    df_weather = pd.DataFrame(df_weather)

    # étendre la météo a chaque équipe du match 

    df_weather_expanded = df_team_stats[["game_id", "team_id"]].merge(
        df_weather, 
        on = "game_id", 
        how = "left"
    )
    
    # Fusion  météo + style de jeu 
    df = df_weather_expanded.merge(df_style, on = ["game_id", "team_id"], how = "left")


    df["wind_impact"] = df["wind_speed"].clip(0, 30) / 30
    df["rain_impact"] = (df["precipitation"]/5).clip(0, 1)

    df["temperature_impact"] = df["temperature"].apply(
        lambda t: abs(t - 30) / 30 if pd.notna(t)  else 0
    ).clip(0,1)

    df["humidity_impact"] = df["humidity"]/100
   


    df["weather_score_raw"] =  (

        0.35 * df["wind_impact"] + 
        0.35 * df["rain_impact"] + 
        0.20 * df["temperature_impact"] + 
        0.10 * df["humidity_impact"]

    )
  
   # Normalized score soit score de difficulté météo 
    min_val = df["weather_score_raw"].min()
    max_val = df["weather_score_raw"].max()
    if max_val == min_val: 
        df["weather_score_norm"] = 0
    else: 
        df["weather_score_norm"] = (df["weather_score_raw"]  - min_val) /(max_val - min_val)

    df["weather_score_norm"] = df["weather_score_norm"].fillna(0)
    # sensiblity météo selon style de jeu 
    df["weather_sensitivity"] = (
        0.6 *  df["pass_heavy"] * (df["wind_impact"] + df["rain_impact"])+
        0.4 * df["run_heavy"] * df["rain_impact"]+
        0.2 * df["balanced"] * df["weather_score_raw"]
    )
    
    return df 



# from pipeline.scrapers.teams_stat import fetch_teams_stat
# from pipeline.scrapers.weather import fetch_weather
# from pipeline.transformation.parse_weathers import parse_weathers
# from pipeline.transformation.parse_team_stats import parse_team_stats
# from pipeline.analytics.context.style_of_play import compute_style_of_play
# raw_team_stat = fetch_teams_stat(all)
# raw_parse_team_stat = parse_team_stats(raw_team_stat)
# df_raw_parse_team_stat = pd.DataFrame(raw_parse_team_stat)

# vallraw_weather = fetch_weather(all)
# vallrawparse_weather = parse_weathers(vallraw_weather)
# df_vallrawparses_weather = pd.DataFrame(vallrawparse_weather)


# valdatafraf = compute_style_of_play(df_raw_parse_team_stat)
# print(compute_weather_features(vallrawparse_weather, valdatafraf, df_raw_parse_team_stat))

