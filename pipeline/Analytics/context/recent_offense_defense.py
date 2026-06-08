def compute_recent_points_for(df, window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df["recent_points_for"] = (
        df.groupby("team")["points_for"]
        .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df

def compute_recent_points_against(df, window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df["recent_points_against"] = ( 
        df.groupby("team")["points_against"]
          .transform(lambda x : x.rolling(window, min_periods = 1).mean())
    )
    return df 


def compute_recent_offense_defense(df , window = 3): 
    df = df.sort_values(["team", "season", "week"]).reset_index(drop = True)

    df = compute_recent_points_for(df, window = window)
    df = compute_recent_points_against(df, window = window)

    return df 