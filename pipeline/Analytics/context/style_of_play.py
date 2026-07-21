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
    #Si yardsTotal == 0 (cas réel pour certaines équipes FCS ou blowouts)

    df["run_ratio"] = df.apply(lambda row: row["yardsRushing"] /row["yardsTotal"] if row["yardsTotal"] > 0 else 0, 
                               axis = 1
              ) 


    df["pass_ratio"] = df.apply(lambda row : row["passingYards"] / row["yardsTotal"] if row["yardsTotal"] > 0 else 0, 
                                axis = 1
    ) 

    # Classification simple
    df["run_heavy"] = (df["run_ratio"] > 0.55).astype(int)
    df["pass_heavy"] = (df["pass_ratio"] > 0.55).astype(int)
    df["balanced"] = ((df["run_heavy"] == 0) & (df["pass_heavy"] == 0)).astype(int)


    # third down %

    def compute_pct(x):
        if isinstance(x, dict) and x.get("attempts", 0) > 0: 
            return x["made"] / x["attempts"]
        return 0
    df["thirdDownPct"] = df["thirdDown"].apply(compute_pct) if "thirdDown" in df.columns else 0
    df["fourthDownPct"] = df["fourthDown"].apply(compute_pct) if "fourthDown" in df.columns else 0

    df["thirdDownPct"] = df["thirdDownPct"].fillna(0)
    df["fourthDownPct"] = df["fourthDownPct"].fillna(0)

    # -----------------------------
    # Style score 
    # -----------------------------

    # Score simple, robuste , compatible avec build_context_features
    # combinaison de run_ratio (style de jeu), pass_ratio (style de jeu) , thirdDownPct (efficacité)
    df["style_score"] = (
         df["run_ratio"] * 0.4 + 
         df["pass_ratio"] * 0.4 + 
         df["thirdDownPct"] * 0.2
    )

    return df
    # Colonne Finale 

   

# from pipeline.scrapers.teams_stat import fetch_teams_stat
# from pipeline.transformation.parse_team_stats import parse_team_stats
# raw = fetch_teams_stat(all)
# rawparse = parse_team_stats(raw)
# valdatafra = pd.DataFrame(rawparse)
# print(compute_style_of_play(valdatafra))