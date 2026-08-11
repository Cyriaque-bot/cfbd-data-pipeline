import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.coach_rating import fetch_coach_rating
from pipeline.transformation.derived.parse_coaching_rating import parse_coaching_rating


def compute_coach_rating(raw_coaching_list): 
    list_compute_coach_rating = []
    for i_compute_coach_rating in raw_coaching_list: 
       

        dict_compute_coach_rating = {
            "school": i_compute_coach_rating["school"], 
            "season": i_compute_coach_rating["season"], 
            "win_percentage": i_compute_coach_rating["wins"] / i_compute_coach_rating["games"], 
            "career_win_percentage": i_compute_coach_rating["career_wins"]/ (i_compute_coach_rating["career_wins"] + i_compute_coach_rating["career_losses"]),
            "conference_score":i_compute_coach_rating["conference_wins"] - i_compute_coach_rating["conference_losses"], 
            "bowl_score": i_compute_coach_rating["bowl_wins"] - i_compute_coach_rating["bowl_losses"], 
            "coach_rating": None 
        }

        # normalizing conference and bowl
        conference_score_normalized = (
                    dict_compute_coach_rating["conference_score"] - max(dict_compute_coach_rating["conference_score"])/
                    max(dict_compute_coach_rating["conference_score"]) - min(dict_compute_coach_rating["conference_score"])
        )

        bowl_score_normalized = (
                                  dict_compute_coach_rating["bowl_score"] - max(dict_compute_coach_rating["bowl_score"])/
                                  max(dict_compute_coach_rating["bowl_score"]) - min(dict_compute_coach_rating["bowl_score"])
        )

        # calculate coach_rating 
      
        coach_rating = (
                        0.45 * dict_compute_coach_rating["win_percentage"]  
                        + 0.30 * dict_compute_coach_rating["career_win_percentage"] 
                        + 0.15 * conference_score_normalized
                        + 0.10 * bowl_score_normalized 
                        # + 0.10 * dict_compute_coach_rating["stability_factor"] for later to improve  my modele
                        )

        # add coach_rating value in dict_compute_coach_rating
        dict_compute_coach_rating["coach_rating"] = coach_rating

        # add dict_compute_coach_rating in list_compute_coach_rating

        list_compute_coach_rating.append(dict_compute_coach_rating)

    return list_compute_coach_rating



vallfetc = fetch_coach_rating()
valparse = parse_coaching_rating(vallfetc)
print(compute_coach_rating(valparse))
