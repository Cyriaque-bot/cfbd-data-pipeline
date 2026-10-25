from pathlib import Path
import sys 



project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.derived.conference_strength_cfbd import fetch_conference_strength_cfbd


def parse_conference_strength_cfbd(raw_conference_strength_cfbd): 
    list_raw_conference_strength_cfbd = []

    for i_raw_conference_strength_cfbd in raw_conference_strength_cfbd: 
        dict_raw_conference_strength_cfbd = {
            "season" : i_raw_conference_strength_cfbd["season"], 
            "conference_id" : int(i_raw_conference_strength_cfbd["conference_id"]),
            "conference_name" : i_raw_conference_strength_cfbd["conference_name"], 
            "conference_short_name" : i_raw_conference_strength_cfbd["conference_short_name"], 
            "conference_classification" : i_raw_conference_strength_cfbd["conference_classification"], 
            "team_count" : int(i_raw_conference_strength_cfbd["team_count"]), 
            "avg_sp_overall" : float(i_raw_conference_strength_cfbd["avg_sp_overall"]), 
            "avg_fpi_overall" : float(i_raw_conference_strength_cfbd["avg_fpi_overall"]), 
            "avg_srs" : float(i_raw_conference_strength_cfbd["avg_srs"]), 
            "avg_elo" : float(i_raw_conference_strength_cfbd["avg_elo"]), 
            "avg_off_ppa" : float(i_raw_conference_strength_cfbd["avg_off_ppa"]), 
            "avg_def_ppa" :float(i_raw_conference_strength_cfbd["avg_def_ppa"]), 
            "avg_off_success" : float(i_raw_conference_strength_cfbd["avg_off_success"]), 
            "avg_def_success" : float(i_raw_conference_strength_cfbd["avg_def_success"]), 
            "avg_off_explosiveness" : float(i_raw_conference_strength_cfbd["avg_off_explosiveness"]), 
            "avg_def_explosiveness" : float(i_raw_conference_strength_cfbd["avg_def_explosiveness"]), 
            "conference_avg_win_rate": float(i_raw_conference_strength_cfbd["conference_avg_win_rate"]),
            "conference_strength_raw" : float(i_raw_conference_strength_cfbd["conference_strength_raw"]), 
            "conference_strength_norm" : float(i_raw_conference_strength_cfbd["conference_strength_norm"])
           
        }
        list_raw_conference_strength_cfbd.append(dict_raw_conference_strength_cfbd)

    return list_raw_conference_strength_cfbd

    




# valscrap = fetch_conference_strength_cfbd()
# print(parse_conference_strength_cfbd(valscrap))