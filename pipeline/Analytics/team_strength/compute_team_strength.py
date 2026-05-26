import pandas as pd 
import json

def compute_team_strength(team_df, features_path, weights_path): 
    # Calcule un score de force par équipe 
    # Combine EPA, Advanced stats et returning production.

    # 1.  charger features et poids 
    with open(features_path, "r") as f : 
        features = json.load(f)

    with open(weights_path, "r") as f : 
        weights = json.load(f)
 
    # 2. Initialiser un score vide(série pandas)
    score = pd.Series(0, index = team_df.index)
    # 3. Score par équipe 
   
    for feat, enabled in features.items(): 
        if enabled: 
            if feat not in team_df.columns:
                raise ValueError(f"Feature '{feat}' not found in team_df ")
            score = score + team_df[feat] * weights[feat]
    team_df["team_strength"] = score

    # 3. Normalisation  min-max 
    min_val = team_df["team_strength"].min()
    max_val = team_df["team_strength"].max()

    team_df["team_strength_norm"] = (
        (team_df["team_strength"] - min_val) / (max_val - min_val)
    )

    return team_df[["team", "conference", "team_strength_norm"]]