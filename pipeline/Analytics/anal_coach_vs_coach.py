import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)


from pipeline.Analytics.anal_coach_season import analyze_coach_season

def compare_coaches(coachA, coachB):
    """
    compare two coachs one a same season.
    coachA and coachB are the output of parse_coach_matchup 
    """

    # Overall summary 
    summaryA = analyze_coach_season(coachA)  
    summaryB = analyze_coach_season(coachB)

    # Opponents Sets 
    oppA = set(summaryA["opponents_summary"].keys())
    oppB = set(summaryB["opponents_summary"].keys())

    common_opponents = oppA.intersection(oppB)

    common_details = {}
    for opp in common_opponents: 
        common_details[opp] = {
            "coachA": summaryA["opponents_summary"][opp], 
            "coachB": summaryB["opponents_summary"][opp]
        }

    return {
        "coachA": summaryA, 
        "coachB": summaryB, 
        "common_opponents": common_details
    }
