import sys
import os 
import pandas as pd 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def compute_style_of_play(df_team_stats): 
    # detemine style de jeu d'une équipe à partir des stats disponibles dans le parse_team_stats (version simplifié,sans advanced stats)
    #colonnes nécessaires : 
    #  - yardsRushing 
    #  - passingYards
    #  - yardsTotal
    # colonne optionnelles si présente 
    #  - thirdown (dict)
    #  - fourthdown (dict)
    # Retourne un DataFrame avec les colonnes : 
    #  - run_ratio
    #  - pass_ratio
    #  - run_heavy
    #  - pass_heavy
    #  - balanced
    #  - thirdDownPct (si possible) 
    #  - fourthDownPct (si possible)


    df = df_team_stats.copy()
    # Ratios run / pass
    df["run_ratio"] = df["yardsRushing"] / df["yardsTotal"]
    df["pass_ratio"] = df["passingYards"] / df["yardsTotal"]

    # Classification simple
    df["run_heavy"] = (df["run_ratio"] > 0.55).astype(int)
    df["pass_heavy"] = (df["pass_ratio"] > 0.55).astype(int)
    df["balanced"] = ((df["run_heavy"] == 0) & (df["pass_heavy"] == 0)).astype(int)


    # third down %

    def compute_pct(x):
        if isinstance(x, dict) and x.get("attempts", 0) > 0: 
            return x["made"] / x["attempts"]
        return None

    df["thirdDownPct"] = df["thirdDown"].apply(compute_pct) if "thirdDown" in df.columns else None
    df["fourthDownPct"] = df["fourthDown"].apply(compute_pct) if "fourthDown" in df.columns else None
    # Colonne Finale 

    cols = [
        "gameId", "teamId", "team", "conference", "run_ratio", "pass_ratio", 
        "run_heavy", "pass_heavy", "balanced", "thirdDownPct", "fourthDownPct"
    ]
    cols = [c for c in cols if c in df.columns]

    return df[cols]


from pipeline.scrapers.teams_stat import fetch_teams_stat
from pipeline.transformation.parse_team_stats import parse_team_stats
raw = fetch_teams_stat(all)
rawparse = parse_team_stats(raw)
valdatafra = pd.DataFrame(rawparse)
print(compute_style_of_play(valdatafra))