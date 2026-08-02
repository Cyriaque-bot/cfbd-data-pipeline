import os
import sys 
import pandas as pd 

# add project_root to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

############## Conference BI #################

def parse_conference_matchup_bi (raw_games, team_to_conf): 
    listrawval = []

    for i in raw_games: 
        #1 retrieve all teams 
        home = i["home_team"]
        away = i["away_team"]

        #2 retrieve all conferences
        home_conf = team_to_conf.get(home)
        away_conf = team_to_conf.get(away)

        # if a conference is unknown , we ignore the game 
        if home_conf is None or away_conf is None:
            continue

        #filtered an keep the game coming from differents conference
        if home_conf == away_conf: 
            continue
        #4 Determined winner/loser 
        if i["home_points"] > i["away_points"]:
            winnerconf = home_conf
            loserconf = away_conf
        else: 
            winnerconf = away_conf
            loserconf = home_conf

        #5 Derived Fields 
        margin = abs(i["home_points"] - i["away_points"])
        notes = i.get("notes", "")

        is_playoff_game = (
            i["season_type"] == "postseason"
            and isinstance(notes, str) and "CFP" in notes
        )
   
        is_bowl_game = (
            i["season_type"] == "postseason"
            and not is_playoff_game
        )

        #6 building the lastobject
        valdictrawvalone = {
            "season": i["season"], 
            "week": i["week"],
            "season_type": i["season_type"],
            "game_id": i["id"], 
            "home_team": home, 
            "away_team": away, 
            "home_conference": home_conf, 
            "away_conference": away_conf,
            "home_point": i["home_points"], 
            "away_point": i["away_points"], 
            "winner_conference": winnerconf, 
            "loser_conference": loserconf, 
            "margin": margin,
            "neutral_site": i["neutral_site"],
            "is_playoff_game": is_playoff_game, 
            "is_bowl_game": is_bowl_game
        }
        listrawval.append(valdictrawvalone)
                
    return listrawval


############# End Conference BI ################


def compute_conference_strength(df: pd.DataFrame)->pd.DataFrame: 
    # Calcule de la force de chaque conférence en utilisant Opponent STrength 
    conference_strength = df.groupby("team_conference").agg({
        "opponent_win_rate": "mean", 
        "opponent_avg_margin": "mean"
    }).reset_index()
    conference_strength = conference_strength.rename(columns = {
        "team_conference": "conference",
        "opponent_win_rate": "conference_avg_opponent_win_rate", 
        "opponent_avg_margin": "conference_avg_opponent_margin"
    })
    return conference_strength


def add_conference_strength(df: pd.DataFrame, conference_strength_df: pd.DataFrame)->pd.DataFrame: 
    # Ajoute la force de la conférence de l'équipe Et de la conférence de l'adversaire.

    # Force de la conférence de l'équipe 
    merged = df.merge(
        conference_strength_df, 
        left_on = "team_conference", 
        right_on = "conference", 
        how = "left"
    ).drop(columns = ["conference"])

    merged = merged.rename(columns = {
    "conference_avg_opponent_win_rate":"team_conference_strength_win_rate", 
    "conference_avg_opponent_margin": "team_conference_strength_margin"
    })

    merged = merged.merge(
        conference_strength_df,
        left_on="opponent_conference",
        right_on="conference",
        how="left"
    ).drop(columns=["conference"])

    merged = merged.rename(columns = {
        "conference_avg_opponent_win_rate": "opponent_conference_strength_win_rate",
        "conference_avg_opponent_margin": "opponent_conference_strength_margin"
    })

    return merged

# pour qu'il puisse récupérer ma conference et toutes les colonnes associées.

def parse_conference_strength(df_team_matchup: pd.DataFrame)-> pd.DataFrame: 
    # pipeline complet:
    # calcule confererence strength 
    # ajoute conference strength à chaque ligne

    conference_strength_df =  compute_conference_strength(df_team_matchup)
    final_df = add_conference_strength(df_team_matchup, conference_strength_df)

    return final_df




# from pipeline.scrapers.conference import fetch_conference
# from pipeline.scrapers.teams_matchups import fetch_load_team
# from pipeline.transformation.parse_team_matchup import parse_team_matchup
# valresult = fetch_load_team()
# valteammatchup = parse_team_matchup(valresult)
# print(parse_conference_strength(valteammatchup))
# valresulttwo = fetch_conference(all)
# print(type(valresulttwo))
# valresulttwo_df = pd.DataFrame(valresulttwo)


