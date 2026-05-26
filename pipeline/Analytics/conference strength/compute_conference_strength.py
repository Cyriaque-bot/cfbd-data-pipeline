import json 
from pathlib import Path 
import pandas as pd 

# Fonction 1 chargement de la configuration 
def load_config(path: str)-> dict: 
    # charge un fichier json de configuration et retourne un dictionaire Python.
    # Les arguments path(str): chemin vers le fichier json 
    # return dict: contenu du fichier json.
    config_path = Path(path)

    if not config_path.exists(): 
        raise  FileNotFoundError(f"the configuration file was not found : {path}")
    with open(config_path, "r", encoding = "utf-8") as f:
        return json.load(f)
    
# print(load_config("Y:\\Document Personnel\\BI Microsoft\\CodePython\\Exorepeateone\\Exo Baby names Us\\Georgia Tech\\pipeline\\analytics\\conference strength\\conference_weights.json"))


###################################################################  ##################################################################
                                                          ######### LOAD DATA  #########
###################################################################  ##################################################################
# Fonction 2 chargement de mes données 

########### load_games_data ###########

def load_games_data()-> pd.DataFrame: 
    # charge les données de macths nécessaires au calcul du conference Strength
    # cette fonction ne fait aucun calcul: elle ne fait que charger et structurer les données.
    # returns: pd.DataFrame: dataframe contenant tous les matchs de la saison
    games_path = Path("pipeline/transformation/parse_games.py")
    if not games_path.exists():
        raise FileNotFoundError(f"file not find :{games_path}")
    
    df = pd.read_csv(games_path)
    
    # verification minimale des colonnes nécéssaires
    required_cols = [
        "season", 
        "week", 
        "home_team", 
        "away_team", 
        "home_points", 
        "away_points", 
        "home_conference", 
        "away_conference", 
        "neutral_site", 
        "game_type"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in games.csv : {missing}")
    
    return df

########### load_epa_data ###########

# EPA Expected Point added (mésure l'éfficacitées reelle d'une action)

def load_epa_data()-> pd.DataFrame: 
    # charge les données EPA(offense, defense, special teams)n nécessaires au calculdu conference Strength.
    # cette fonction ne fait aucun calcul : elle ne fait que charger et structurer les données 
    # return pd.Dataframe contenant les les EPA par équipe et par match
    epa_path = Path("data/processed/epa.csv")

    if not epa_path.exists(): 
        raise FileNotFoundError(f"file not find :{epa_path}")
    df = pd.read_csv(epa_path)
    #colonne minimal necessaire pour l'analytique
    required_cols = [
        "team", 
        "conference", 
        "season", 
        "game_id", 
        "epa_offense", 
        "epa_defense", 
        "epa_special", 
        "epa_total"
    ]


    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError( f"missing columns in epa.csv : {missing}")
    
    return df

########### load_recruiting_data ###########

def load_recruiting_data()->pd.DataFrame:
    recruiting_path =  Path("data/processed/recruiting")
    if not recruiting_path.exists(): 
        raise FileNotFoundError(f"file not find : {recruiting_path}")
    df = pd.read_csv(recruiting_path)

    required_cols = [
        "team", 
        "conference", 
        "recruiting_points", 
        "recruiting_rank", 
        "blue_chip_rattio", 
        "five_star", 
        "four_star"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
       raise ValueError(f"missing columns in recruiting.csv : {missing}")
    return df 

  ########### load_nfl_data ###########

def load_nfl_data()->pd.DataFrame: 

    nfl_path = Path("data/processed/nfl.csv")
    if not nfl_path.exists(): 
        raise FileNotFoundError(f"file not find : {nfl_path}")
    df = pd.read_csv(nfl_path)

    required_cols = [
        "team", 
        "conference", 
        "season", 
        "drafted_players", 
        "drafted_round_1", 
        "drafted_round_2", 
        "drafted_round_3",
        "nfl_active_players", 
        "nfl_total_value"
    ]
    
    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in nfl.csv: {missing}")
    return df 

  ########### load_tv_data ###########

def load_tv_data()->pd.DataFrame: 

    tv_path = Path("data/processed/tv.csv")
    if not tv_path.exists(): 
        raise FileNotFoundError(f"file not find : {tv_path}")
    df = pd.read_csv(tv_path)

    required_cols = [
        "team", 
        "conference", 
        "season", 
        "tv_audience_avg", 
        "tv_audience_median", 
        "tv_audience_peak", 
        "tv_games_count", 
        "tv_revenue", 
        "prime_time_games", 
        "national_games"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in tv.csv : {missing}")
    return df

  ########### load_top_25_data ###########

def load_top_25_data()->pd.DataFrame: 
    top25_path = Path("data/processed/top25.csv")
    if not top25_path.exists(): 
        raise FileNotFoundError(f"file not find : {top25_path}")
    df = pd.read_csv(top25_path)

    required_cols = [
        "team", 
        "conference", 
        "season", 
        "ap_rank", 
        "coaches_rank", 
        "weeks_ranked", 
        "weeks_top10", 
        "weeks_top5", 
        "best_rank"
    ]
    
    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
       raise ValueError(f"missing columns in top25.csv : {missing}")

    return df 

  ########### load_coaching_data ###########

def load_coaching_data()->pd.DataFrame:
    coaching_path = Path("data/processed/coaching.csv")
    if not coaching_path:
        raise FileNotFoundError(f"file not find : {coaching_path}")
    df = pd.read_csv(coaching_path)
    
    required_cols = [
        "team", 
        "conference", 
        "season", 
        "head_coach", 
        "head_coach_years", 
        "oc_name", 
        "oc_years", 
        "dc_name", 
        "dc_years",
        "coach_record_wins", 
        "coach_record_losses", 
        "coaching_stability_score"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in coaching.csv : {missing}")
    
    return df 
   
 ########### load_interconference_data ###########
def load_interconference_data()->pd.DataFrame: 
    inter_path = ("data/processed/interconference.csv")
    if not inter_path: 
       raise FileNotFoundError(f"file not find : {inter_path}")
    
    df = pd.read_csv(inter_path)
    required_cols = [
        "season",
        "game_id", 
        "team", 
        "team_conference", 
        "opponent", 
        "opponent_conference", 
        "team_points", 
        "opponent_points", 
        "team_epa", 
        "opponent_epa", 
        "is_power5_opponent", 
        "is_top25_opponent"
    ]
    
    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in interconference.csv : {missing}")
    return df

def load_all_data()->dict: 
    # charges toutes les données nécessaires au calcul du conference Strength.
    # cette fonction ne fait aucun calcul: elle ne fait que charger et structurer les données 
    # return = un dictionnaire contenant toutes les données organisées par catégories.

    data = {
        "games": load_games_data(),                          # résultats des matchs 
        "epa": load_epa_data(),                              # EPA offense/defense/ST
        "recruiting":load_recruiting_data(),                 # talent (4 ans)
        "nfl": load_nfl_data(),                              # draft + joueurs actifs 
        "tv": load_tv_data(),                                # revenus + audiences 
        "top25": load_top_25_data(),                         # AP/Coaches Poll
        "coaching": load_coaching_data(),                    # continuité + résultats
        "interconference": load_interconference_data()       # résultats inter-conférences
    }
    return data 

###################################################################  ##################################################################
                                                         ######### FIN LOAD DATA  #########
###################################################################  ##################################################################


###################################################################  ##################################################################
                                                  ######## COMPUTE CONFERENCE #########
###################################################################  ##################################################################


########### compute_epa_score ###########

def compute_epa_score(epa_df: pd.DataFrame) -> pd.DataFrame: 
    # Calcul un score EPA par conference, combine EPA offense, defense et special teams Normalise les valeurs et retourne un score par conference

    # 1. Epa total par équipe (moyenne par match)
    team_epa = (
        epa_df.groupby(["team", "conference"])["epa_total"]
        .mean()
        .reset_index()
        .rename(columns = {"epa_total": "epa_team"})
    )

    # 2. EPA moyen par conference 
    conf_epa = (
        team_epa.groupby("conference")["epa_team"]
        .mean()
        .reset_index()
        .rename(columns = {"epa_team": "epa_raw"})
    )

    # 3. Normalisation min-max
    min_val = conf_epa["epa_raw"].min()
    max_val = conf_epa["epa_raw"].max()

    conf_epa["epa_score"] = (conf_epa["epa_raw"] - min_val)/(max_val - min_val)

    # 4. Retourner un dataframe propre
    return conf_epa[["conference", "epa_score"]]


########### compute_recruiting_score ###########

def compute_recruiting_score(recruiting_df: pd.DataFrame)->pd.DataFrame:
    # Calcule un scorede talent par conference.combine points 247, blue-chip ratio, 5* et 4* normalise les valeurset retourne un score par conférence

    # 1 . Calcul du talent par équipe
    recruiting_df["talent_score"] = (
        recruiting_df["recruiting_points"] * 0.5 +
        recruiting_df["blue_chip_ratio"] * 0.3 + 
        recruiting_df["five_star"] * 0.15 +
        recruiting_df["four_star"] * 0.05
    )

    # 2 . Talent moyen par conference
    conf_talent = ( 
        recruiting_df.groupby("conference")["talent_score"]
        .mean()
        .reset_index()
        .rename(columns = {"talent_score": "talent_raw"})
        )
    
    # 3. Normalisation min-max
    min_val = conf_talent["talent_raw"].min()
    max_val = conf_talent["talent_raw"].max()

    conf_talent["recruiting_score"] = (conf_talent["talent_raw"] - min_val /(max_val - min_val))

    # 4. Retourner un DataFrame propre 
    return conf_talent[["conference", "recruiting_score"]]


########### compute_nfl_score ###########

def compute_nfl_score(nfl_df: pd.DataFrame)->pd.DataFrame:
    # Calcule un score NFL par conférence.
    # Combine valeur NFL, joueurs draftés et joueurs actifs.
    # Normalise les valeurs et retourne un score par conférence.

    # 1. Score NFL par équipe 
    nfl_df["nfl_score_team"] = (
        nfl_df["nfl_total_value"] * 0.5 + 
        nfl_df["draft_round_1"] * 0.25 + 
        nfl_df["draft_round_2"] * 0.15 + 
        nfl_df["draft_round_3"] * 0.05 + 
        nfl_df["nfl_active_players"] * 0.05
    )

    # 2. Score moyen par conférence
    conf_nfl = (
        nfl_df.groupby("conference")["nfl_score_team"]
        .mean()
        .reset_index()
        .rename(columns = {"nfl_score_team": "nfl_raw"})
    )

    # 3. Normalisation min-max
    min_val = conf_nfl["nfl_raw"].min()
    max_val = conf_nfl["nfl_raw"].max()

    conf_nfl["nfl_score"] = (
        conf_nfl["nfl_raw"] - min_val / ( max_val - min_val)
    )

    # retourner un DataFrame Propre 

    return conf_nfl[["conference", "nfl_score"]]


########### compute_tv_score ###########
def compute_tv_score(tv_df: pd.DataFrame)->pd.DataFrame: 
    # calcule un score TV par conférence.
    # Combine audience, exposition nationale et revenus TV.
    # Normalise les valeurs et retourne un score par conférence.

    # 1. Score TV par équipe
    tv_df["tv_score_team"] = (
        tv_df["tv_audience_avg"] * 0.35 + 
        tv_df["tv_audience_peak"] * 0.25 +
        tv_df["tv_revenue"] * 0.20 + 
        tv_df["national_games"] * 0.10 + 
        tv_df["prime_time_games"] * 0.10
    )
    # 2. Score moyen par conference
    conf_tv = (
        tv_df.groupby("conference")["tv_score_team"]
        .mean()
        .reset_index()
        .rename(columns = {"tv_score_team": "tv_raw"})
    )
    # 3. Normalisation min-max
    min_val = conf_tv["tv_raw"].min()
    max_val = conf_tv["tv_raw"].max() 
    conf_tv["score"] = (conf_tv["tv_raw"] - min_val) / (max_val - min_val)

    # 4. Retourner un DataFrame propre 
    return conf_tv[["conference", "tv_score"]]



########### compute_top25_score ###########

def compute_top25_score(top25_df: pd.DataFrame)->pd.DataFrame:
    # Calcule un score top25 par conference.
    # Combine semaines classées, top 10, top 5, meilleur rang et rang AP.
    # Normalise les valeurs et retourne un score par conference.

    #1. Score Top 25 par équipe 
    top25_df["top25_score_team"] = (
        top25_df["weeks_ranked"] * 0.35 + 
        top25_df["weeks_top10"] * 0.25 +
        top25_df["weeks_top5"] * 0.20 +
        (26 - top25_df["best_rank"]) * 0.15 +
        (26 - top25_df["ap_rank"]) * 0.05
    
    )

    #2. Score moyen par conference 
    conf_top25 = (
        top25_df.groupby("conference")["top25_score_team"]
        .mean()
        .reset_index()
        .rename(columns = {"top25_score_team": "top25_raw"})
    )

    #3. Normalisation  min - max 

    min_val = conf_top25["top25_raw"].min()
    max_val = conf_top25["top25_raw"].max()

    conf_top25["top25_score"] = (
        (conf_top25["top25_raw"] - min_val) /(max_val - min_val)
    )

   #4. Retourner un Dataframepropre 
    return conf_top25[["conference", "top25_score"]]


########### compute_coaching_score ###########
def compute_coaching_score(coach_df: pd.DataFrame)->pd.DataFrame:
    # calcule un score de coaching par conférence 
    # combine win rates , expérience, stabilité et titres 
    # Normalise  les valeurs et retoourne un score par conférence.
    
    # 1. Score coaching par équipe 
    coach_df["coaching_score_team"] = (
        coach_df["career_win_rate"] * 0.35 + 
        coach_df["conference_win_rate"] * 0.25 +
        coach_df["top25_win_rate"] * 0.15 +
        coach_df["coach_years_at_school"] * 0.10 +
        coach_df["coach_experience_years"] * 0.10 +
        coach_df["championships"] * 0.05
    )
    
    #2. Score moyeb par conference 
    conf_coach = (
        coach_df.groupby("conference")["coaching_score_team"]
        .mean()
        .reset_index()
        .rename(columns = {"coaching_score_team": "coaching_raw"})
    )

    #3. Normalisation min-max 
    min_val = conf_coach["coaching_raw"].min()
    max_val = conf_coach["coaching_raw"].max()

    conf_coach["coaching_score"] = (
        (conf_coach["coaching_raw"] - min_val) / (max_val - min_val)
    )
    return conf_coach[["conference", "coaching_score"]]


########### compute_interconference_score ###########
def compute_interconference_score(inter_df: pd.DataFrame)->pd.DataFrame: 
    # Calcule un score interconference par conférence.
    # Combine win rate, victoire vs Power5, victoire vs Top 25 et force des adversaires 
    # Normalise et retourne un score par conférence

    # 1 . Score interconnference par équipe 
    inter_df["inter_score_team"] = (
        inter_df["win_rate_interconference"] * 0.50 +
        inter_df["wins_vs_power5"] * 0.25 + 
        inter_df["wins_vs_top25"] * 0.15 + 
        inter_df["strength_of_opponents"] * 0.10
    )

    # 2 . Score moyen par conference 

    conf_inter = (
        inter_df.groupby("conference")["inter_score_team"]
        .mean()
        .reset_index()
        .rename(columns ={"inter_score_team": "inter_raw"})
    ) 
    
    # 3. Normalisation min-max
    min_val = conf_inter["inter_raw"].min()
    max_val = conf_inter["inter_raw"].max()

    conf_inter["interconference_score"] = (
            (conf_inter["inter_raw"] - min_val) / (max_val - min_val)
    )
    # 4 . Retournons un excellent dataFrame 
    return  conf_inter[["conference", "interconference_score"]]

######################## Conference Strength()###########################

def compute_conference_strength(
        epa_df, 
        recruiting_df, 
        nfl_df, 
        tv_df,
        top25_df,
        coaching_df, 
        inter_df
    ): 
    # fusinne toutes les métriques normalisées pour produire un score finalde force des conférences 

    # 1.fusion progressive sur la colonne 'conference'
    df = epa_df.merge(recruiting_df, on = "conference", how = "left")
    df = df.merge(nfl_df, on = "conference", how = "left")
    df = df.merge(tv_df, on = "conference", how = "left")
    df = df.merge(top25_df, on = "conference", how = "left")
    df = df.merge(coaching_df, on = "conference", how = "left")
    df = df.merge(inter_df, on = "conference", how = "left")

    # 2. Score final pondéré
    df["conference_strength"] = (
        df["epa_score"] * 0.25 +  
        df["recruiting_score"] * 0.20 + 
        df["nfl_score"] * 0.15 + 
        df["tv_score"] * 0.15 +
        df["top25_score"] * 0.15 +
        df["coaching_score"]* 0.05 +
        df["interconference_score"] * 0.05
    )

    # classement final 
    df = df.sort_values ("conference_strength", ascending = False).reset_index(drop = True)
    df["rank"] = df.index + 1

    # 4. retournons un dataframe propre 

    return df[[
        "rank", 
        "conference", 
        "conference_strength", 
        "epa_score", 
        "recruiting_score", 
        "nfl_score", 
        "tv_score",  
        "top25_score", 
        "coaching_score", 
        "interconference_score"
    ]]