import pandas as pd 

# Fonction principal 

def analyze_coach_season(row: dict)-> dict: 
    # Analyse complète d'un coach sur une saison données.
    # row = une ligne du dataset final (team + season + stats) 

    # Véreifiacation minimale 
    required = [
        "team", 
        "season", 
        "conference", 
        "head_coach", 
        "win_rate", 
        "conference_win_rate", 
        "top25_win_rate", 
        "offensive_strength", 
        "defensive_strength", 
        "coaching_stability", 
        "experience_score"
    ]  

    for col in required: 
        if col not in row : 
            raise ValueError(f"Missing column in analyze_coach_season: {col}")
        

    # 2 extraction des infos
    team = row["team"]
    season = row["season"]
    coach = row["head_coach"]

    win_rate = row["win_rate"]
    conf_rate = row["conference_win_rate"]
    top25_rate = row["top25_win_rate"]

    off = row["offensive_strength"]
    deff = row["defensive_strength"]

    stability = row["coaching_stability"]
    experience = row["experience_score"]

    # 3. points forts 
    strengths = []
    if win_rate > 0.65: 
        strengths.append("Excellent Win Rate")

    if conf_rate > 0.65:
        strengths.append("Strong conference performance")
    
    if top25_rate > 0.40:
        strengths.append("Competitive vs Top 25 Teams")

    if off > 0: 
        strengths.append("Positive offensive EPA")

    if deff > 0: 
        strengths.append("Positive defensive EPA")
    
    if stability > 3: 
        strengths.append("Stable coaching staff")

    # 4. Points faibles 
    weaknesses = []

    if win_rate < 0.40: 
        weaknesses.append("Low Win Rate")

    if conf_rate < 0.40:
        weaknesses.append("weak conference performance")
    
    if top25_rate < 0.20:
        weaknesses.append("Struggles vs Top 25 Teams")

    if off < 0: 
        weaknesses.append("Negative offensive EPA")

    if deff > 0: 
        weaknesses.append("Negative defensive EPA")
    
    if stability < 1: 
        weaknesses.append("Unstable coaching staff")

    # 5. Résume 
    summary = (
        f"{coach} coached {team} in {season}. "
        f"The team had a win rate of {win_rate:.2f}, "
        f"a conference win rate of {conf_rate:.2f}, "
        f"and a top 25 win rate of {top25_rate:.2f}. "
        f"offensive EPA: {off:.2f}, Defensive EPA: {deff:.2f}. "
        f"Coaching stability score: {stability:.1f}."
    )

    #6. Rapport final 

    return {
        "team" : team, 
        "season": season, 
        "summary": summary, 
        "strengths": strengths, 
        "weaknesses": weaknesses, 
        "metrics":{
            "win_rate":win_rate, 
            "conference_win_rate":conf_rate, 
            "top25_win_rate": top25_rate, 
            "offensive_strength": off, 
            "defensive_strength": deff, 
            "coaching_stability": stability, 
            "experience_score": experience
        }
    }