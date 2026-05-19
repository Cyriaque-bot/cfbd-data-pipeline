import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)

from datetime import datetime
from pipeline.Analytics.anal_coach_season import analyze_coach_season

def compare_coaches(coachA, coachB):
    """
    compare two coachs one a same season.
    coachA and coachB are the output of parse_coach_matchup 
    """

    # Overall summary 
    summaryA = analyze_coach_season(coachA)  
    summaryB = analyze_coach_season(coachB)

    # === Pro feature 1 : Comparison Table ===
    comparison_table = {
        "win_rate":{
            "coachA": summaryA["win_rate"], 
            "coachB": summaryB["win_rate"], 
        }, 
        "points_for_avg":{
            "coachA": summaryA["points_for_avg"],
            "coachB": summaryB["points_for_avg"]
        }, 
        "points_against_avg":{
            "coachA": summaryA["points_against_avg"], 
            "coachB": summaryB["points_against_avg"]
        }, 
        "points_diff_avg":{
            "coachA": summaryA["points_diff_avg"],
            "coachB": summaryB["points_diff_avg"]
        }, 
        "record_home":{
            "coachA": summaryA["record_home"],
            "coachB": summaryB["record_home"]
        }, 
        "record_away":{
            "coachA": summaryA["record_away"],
            "coachB": summaryB["record_away"]
        },
        "biggest_win_diff":{
            "coachA": summaryA["biggest_win"]["diff"] if summaryA["biggest_win"] else None,
            "coachB": summaryB["biggest_win"]["diff"] if summaryB["biggest_win"] else None
        }, 
         "biggest_loss_diff":{
            "coachA": summaryA["biggest_loss"]["diff"] if summaryA["biggest_loss"] else None,
            "coachB": summaryB["biggest_loss"]["diff"] if summaryB["biggest_loss"] else None
        }

    }

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
    
    common_opponents_analysis = {}

    
    for opp in common_opponents: 
        #coach A stats
        gamesA = [g for g in coachA["games"] if g["opponent"] == opp]
        pfA = sum(g["points_for"] for g in gamesA)
        paA = sum(g["points_against"] for g in gamesA) 
        diffA = pfA - paA
        avg_diffA = diffA / len(gamesA) if gamesA else 0
      
        #coach A stats
        gamesB = [g for g in coachB["games"] if g["opponent"] == opp]
        pfB = sum(g["points_for"] for g in gamesB)
        paB = sum(g["points_against"] for g in gamesB) 
        diffB = pfB - paB
        avg_diffB = diffB / len(gamesB) if gamesB else 0

        common_opponents_analysis[opp] = {
            "coachA":{
                "games": len(gamesA), 
                "points_for": pfA, 
                "points_against": paA, 
                "diff_total": diffA, 
                "diff_avg": avg_diffA
            }, 
            "coachB":{
                "games": len(gamesB), 
                "points_for": pfB, 
                "points_against": paB, 
                "diff_total": diffB, 
                "diff_avg": avg_diffB
            }, 
        }

# Analyse Pro home /Away
    def compute_location_stats(coach_games, location): 
        games = [i for i in coach_games if i["location"] == location]
        if not games: 
            return {"games": 0, "points_for": 0, "points_against": 0, "diff_avg": 0}
        
        pf = sum(i["points_for"] for i in  games)
        pa = sum(i["points_against"] for i in games)
        diff_avg = (pf - pa)/ len(games)

        return {
            "games": len(games),
            "points_for": pf, 
            "points_against": pa,
            "diff_avg": diff_avg
        }
    homeA = compute_location_stats(coachA["games"], "home")
    awayA = compute_location_stats(coachA["games"], "away")
    homeB = compute_location_stats(coachB["games"], "home")
    awayB = compute_location_stats(coachB["games"], "away")

    home_away_analysis = {
        "home": {"coachA": homeA, "coachB": homeB}, 
        "away": {"coachA": awayA, "coachB": awayB}
    }
 
