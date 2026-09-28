import pandas as pd 
from pathlib import Path 
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

# scrapers 
from pipeline.scrapers.derived.merge_team import fetch_merge_team
from pipeline.scrapers.cfbd.rivalries import fetch_rivalries
from pipeline.scrapers.cfbd.media import fetch_media
from pipeline.scrapers.cfbd.rankings import fetch_rankings

# parse
from pipeline.transformation.derived.parse_merge_team import parse_merge_team
from pipeline.transformation.cfbd.parse_rivalries import parse_rivalries
from pipeline.transformation.cfbd.parse_media import parse_media
from pipeline.transformation.cfbd.parse_rankings import parse_rankings

def build_team_id_map(df): 
    df = pd.DataFrame(df)
    # build a reliable mapping table between team (string) and team_id based on merge_merge_team
    team_map = df[["team", "team_id"]].drop_duplicates()
    opponent_map = df[["opponent", "opponent_id"]].drop_duplicates()
    return team_map, opponent_map

def merge_rivalries(df, rivalries_df): 
    # Convertir en DataFrame
    riv = pd.DataFrame(rivalries_df).copy()
  
    # Normalisation lower case 
    riv["team"] = riv["team"].str.lower()
    riv["opponent"] = riv["opponent"].str.lower()
    # mapping team -> team_id
    team_map, opp_map = build_team_id_map(df)
    team_map["team_lower"] = team_map["team"].str.lower()
    opp_map["opponent_lower"] = opp_map["opponent"].str.lower()

    # transform my df in Dataframe 
    df = pd.DataFrame(df)
    # add team id 
    riv = riv.merge(
        team_map[["team_lower", "team_id"]],
        left_on = "team",
        right_on = "team_lower",
        how = "left"
    )
    # add opponent id 
    riv = riv.merge(
        opp_map[["opponent_lower","opponent_id"]], 
        left_on = "opponent", 
        right_on = "opponent_lower",
        how = "left"
    )

    # final merge on opponent_id and team_id
    df = df.merge(
        riv[["team_id", "opponent_id", "intensity"]], 
        on = ["team_id", "opponent_id"],
        how = "left"
    )
    df["rivalry_pressure"] = df["intensity"].fillna(0)
    df = df.drop(columns = ["intensity"], errors = 'ignore')

    return df 


def merge_media(df, media_df):
    media = pd.DataFrame(media_df).copy()

    # mapping team -> team_id
    team_map, _ = build_team_id_map(df)
    team_map["team_lower"] = team_map["team"].str.lower()

    # add home_team_id
    media["home_team_lower"] = media["home_team"].str.lower()
    media = media.merge(
        team_map[["team_lower", "team_id"]], 
        left_on = "home_team_lower", 
        right_on = "team_lower", 
        how = "left"
    ).rename(columns = {"team_id" : "home_team_id"})

    # add away_team_id
    media["away_team_lower"] = media["away_team"].str.lower()
    media = media.merge(
         team_map[["team_lower", "team_id"]], 
         left_on = "away_team_lower", 
         right_on = "team_lower", 
         how = "left"
    ).rename(columns = {"team_id": "away_team_id"})

    # final merge 
    df = df.merge(
        media[["game_id", "home_team_id", "away_team_id", "prime_time", "national_broadcast"]], 
        on = "game_id",
        how = "left"
    )

    # select the good column according to team_side
    df["media_prime_time"] = df.apply(
        lambda row: row["prime_time"] if row["team_id"] in (row["home_team_id"], row["away_team_id"]) else 0, 
        axis = 1
    )
    df["media_national"] = df.apply(
        lambda row: row["national_broadcast"] if row["team_id"] in  (row["home_team_id"], row["away_team_id"]) else 0,
        axis = 1
    )
    # normalization 
    df["prime_time"] = df["media_prime_time"].fillna(0).astype(int)
    df["national_broadcast"] = df["media_national"].fillna(0).astype(int)

    df = df.drop( columns = ["home_team_id", "away_team_id", "media_prime_time", "media_national"], errors = "ignore")

    return df 

def compute_media_pressure(df): 
    df["media_pressure"] = (
        df["prime_time"]
        + df["national_broadcast"] 
        + ((df["team_rank"] <= 25) & (df["team_rank"] <= 25)).astype(int)
    )
    return df

    # Merge ranking
