import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_coaching import load_coaching


def parse_coaching(): 
    list_coaching = []
    result_coaching = load_coaching()

    for i in result_coaching: 
        dict_coaching = {
            "team": i["team"],
            "season": int(i["season"]), 
            "head_coach": i["head_coach"], 
            "years_at_school": int(i["years_at_school"]),
            "career_win_pct": float(i["career_win_pct"]), 
            "program_win_pct": float(i["program_win_pct"]), 
            "player_dev_score": float(i["player_dev_score"]),
            "coach_value_score": int(i["coach_value_score"])
        }

        list_coaching.append(dict_coaching)

    return list_coaching