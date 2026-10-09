from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.team_season_overview import fetch_team_season_overview

def parse_team_season_overview(raw_team_season_overwiew): 
    list_raw_team_season_overwiew = []
    for i_team_season_overwiew in raw_team_season_overwiew: 
        dict_raw_team_season_overwiew = {

            # identity
            "team_id": int(i_team_season_overwiew["teamId"]), 
            "team": i_team_season_overwiew["team"], 
            "season": int(i_team_season_overwiew["season"]), 
            "conference": i_team_season_overwiew["conference"], 
            # record
            "wins": int(i_team_season_overwiew["record"]["wins"]),
            "losses": int(i_team_season_overwiew["record"]["losses"]),
            "ties": int(i_team_season_overwiew["record"]["ties"]),
            "games": int(i_team_season_overwiew["record"]["games"]),
            # rating SP+
            "sp_offense": float(i_team_season_overwiew["ratings"]["sp"]["offense"]["rating"]),
            "sp_defense": float(i_team_season_overwiew["ratings"]["sp"]["defense"]["rating"]),
            "sp_special": float(i_team_season_overwiew["ratings"]["sp"]["specialTeams"]["rating"]),
            "sp_overall": float(i_team_season_overwiew["ratings"]["sp"]["overall"]["rating"]),
            # SRS / ELO
            "srs": float(i_team_season_overwiew["ratings"]["srs"]["rating"]),
            "elo": int(i_team_season_overwiew["ratings"]["elo"]),
            # FPI
            "fpi_offense": float(i_team_season_overwiew["ratings"]["fpi"]["offense"]["rating"]),
            "fpi_defense": float(i_team_season_overwiew["ratings"]["fpi"]["defense"]["rating"]),
            "fpi_special": float(i_team_season_overwiew["ratings"]["fpi"]["specialTeams"]["rating"]),
            "fpi_overall": float(i_team_season_overwiew["ratings"]["fpi"]["overall"]["rating"]),

            # offense

            "off_ppa": float(i_team_season_overwiew["advanced"]["offense"]["ppa"]),
            "off_success": float(i_team_season_overwiew["advanced"]["offense"]["successRate"]),
            "off_explosiveness": float(i_team_season_overwiew["advanced"]["offense"]["explosiveness"]),
            "off_drives": int(i_team_season_overwiew["advanced"]["offense"]["drives"]),
            "off_plays": int(i_team_season_overwiew["advanced"]["offense"]["plays"]),
 
            "off_ppa_pass": float(i_team_season_overwiew["advanced"]["offense"]["passingPlays"]["ppa"]),
            "off_success_pass": float(i_team_season_overwiew["advanced"]["offense"]["passingPlays"]["successRate"]),
            "off_explosiveness_pass": float(i_team_season_overwiew["advanced"]["offense"]["passingPlays"]["explosiveness"]),

            "off_ppa_rush": float(i_team_season_overwiew["advanced"]["offense"]["rushingPlays"]["ppa"]),
            "off_success_rush": float(i_team_season_overwiew["advanced"]["offense"]["rushingPlays"]["successRate"]),
            "off_explosiveness_rush": float(i_team_season_overwiew["advanced"]["offense"]["rushingPlays"]["explosiveness"]),

            # defense

            "def_ppa": float(i_team_season_overwiew["advanced"]["defense"]["ppa"]),
            "def_success": float(i_team_season_overwiew["advanced"]["defense"]["successRate"]),
            "def_explosiveness": float(i_team_season_overwiew["advanced"]["defense"]["explosiveness"]),
            "def_drives": int(i_team_season_overwiew["advanced"]["defense"]["drives"]),
            "def_plays": int(i_team_season_overwiew["advanced"]["defense"]["plays"]),
        
            "def_ppa_pass": float(i_team_season_overwiew["advanced"]["defense"]["passingPlays"]["ppa"]),
            "def_success_pass": float(i_team_season_overwiew["advanced"]["defense"]["passingPlays"]["successRate"]),
            "def_explosiveness_pass": float(i_team_season_overwiew["advanced"]["defense"]["passingPlays"]["explosiveness"]),
    
            "def_ppa_rush": float(i_team_season_overwiew["advanced"]["defense"]["rushingPlays"]["ppa"]),
            "def_success_rush": float(i_team_season_overwiew["advanced"]["defense"]["rushingPlays"]["successRate"]),
            "def_explosiveness_rush": float(i_team_season_overwiew["advanced"]["defense"]["rushingPlays"]["explosiveness"])
        }

        list_raw_team_season_overwiew.append(dict_raw_team_season_overwiew)

    return list_raw_team_season_overwiew





# val  = fetch_team_season_overwiew()
# print(parse_team_season_overwiew(val))