# Conference-Level advanced analysis

    All_conferences = set(summaryA["record_by_conference"].keys()) | set(summaryB["record_by_conference"].keys())

    conference_analysis = {}

    for conf in All_conferences:
        # coach A
        gamesA = [i for i in coachA["games"] if i["opponent_conference"] == conf]
        pfA = sum(i["points_for"] for i in gamesA)
        paA = sum(i["points_against"] for i in gamesA)
        diffA = pfA - paA
        avgA = diffA/ len(gamesA) if gamesA else  0

        #coach B 
        gamesB = [i for i  in coachB["games"] if i["opponent_conference"] == conf]
        pfB = sum(i["points_for"] for i in gamesB)
        paB = sum(i["points_against"] for i in gamesB)
        diffB = pfB - paB
        avgB = diffB/ len(gamesB) if gamesB else  0

        conference_analysis[conf] = {
            "coachA": {
                "games": len(gamesA), 
                "points_for": pfA,
                "points_against": paA,
                "diff_total": diffA,
                "diff_Avg": avgA
            }, 

            "coachB": {
                "games": len(gamesB), 
                "points_for": pfB,
                "points_against": paB,
                "diff_total": diffB,
                "diff_Avg": avgB
            }
        }


    def compute_final_score(summary, common_analysis, home_away, conf_analysis): 
        # win_rate
        score_win_rate = summary["win_rate"] * 20

        # Diff avg 
        score_diff_avg = max(0, min(20, (summary["points_diff_avg"]/20)*20))

        # common opponents
        diff_total_common = sum(v["coachA"]["diff_total"] + v["coachB"]["diff_total"] for v in common_analysis.values())
        diff_avg_common = sum(v["coachA"]["diff_avg"] + v["coachB"]["diff_avg"] for v in common_analysis.values())
        score_common = max(0, min(20, (diff_total_common + diff_avg_common)/5))

        # Home/ Away 
        diff_home = home_away["home"]["points_for"] - home_away["home"]["points_against"]
        diff_away = home_away["away"]["points_for"] - home_away["away"]["points_against"]
        score_home_away = max(0, min(20, (diff_home + diff_away)/5))

        # Conference 
        diff_conf = sum(v["coachA"]["diff_total"] + v["coachA"]["diff_total"] for v in conf_analysis.values())
        score_conf = max(0, min(20, diff_conf / 10))

        return round(score_win_rate + score_diff_avg + score_common + score_home_away + score_conf, 2)
    
    # final_scoreA = compute_final_score(summaryA, common_opponents_analysis, home_away_analysis["coachA"],conference_analysis)
    # final_scoreB = compute_final_score(summaryB, common_opponents_analysis, home_away_analysis["coachB"],conference_analysis)
    final_scoreA = compute_final_score(
                   summaryA, 
                   common_opponents_analysis, 
                   {
                       "home": home_away_analysis["home"]["coachA"], 
                       "away": home_away_analysis["away"]["coachA"]
                   }, 
                   conference_analysis
                                       )
    
    final_scoreB = compute_final_score(
                   summaryB, 
                   common_opponents_analysis, 
                   {
                       "home": home_away_analysis["home"]["coachB"], 
                       "away": home_away_analysis["away"]["coachB"]
                   }, 
                   conference_analysis
                                       )

    final_score = {
        "coachA": final_scoreA, 
        "coachB": final_scoreB
    }
    
    # ce return n'est pas vendable dans la mésure ou il n'est pas 
    # - pas hiérarchisé, par normalisé , pas API-ready, pas multi-sport, pas produit SaaS, pas portfolio premimum
    # - Notre transformation en structure entreprise c'est à dire propre, hiérarchique , stable, extensible vendable ,
    #  compatible API compatible dashboard

    # return {
    #     "coachA": summaryA, 
    #     "coachB": summaryB, 
    #     "comparison_table": comparison_table, 
    #     "common_opponents": common_details, 
    #     "common_opponents_analysis": common_opponents_analysis, 
    #     "home_away_analysis": home_away_analysis, 
    #     "conference_analysis": conference_analysis,
    #     "final_score": final_score
    # }

    # Now this is our final result 
    return {
        "metadata":{
            "season":summaryA["season"], 
            "comparison_type": "coach_vs_coach", 
            "generated_at": datetime.now().isoformat()
        }, 
        "coachA": {
            "profile":{
                "coach": summaryA["coach"],
                "team": summaryA["team"]
            }, 
            "season_summary": summaryA
        }, 
        "coachB": {
            "profile": {
                "coach":summaryB["coach"],
                "team": summaryB["team"]
            }, 
            "season_summary": summaryB
        }, 
        "comparison": {
            "global_metrics": comparison_table, 
            "common_opponents": {
                "summary": common_details, 
                "detailed_analysis": common_opponents_analysis
            }, 
         "advanced_analysis": {
             "home_away": home_away_analysis, 
             "conference": conference_analysis
         }
        }, 
        "final_score":{
            "coachA": final_scoreA,
            "coachB": final_scoreB, 
            "winner": summaryA["coach"] if final_scoreA > final_scoreB else summaryB["coach"]
        }
    }

from pipeline.loaders.load_coaches import loads_coaches
from pipeline.loaders.load_games import load_games
from pipeline.loaders.load_conference import load_conference
rawmachupcoach = loads_coaches()
rawmachupgames = load_games()
rawmachupconf = load_conference()
from pipeline.transformation.parse_coach_matchup import parse_coach_matchup
parsed = parse_coach_matchup(rawmachupcoach, rawmachupgames, rawmachupconf)
print(compare_coaches(parsed[0], parsed[1]))