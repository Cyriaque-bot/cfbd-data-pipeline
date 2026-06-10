def compute_wind_impact(df, max_wind = 30): 
    # On clique pour éviterdes valeurs absurdes 
    df["wind_clipped"] = df["wind_speed"].clip(lower = 0, upper = max_wind)
    df["wind_impact"] = df ["wind_clipped"] / max_wind
    return df