def merge_rankings(df, rankings_df): 
    rank = pd.DataFrame(rankings_df).copy()
    
    # Team Rank 
    df = df.merge(
        rank.rename(columns = {"school": "team", "rank": "team_rank"})[["season", "week", "team", "team_rank"]], 
        on = ["season", "week", "team"], 
        how = "left"
    )
    # opponent rank 
    df = df.merge(
        rank.rename(columns = {"school": "opponent", "rank": "opponent_rank"})[["season", "week", "opponent", "opponent_rank"]], 
        on = ["season", "week", "opponent"],
        how = "left"
    )
    df["team_rank"] = df["team_rank"].fillna(999)
    df["opponent_rank"] = df["opponent_rank"].fillna(999)
    return df 

def compute_stakes_pressure(df):
    # Pressure related to the g
    # bowl, playoffs, championship 

    df["stakes_pressure"] = 0.0
    df.loc[df["season_type"].str.contains("championship", case = False, na = False), "stakes_pressure"] = 1.0
    df.loc[df["season_type"].str.contains("postseason", case = False, na = False), "stakes_pressure"] = 1.0
    df.loc[df["week"] >= 12,"stakes_pressure"] =  df["stakes_pressure"] + 1.0
    df["stakes_pressure"] = df["stakes_pressure"] + ((df["team_rank"] <= 25) & (df["opponent_rank"] <= 25)).astype(float) 

    df["stakes_pressure"] = df["stakes_pressure"] + df["conference_game"].astype(float)
    df["stakes_pressure"] = df["stakes_pressure"] + df["neutral_site"].astype(float)

    max_val = df["stakes_pressure"].max()
    df["stakes_pressure"] = df["stakes_pressure"] / max_val if max_val > 0 else 0.0
    return df

def compute_psychological_shock(df):
    # psycological pressure based on the previous match: 
    # huge win -> pressure to confirm
    # huge defeat  -> rebound pressure
    # we take the absolute value of the previous margin and divide it by the largest abolute margin of the season
    # of course we gained a result between 0 and 1

    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)

    # Marge du match précédent
    df["prev_margin"] = df.groupby("team_id")["margin"].shift(1)
    # max_abs = df["prev_margin"].abs().max()

    df["psychological_shock"] = df.groupby("team_id")["prev_margin"].transform(lambda x: x.abs()/(x.abs().max() if x.abs().max()else 1))

    # Remplacer le nan du premier match par 0
    df["psychological_shock"] = df["psychological_shock"].fillna(0)

    return df

def compute_pressure_index(df): 

    df["pressure_raw"] = (
         0.20 * df["rivalry_pressure"] + 
         0.20 * df["stakes_pressure"] + 
         0.20  * df["media_pressure"] + 
         0.20 * df["psychological_shock"]+
         0.20 * df["WPI"]
    )

    min_val = df["pressure_raw"].min()
    max_val = df["pressure_raw"].max()

    df["pressure_index"] = df["pressure_raw"] - min_val / (max_val - min_val) if max_val != min_val else 0.0
    return df

def compute_pressure_proxies(df, rivalries_df , media_df, rankings_df ): 
    df = pd.DataFrame(df)
    df = df.sort_values(["team_id", "season", "week"]).reset_index(drop = True)
    df = merge_rivalries(df, rivalries_df)
    df = merge_media(df, media_df)
    df = merge_rankings(df, rankings_df)

    df = compute_stakes_pressure(df)
    df = compute_media_pressure(df)
    df = compute_psychological_shock(df)
    df = compute_pressure_index(df)

    return df

# val = fetch_merge_team()
# valrival = fetch_rivalries()
# valmedia = fetch_media()
# valranking = fetch_rankings()

# parseval = parse_merge_team(val)
# parsevalrival = parse_rivalries(valrival)
# parsemedia = parse_media(valmedia)
# parseranking = parse_rankings(valranking)
# vall = merge_rivalries(parseval, parsevalrival)
# vallmed = merge_media(vall, parsemedia)
# vallrank = merge_rankings(vall, parseranking)
# print(compute_pressure_proxies(parseval, parsevalrival, parsemedia, parseranking))

# if __name__ == "__name__":
# from pipeline.scrapers.cfbd.media import fetch_media
# from pipeline.scrapers.cfbd.rankings import fetch_rankings
# from pipeline.scrapers.cfbd.rivalries import fetch_rivalries
# from pipeline.transformation.cfbd.parse_rankings import parse_rankings
# from pipeline.transformation.cfbd.parse_media import parse_media
# from pipeline.transformation.cfbd.parse_rivalries import parse_rivalries

# valrivalries = fetch_rivalries()
# rivalries_df = parse_rivalries(valrivalries)

# valprime = fetch_media()
# media_df  = parse_media(valprime)

# valranking = fetch_rankings(all)
# rankings_df = parse_rankings(valranking)

# df_with_pressure = compute_pressure_proxies(df, rivalries_df, media_df, rankings_df )
# print(df_with_pressure.head())
