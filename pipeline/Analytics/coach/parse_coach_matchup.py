import pandas as pd 
from pathlib import Path 


######### start load_raw_coach_data #########
def load_raw_coach_data(path: str = "data/raw/coaching.csv")->pd.DataFrame:
    # Charge les données brutes de coaching 
    # Si le fichier n'existe pas encore , lève une erreur claire 

    coach_path = Path(path)

    if not coach_path.exists(): 
        raise FileNotFoundError(f"le fichier brut n'existe pas encore: {coach_path}\n")
    
    df = pd.read_csv(coach_path)
    # les colonnes minimales attendues 
    required_cols = [
        "season", 
        "team", 
        "conference", 
        "head_coach", 
        "head_coach_years_at_school", 
        "head_coach_experience_years", 
        "wins", 
        "losses", 
        "conference_wins", 
        "conference_losses", 
        "top25_wins",
        "top25_losses", 
        "oc_name", 
        "oc_years_at_school",
        "dc_name", 
        "dc_years_at_school", 
        "offense_epa", 
        "defense_epa"
    ]

    missing = [col for col in required_cols if col not in df.columns]
    if missing: 
        raise ValueError(f"missing columns in coaching.csv: {missing}")
    
    return df 
######### end load_raw_coach_data #########

######### start clean_coach_data #########

def clean_coach_data(df: pd.DataFrame)->pd.DataFrame: 
    # Nettoie les données nrutes de coaching: 
    # - normalisation des noms 
    # - gestion des valeures manquantes 
    # - conversion des types 
    # - standardisation des colonnes 

    # 1 Normaliser les noms de colonnes 
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
   
    # 2 Nettoyer les chaines de caractères 
    str_cols = [
        "team", "conference", "head_coach", "oc_name", "dc_name"
    ]

    for col in str_cols:
        if col in df.columns: 
           df[col] = (
               df[col]
               .astype(str)
               .str.strip()
               .str.title() # Alabama ->Alabama, nick saban -> Nick Saban
           )
        
    # 3 Convertir les colonnes Numériques 

    numeric_cols = [
        "season", 
        "head_coach_years_at_school",
        "head_coach_experience_years", 
        "wins", 
        "losses", 
        "conference_wins", 
        "conference_losses", 
        "top25_wins",
        "top25_losses", 
        "oc_years_at_school",
        "dc_years_at_school",
        "offense_epa", 
        "defense_epa"
    ]

    for col in numeric_cols: 
        if col in df.columns: 
            df[col] = pd.to_numeric(df[col], errors = "coerce")
    
    # 4 Gerer les valeurs manquantes 

    df = df.fillna({
        "offense_epa": 0, 
        "defense_epa": 0, 
        "top25_wins": 0, 
        "top25_losses": 0, 
        "conference_wins": 0, 
        "conference_losses": 0, 
        "wins": 0, 
        "losses": 0
    })
 
    # 5 Supprimer les lignes sans coach (rare mais possible)

    df = df[df["head_coach"].notna()]
    
    return df


######### end clean_coach_data #########

######### start structure_coach_season #########

def structure_coach_season(df: pd.DataFrame)->pd.DataFrame:
    # structure les données coaching par équipe et par saison
    # - retourne eb dataframe ou chaque ligne représente : 
    # - une équipe 
    # - une saison
    # - staff complet(HC, OC, DC) 

    # 1. colonnes essentielles 
    required_cols = [
        "season", 
        "team", 
        "conference", 
        "head_coach", 
        "head_coach_years_at_school",
        "head_coach_experience_years",
        "oc_name", 
        "oc_years_at_school",
        "dc_name", 
        "dc_years_at_school",
        "wins", 
        "losses", 
        "conference_wins", 
        "conference_losses", 
        "top25_wins",
        "top25_losses",
        "offense_epa",
        "defence_epa"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing : 
        raise ValueError(f"colonnes manquantes pour structure_coach_season : {missing}")
   
    # 2. Créer un identifant unique team-season 
    df["team_season_id"] = df["team"] + "_" + df["season"].astype(str)

    # 3. Regrouper par équipe + saison 
    grouped = df.groupby(["team", "season", "conference"], as_index = False).agg({
        "head_coach": "first", 
        "head_coach_years_at_school": "first", 
        "head_coach_experience_years": "first", 
        "oc_name": "first", 
        "oc_years_at_school": "first", 
        "dc_name": "first", 
        "dc_years_at_school": "first", 
        "wins": "sum", 
        "losses": "sum", 
        "conference_wins": "sum", 
        "conference_losses": "sum", 
        "top25_wins": "sum", 
        "top25_losses": "sum", 
        "offense_epa": "mean",
        "defence_epa": "mean"
    })

    # 4. Champs dérivés utiles pour l'analyse 
    grouped["games_played"] = grouped["wins"] + grouped["losses"]
    grouped["conference_games"] = grouped["conference_wins"] + grouped["conference_losses"]
    grouped["top25_games"] = grouped["top25_wins"] + grouped["top25_losses"]


    # 5. Retourner un DataFrame
    return grouped
######### end structure_coach_season #########

######### start compute_basic_coach_stats #########
def compute_basic_coach_stats(df: pd.DataFrame)-> pd.DataFrame: 
    # Calcule les statistqiques de base pour chaque équipe 
    # win rate 
    # conference win rate 
    # top25 win rate 
    # offensive & defensiv EPA 
    # coaching stability
    # Experience score

    # 1. Win rate global 
    df["win_rate"] = df["wins"] / df["games_played"]
    df["win_rate"] =  df["win_rate"].fillna(0)

    # 2. Win rate conference
    df["conference_win_rate"] = df["conference_wins"] / df["conference_games"]
    df["conference_win_rate"] = df["conference_win_rate"].fillna(0)

    # 3. Win rate vs top 25
    df["top25_win_rate"] = df["top25_wins"] / df["top25_games"]
    df["top25_win_rate"] = df["top25_win_rate"].fillna(0)

    # 4. EPA offensif et défensif (déjà des moyennes)
    df["offensive_strength"] = df["offense_epa"]
    df["defensive_strength"] = df["defence_epa"]

    # 5. Stabilité du staff(HC + OC + DC)

    df["coaching_stability"] = (
        df["head_coach_years_at_school"] * 0.5 + 
        df["oc_years_at_school"] * 0.25 + 
        df["dc_years_at_school"] * 0.25
    )

    # 6. Score d'expérience du head coach
    df["experience_score"] = df["head_coach_experience_years"]

    return df

######### end compute_basic_coach_stats #########

def build_coach_dataset(path: str = "data/raw/coaching.csv")->pd.DataFrame: 
    # Pipeline complet du module coaching: 
    # - charge les données 
    # - nettoie les données 
    # - structure par équipe + saison
    # - calcul les statistiques de base 
    # - renvoie un dataFrame final prêt pour l'analyse 

    # 1. charger les données brutes 
    df_raw = load_raw_coach_data(path)

    # 2. Nettoyer les données 
    df_clean = clean_coach_data(df_raw)

    # 3. Structurer par équipe + saison 
    df_structured = structure_coach_season(df_clean)

    # 4. calculer les statistiques de base 
    df_final = compute_basic_coach_stats(df_structured)

    return df_final
# version export(optionnelle)

#if __name__ == "__main__":
#    df = build_coach_dataset()
#    df.to_csv("data/processed/coach_dataset.csv", index=False)
#    print("Coach dataset generated successfully.")