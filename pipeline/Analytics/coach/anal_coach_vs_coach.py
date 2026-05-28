def analyze_coach_vs_coach(coachA: dict, coachB: dict)->dict: 
    # Comparer deux coachs sur une saison
    # CoachA et coachB sont les sorties de analyze_coach_season()

    # 1. Extraction des infos 
    nameA = coachA["coachA"]
    nameB = coachB["coachB"]

    metricsA = coachA["metrics"]
    metricsB = coachB["metrics"]

    # 2. Comparaison metrique par metrique 
    comparison = {}
    for key in metricsA:
        comparison[key] = {
            "coachA": metricsA[key],
            "coachB": metricsB[key], 
            "avantage": (
                "A" if metricsA[key] > metricsB[key]
                else "B" if metricsB[key] > metricsA[key]
                else "equal"
            )
        }
    
    # 3. Avantages globaux
    advantages = {
        "coachA": sum(1 for k in comparison if comparison[k]["advantage"] == "A"), 
        "coachB": sum(1 for k in comparison if comparison[k]["advantage"] == "B"),
        "equal": sum(1 for k in comparison if comparison[k]["advantage"] == "equal")
    }

    # 4. Résumé textuel
    if advantages["coachA"] > advantages["coachB"]:
        summary = f"{nameA} shows stronger overall metrics than {nameB}."
    elif advantages["coachB"] > advantages["coachA"]:
        summary = f"{nameB} shows stronger overall metrics than {nameA}."
    else:
        summary = f"{nameA} and {nameB} are evenly matched based on available metrics"

    return {
        "coachA": nameA, 
        "coachB": nameB, 
        "comparison": comparison, 
        "advantages": advantages, 
        "summary": summary, 
        "strengthsA": coachA["strengths"], 
        "strengthsB": coachB["strengths"], 
        "weaknessesA": coachA["weaknessesA"], 
        "weaknessesB": coachB["weaknessesB"]
    }