import pandas as pd
from parse_coach_matchup import build_coach_dataset
from anal_coach_season import analyze_coach_season
from anal_coach_vs_coach import analyze_coach_vs_coach

# Etape 1 - Fonction utilitaire: récupérer la ligne d'un coach

def get_coach_season_row(df: pd.DataFrame, coach_name: str, season: int)->dict: 
    # retourne une ligne correspondante à un coach pour une saison donnée.
    row = df[(df["head_coach"] == coach_name) & (df["season"] == season)]
    if row.empty:
        raise ValueError(f"Aucune données trouvée pour {coach_name} en {season}")
    return row.iloc[0].to_dict()

# Etape 2 fonction principale

def coach_matchup(coachA_name: str , coachB_name: str, season: int)->dict:
    # comparer les deux coachs pour une saison donnée

    # 1. Charger le dataset final 
    df = build_coach_dataset()

    # 2. Extraires les lignes des deux coachs 
    rowA = get_coach_season_row(df, coachA_name, season)
    rowB = get_coach_season_row(df, coachB_name, season)

    # 3. Générer les rapports individuels 
    reportA = analyze_coach_season(rowA)
    reportB = analyze_coach_season(rowB)

    # 4. Comparer les deux coaches 
    comparisons =  analyze_coach_vs_coach(reportA, reportB)

    # 5. Retournons  le rapport final 
    return {
        "season": season, 
        "coachA_report": reportA, 
        "coachB_report": reportB, 
        "comparison": comparisons
    }

# exemple d'utilisation 

# if __name__ == "__main__":
#     result = coach_matchup("Nick Saban", "Kirby Smart", 2021)
#     print(result["summary"])