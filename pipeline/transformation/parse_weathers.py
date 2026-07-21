import os 
import sys
from pathlib import Path 
import pandas as pd 


project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))


from pipeline.transformation.parse_games import parse_games
from pipeline.scrapers.games import fetch_games
from pipeline.scrapers.weather import fetch_weather
# retrieve the datacolumns 
def parse_weathers(weathersraw): 
    listweather = []

    for i in weathersraw: 
        weathersdict = {
            "game_id": i["id"], 
            "season": i["season"], 
            "season_type": i["seasonType"], 
            "start_date": i["startDate"], 
            "venue": i["venue"], 
            "home_team": i["homeTeam"], 
            "away_team": i["awayTeam"], 
            "temperature": i["temperature"], 
            "dew_point": i["dewPoint"], 
            "humidity": i["humidity"], 
            "precipitation": i["precipitation"], 
            "wind_speed": i["windSpeed"], 
            "wind_direction": i["windDirection"], 
            "pressure": i["pressure"], 
            "condition": i["condition"]
        }

        listweather.append(weathersdict)
    
    return listweather
  
  # convertir mon games en DataFrame

# valgames = fetch_games(all)
# vallgames = parse_games(valgames)
# vallgames_df = pd.DataFrame(vallgames)

# valweather = fetch_weather(all)
# vallweather = parse_weathers(valweather)
# listweather_df = pd.DataFrame(vallweather) 
    
# # # merging vallgames_df
# def merge_weather_with_games(listweather_df: pd.DataFrame , vallgames_df: pd.DataFrame)->pd.DataFrame: 
#     merged = listweather_df.merge(
#          vallgames_df, 
#          left_on = "game_id", 
#          right_on = "game_id", 
#          how =  "left"
#     )
#     return merged



# print(merge_weather_with_games(listweather_df , vallgames_df))