

def compute_schedule_difficulty(df):
    # Score coming from the strenght of the opponent conference 
    # opponent_conference_strength_win_rate ->  C’est le taux de victoire moyen des équipes de la conférence de l’adversaire
    # opponent_conference_strength_margin -> C’est la marge moyenne de victoire/défaite des équipes de la conférence de l’adversaire.
    df["schedule_difficulty"] = (
        0.5 * df["opponent_conference_strength_win_rate"] + 0.5 * df["opponent_conference_strength_margin"]
    )

    # Normalisation  min - max 
    min_val = df["schedule_difficulty"].min()
    max_val = df["schedule_difficulty"].max()

    df["schedule_difficulty_norm"] = (
        (df["schedule_difficulty"] - min_val)/ (max_val - min_val)
    ).fillna(0)

    return df

    # rolling on the last three matchs 
def compute_schedule_difficulty_rolling(df, window = 3): 
    # sorting all games 
    df = df.sort_values(by = ["team_id", "season", "week"]).reset_index(drop = True)

    # Rolling coming from the normalizing values
    df["schedule_difficulty_rolling_3"] = (
        df.groupby("team")["schedule_difficulty_norm"]
        .rolling(window = window, min_periods = 1)
        .mean()
        .reset_index(level = 0, drop = True)
    )

    # Normalisation min - max 
    min_val = df["schedule_difficulty_rolling_3"].min()
    max_val = df["schedule_difficulty_rolling_3"].max()

    df ["schedule_difficulty_rolling_3_norm"] = (
        (df["schedule_difficulty_rolling_3"] - min_val)/ (max_val - min_val)
    ).fillna(0)

    return df

# weighted rolling (more recent = more important)
def compute_schedule_difficulty_weighted(df): 
    df = df.sort_values(by = ["team_id", "season", "week"]).reset_index(drop = True)

    # Poids : plus réçent = plus important 
    weights = [1, 2, 3]
    def weighted_last_3(values): 
        # values = array des 3 derniers schedule_difficulty_norm
        wval = weights[-len(values):] # ajuste si moins de 3 matchs 
        
        return(values * wval).sum()/ sum(wval)
    
    df["schedule_difficulty_weighted_3"] = (
        df.groupby("team_id")["schedule_difficulty_norm"]
        .rolling(3, min_periods = 1)
        .apply(weighted_last_3, raw = True)
        .reset_index(level = 0, drop = True) 
       )

    # Normalisation min - max 
    min_val = df["schedule_difficulty_weighted_3"].min()
    max_val = df["schedule_difficulty_weighted_3"].max()

    df["schedule_difficulty_weighted_3_norm"] = (
        (df["schedule_difficulty_weighted_3"] - min_val) / (max_val - min_val)
    ).fillna(0)
    return df 