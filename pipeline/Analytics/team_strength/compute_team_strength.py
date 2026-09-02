import sys
from pathlib import Path
import pandas as pd 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

# the load 
from pipeline.loaders.external.load_conference_strength import load_conference_strength
# the scrapers 
from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season
from pipeline.scrapers.cfbd.team_roster import fetch_team_roster
from pipeline.scrapers.cfbd.season_advanced import fetch_season_advanced
from pipeline.scrapers.cfbd.talent import fetch_talent
from pipeline.scrapers.cfbd.media import fetch_media
from pipeline.scrapers.cfbd.rankings import fetch_rankings
from pipeline.scrapers.cfbd.teams import fetch_teams

# the parse
from pipeline.transformation.cfbd.parse_season_advanced import parse_season_advanced
from pipeline.transformation.cfbd.parse_media import parse_media 
from pipeline.transformation.cfbd.parse_talent import parse_talent
from pipeline.transformation.cfbd.parse_team_roster import parse_team_roster
from pipeline.transformation.cfbd.parse_stats_player_season import parse_stats_player_season
from pipeline.transformation.external.parse_conference_strength import parse_conference_strength
from pipeline.transformation.cfbd.parse_top25 import parse_top25
from pipeline.transformation.cfbd.parse_teams import parse_teams 


# from pipeline.analytics.team_strength.team_top25 import 

# the analytics
from pipeline.analytics.matchup.compute_coaches_rating import compute_coach_rating
from pipeline.analytics.returning_production.scraper_returning_production import scrape_returning_production
from pipeline.analytics.matchup.compute_coaches_rating import compute_coach_rating
from pipeline.analytics.coach.scraper_coach_rating import scrape_coach_rating
from pipeline.analytics.coach.parse_coach_rating import parse_coach_rating
from pipeline.analytics.team_strength.scraper_team_top25 import scraper_team_top25
def compute_team_strength(
                          val_season_advanced, 
                          val_media,
                          val_talent, 
                          val_coaching_rating,
                          val_returning_production, 
                          val_conference_strength, 
                          val_team_top25
                          ): 
    # transform all my list in dataframe in order to male m
    df_val_season_advanced = pd.DataFrame(val_season_advanced) 
    df_val_media = pd.DataFrame(val_media)
    df_val_talent = pd.DataFrame(val_talent)
    df_val_coaching_rating = pd.DataFrame(val_coaching_rating)
    df_val_returning_production = pd.DataFrame(val_returning_production)
    df_val_conference_strength = pd.DataFrame(val_conference_strength)
    df_val_team_top25 = pd.DataFrame(val_team_top25)



    df_compute_team_final = (df_val_season_advanced
                   .merge(df_val_media, left_on = ["school","season"], right_on = ["home_team", "season"])        
    )

    
    df_inter_final = ( df_inter
    .merge(
        df_val_talent, 
        on = ["school", "season"], 
        how = "left"
        )
    .merge(
        df_val_coaching_rating, 
        on = ["school","season"], 
        how = "left"
       )
    )

    df_inter_final = df_inter_final.to_csv()

    # return df_inter_final.columns.tolist()
    return df_inter_final





# valscpppateam = fetch_ppa_team()
# valscpmedia = fetch_media()
# valscptalent = fetch_talent()
# valscpcoachrating = fetch_coach_rating()
# valoparsecoaching = parse_coaching_rating(valscpcoachrating)

# valoparseppateam = parse_ppa_team(valscpppateam)
# valoparsemedia = parse_media(valscpmedia)
# valoparsetalent = parse_talent(valscptalent)
# valcomputecoaching = compute_coach_rating(valoparsecoaching)

# print(compute_team_strength(valoparseppateam, valoparsemedia, valoparsetalent, valcomputecoaching ))