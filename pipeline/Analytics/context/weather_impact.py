


def compute_weather_features(df): 

    # On clique pour éviterdes valeurs absurdes 
    # wind 

    df["wind_clipped"] = df["wind_speed"].clip(lower = 0, upper = 30)
    df["wind_impact"] = df ["wind_clipped"] / 30
   
    # Rain 
    df["rain_impact"] = (df["precipitation"] / 5).clip(lower = 0, upper = 30)

    # Temperature 
    df["temperature_impact"] = df["temperature"].apply(
        lambda t : abs(t - 30) / 30 if t != 30 else 0
    ).clip(0, 1)

    # Humidity

    df["humidity_impact"] = df["humidity"] / 100

    # Raw score 

    df["weather_score_raw"] =  (

        0.35 * df["wind_impact"] + 
        0.35 * df["rain_impact"] + 
        0.20 * df["temperature_impact"] + 
        0.10 * df["humidity_impact"]

    )
  
   # Normalized score soi score de difficulté météo 
    df["weather_score_norm"] =  (
        df["weather_score_raw"] -  df["weather_score_raw"].min()
   ) / (df["weather_score_raw"].max() - df["weather_score_raw"].min())
    
    return df 