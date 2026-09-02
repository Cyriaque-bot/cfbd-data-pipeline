import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.cfbd.team_roster import fetch_team_roster
from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season


from pipeline.transformation.cfbd.parse_team_roster import parse_team_roster
from pipeline.transformation.cfbd.parse_stats_player_season import parse_stats_player_season

def scrape_returning_production(result_parse_roster, result_stats_player_season):
    df_parse_roster = pd.DataFrame(result_parse_roster)
    df_stats_player_season = pd.DataFrame(result_stats_player_season)
    
    df_roster_season = (df_parse_roster
                        .merge(
                            df_stats_player_season, 
                            left_on = "player_id",
                            right_on = "playerId",
                            how = "left"
                        )
    ) 
    
 
    df_roster_season = df_roster_season.rename(columns = {"team_x":"team"})
    
    # offense 
    df_roster_season.loc[df_roster_season["returning"] == True,"returning_offense_yards_int"] = (
                                                                                                   df_roster_season["passing_yards"] 
                                                                                                 + df_roster_season["receiving_yards"] 
                                                                                                 + df_roster_season["rushing_yards"]
    )

    df_roster_season["total_offense_yards_last_year_int"] = (
                                                            df_roster_season["passing_yards"] 
                                                            + df_roster_season["receiving_yards"] 
                                                            + df_roster_season["rushing_yards"]
    )

    # defense 

    df_roster_season.loc[df_roster_season["returning"] == True,"returning_defense_yards_int"] = (
                                                                                                       df_roster_season["pressures"] 
                                                                                                     + df_roster_season["sacks"] 
                                                                                                     + df_roster_season["tackles"]
    )

    df_roster_season["total_defense_yards_last_year_int"] = (
                                                                df_roster_season["pressures"] 
                                                                + df_roster_season["sacks"] 
                                                                + df_roster_season["tackles"]
        )

    # replace all the nan with 0
    df_roster_season = df_roster_season.fillna(0)
    # put all my columns in integer
    df_roster_season["returning_offense_yards_int"] = df_roster_season["returning_offense_yards_int"].astype(int)
    df_roster_season["total_offense_yards_last_year_int"] =  df_roster_season["total_offense_yards_last_year_int"].astype(int)
    df_roster_season["returning_defense_yards_int"] = df_roster_season["returning_defense_yards_int"].astype(int)
    df_roster_season["total_defense_yards_last_year_int"] = df_roster_season["total_defense_yards_last_year_int"].astype(int)

    
    # df_roster_season = df_roster_season[["team", "season"]]
    # df_returning_offense_yards = df_roster_season.groupby(["team", "season"])["returning_offense_yards_int"].sum().reset_index(name = "returning_offense_yards")
    df_returning_offense_yards = df_roster_season.groupby(["team", "season"], as_index = False).agg(
        returning_offense_yards = ("returning_offense_yards_int", "sum"), 
        total_offense_yards_last_year = ("total_offense_yards_last_year_int", "sum"), 
        returning_defense_yards = ("returning_defense_yards_int", "sum"), 
        total_defense_yards_last_year = ("total_defense_yards_last_year_int", "sum")
       )
    df_returning_offense_yards =  df_returning_offense_yards.to_dict(orient = "records")
    return df_returning_offense_yards


# valrostfetch = fetch_team_roster()
# # print(fetch_team_roster())
# valseafetch = fetch_stats_player_season()
# valroste = parse_team_roster(valrostfetch)
# valstats_player_season = parse_stats_player_season(valseafetch)

# print(scrape_returning_production(valroste, valstats_player_season))