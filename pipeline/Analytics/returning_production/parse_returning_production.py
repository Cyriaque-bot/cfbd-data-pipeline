import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season
from pipeline.scrapers.cfbd.team_roster import fetch_team_roster

from pipeline.transformation.cfbd.parse_team_roster import parse_team_roster
from pipeline.transformation.cfbd.parse_stats_player_season import parse_stats_player_season

from pipeline.analytics.returning_production.scraper_returning_production import scrape_returning_production

def parse_returning_production(raw_scrape_returning_production): 

    list_parse_returning_production = []

    for i_scrape_returning_production in raw_scrape_returning_production: 
        dict_parse_returning_production  = {
            "school": i_scrape_returning_production["team"], 
            "returning_production": 
               round(   
                       (
                        float( 0.5 *
                               (i_scrape_returning_production["returning_offense_yards"]/i_scrape_returning_production["total_offense_yards_last_year"])
                             +
                               0.5 * 
                               (i_scrape_returning_production["returning_defense_yards"]/i_scrape_returning_production["total_defense_yards_last_year"])      
                             )
                    ), 2
               )

            }   
        list_parse_returning_production.append(dict_parse_returning_production)

    return list_parse_returning_production


vallstats = fetch_stats_player_season()
vallroster = fetch_team_roster()
vallparsestat = parse_stats_player_season(vallstats)
vallparseroste = parse_team_roster(vallroster)
# print(scrape_returning_production(vallparseroste, vallparsestat))
vall = scrape_returning_production(vallparseroste, vallparsestat)
print(parse_returning_production(vall))