import sys
from pathlib import Path
import pandas as pd 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

# the scrapers 
from pipeline.scrapers.cfbd.ppa_team import fetch_ppa_team
from pipeline.scrapers.cfbd.talent import fetch_talent
from pipeline.scrapers.cfbd.media import fetch_media
from pipeline.scrapers.derived.coach import fetch_coach_rating
# from data.raw.external 

from pipeline.transformation.cfbd.parse_ppa_team import parse_ppa_team
from pipeline.transformation.cfbd.parse_media import parse_media 
from pipeline.transformation.cfbd.parse_talent import parse_talent
from pipeline.transformation.derived.parse_coach_rating import parse_coaching_rating
from pipeline.analytics.matchup.compute_coaches_rating import compute_coach_rating


def compute_team_strength(val_ppa_team, val_media, val_talent, val_coaching_rating): 
    # transform all my list in dataframe in order to male m
    df_val_ppa_team = pd.DataFrame(val_ppa_team)
    df_val_media = pd.DataFrame(val_media)
    df_val_talent = pd.DataFrame(val_talent)
    df_val_coaching_rating = pd.DataFrame(val_coaching_rating)

    df_inter_one = (df_val_ppa_team
                   .merge(df_val_media, left_on = ["school","season"], right_on = ["home_team", "season"])        
    )

    df_inter_two = (df_val_ppa_team
                    .merge(df_val_media, left_on = ["school" , "season"], right_on = ["away_team", "season"]))
    df_inter = pd.concat([df_inter_one, df_inter_two])

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





valscpppateam = fetch_ppa_team()
valscpmedia = fetch_media()
valscptalent = fetch_talent()
valscpcoachrating = fetch_coach_rating()
valoparsecoaching = parse_coaching_rating(valscpcoachrating)

valoparseppateam = parse_ppa_team(valscpppateam)
valoparsemedia = parse_media(valscpmedia)
valoparsetalent = parse_talent(valscptalent)
valcomputecoaching = compute_coach_rating(valoparsecoaching)

print(compute_team_strength(valoparseppateam, valoparsemedia, valoparsetalent, valcomputecoaching ))