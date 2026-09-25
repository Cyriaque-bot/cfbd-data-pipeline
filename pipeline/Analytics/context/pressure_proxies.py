import pandas as pd 
from pathlib import Path 
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def merge_rivalries(df, rivalries_list): 
    # Convertir en DataFrame
    riv = pd.DataFrame(rivalries_list).copy()
    # riv = rivalries_json.copy()

    # Normalisation lower case 
    riv["team"] = riv["team"].str.lower()
    riv["opponent"] = riv["opponent"].str.lower()

    # Definition d'une intensité par défaut
    major = ["Iron Bowl", "Red River", "The Game", "Army-Navy"]
    medium = ["Jeweled Shillelagh", "Civil War", "Sunshine Showdown"]
    minor = ["Egg Bowl", "Palmetto Bowl"]

    riv["intensity"] = 0.0 # default value

    riv.loc[riv["rivalrie_name"].isin(major), "intensity"] = 1.0
    riv.loc[riv["rivalrie_name"].isin(medium), "intensity"] = 0.7
    riv.loc[riv["rivalrie_name"].isin(minor), "intensity"] = 0.4

    # Normalisation des équipes dans df
    df["team_lower"] = df["team"].str.lower()
    df["team_opponent"] = df["opponent"].str.lower()

    # Merge direct (team vs opponent)
    df = df.merge(
        riv.rename(columns = {"team": "team_lower", "opponent": "team_opponent", "intensity": "rivalry_pressure"}), 
        on = ["team_lower", "team_opponent"], 
        how = "left"
    )
    # Merge inverse (opponent vs team)
    rev_inv = riv.rename(columns = {"team": "team_opponent", "opponent": "team_lower", "intensity": "rivalry_pressure_inv"})
    df = df.merge(
        rev_inv,
        on = [ "team_lower","team_opponent"], 
        how = "left"
    )

    # Fusionner les deux colonnes 
    df["rivalry_pressure"] = df[["rivalry_pressure", "rivalry_pressure_inv"]].max(axis = 1).fillna(0)

    # Nettoyage 
    df = df.drop(columns = [
                             "rivalry_pressure_inv", 
                             "team_lower", 
                             "opponent_lower", 
                             "rivalrie_name_x", 
                             "rivalrie_name_y"
                            ], 
                            errors = "ignore")
    return df 



def merge_media(df, media_df):
    media = pd.DataFrame(media_df).copy()
    # keep only the column that we need
    cols = ["game_id", "national_broadcast", "prime_time"]
    media = media[[c for c in cols if c in media.columns]]
    df = df.merge(
        media, 
        on = 'game_id', 
        how =  "left"
    )
    # normalization 
    df["prime_time"] = df["prime_time"].fillna(0).astype(int)
    df["national_broadcast"] = df["national_broadcast"].fillna(0).astype(int)

    return df 

# print("=== APRES merge_prime_time ===")
# print(df.columns) 
    # Merge ranking
def merge_rankings(df, rankings_df): 
    rank = pd.DataFrame(rankings_df).copy()
    
    # Team Rank 
    df = df.merge(
        rank.rename(columns = {"school": "team", "rank": "team_rank"})[["season", "week", "team", "team_rank"]], 
        on = ["season", "week", "team"], 
        how = "left"
    )
    # opponent rank 
    df = df.merge(
        rank.rename(columns = {"school": "opponent", "rank": "opponent_rank"})[["season", "week", "opponent", "opponent_rank"]], 
        on = ["season", "week", "opponent"],
        how = "left"
    )
    df["team_rank"] = df["team_rank"].fillna(999)
    df["opponent_rank"] = df["opponent_rank"].fillna(999)
    return df 

def compute_stakes_pressure(df):
    # Pression liée à l'enjeu du match 
    # bowl, playoffs, championship 

    df["stakes_pressure"] = 0
    df.loc[df["season_type"].str.contains("championship", case = False, na = False), "stakes_pressure"] = 1
    df.loc[df["season_type"].str.contains("postseason", case = False, na = False), "stakes_pressure"] = 1
    df.loc[df["week"] >= 12,"stakes_pressure"] = 1 # fin de saison enjeux plus élévés c'est un peu osé mais je pose ça la pour l'instant

    return df
    
def compute_media_pressure(df): 
    # Pression liées à la médiatisation , prime time, Tv national , gros match(top 25) 
    # il peut avoir la valeurs 0 ou 1
    df["media_pressure"] = 0

    # Si nous avons une colonne "is_prime_time" otu "tv_audience", nous pouvons l'utiliser 
    if "prime_time" in df.columns: 
        df["media_pressure"] =  df["media_pressure"] + df["prime_time"]

    # national TV
    if "is_national_tv" in df.columns: 
        df["media_pressure"] =  df["media_pressure"] + df["national_broadcast"]

    # game between two team from top25

        df["media_pressure"] = df["media_pressure"] + ((df["team_rank"] <= 25) & (df["opponent_rank"] <= 25)).astype(int)
    return df 

def compute_psychological_shock(df):
    # pression psychologique basées sur le match précédent : 
    # Grosse victoire -> pression de confirmer 
    # Grosse défaite  -> pressionde Rebondir 
    # On prends la valeurs absolue du margin précédent  que l'on divise par le plus gros margin absolu de la saison 
    # biensure on obtient un résulat entre 0 et 1

    df = df.sort_values(["team", "date"]).reset_index(drop = True)

    # Marge du match précédent
    df["prev_margin"] = df.groupby("team")["point_diff"].shift(1)
    # max_abs = df["prev_margin"].abs().max()

    df["psychological_shock"] = df.groupby("team")["prev_margin"].transform(lambda x: x.abs()/(x.abs().max() if x.abs().max()else 1))

    # Remplacer le nan du premier match par 0
    df["psychological_shock"] = df["psychological_shock"].fillna(0)

    return df

def compute_pressure_index(df, w_rivalry = 0.25, w_stakes = 0.25, w_media = 0.25, w_shock = 0.25): 
    # Ici je fais une normalisation coneptuelle pas mathématique 
    # je mets toute les variable au même niveau d'importance  et je garantie que jle score finale reste dans une 
    # echelle cohérente j'empêche une variable dominante de dominer les autres 
    # Score final deoression (0 à 1)
    df["pressure_index"] = (
        w_rivalry * df["rivalry_pressure"] + 
        w_stakes * df["stakes_pressure"] + 
        w_media  * df["media_pressure"] + 
        w_shock * df["psychological_shock"]
    )
    return df

def compute_pressure_proxies(df, rivalries_df , prime_df, rankings_df ): 
    df = merge_rivalries(df, rivalries_df)
    df = merge_media(df, prime_df)
    df = merge_rankings(df, rankings_df)

    df = compute_stakes_pressure(df)
    df = compute_media_pressure(df)
    df = compute_psychological_shock(df)
    df = compute_pressure_index(df)

    return df

# if __name__ == "__name__":
# from pipeline.scrapers.cfbd.media import fetch_media
# from pipeline.scrapers.cfbd.rankings import fetch_rankings
# from pipeline.scrapers.cfbd.rivalries import fetch_rivalries
# from pipeline.transformation.cfbd.parse_rankings import parse_rankings
# from pipeline.transformation.cfbd.parse_media import parse_media
# from pipeline.transformation.cfbd.parse_rivalries import parse_rivalries

# valrivalries = fetch_rivalries()
# rivalries_df = parse_rivalries(valrivalries)

# valprime = fetch_media()
# media_df  = parse_media(valprime)

# valranking = fetch_rankings(all)
# rankings_df = parse_rankings(valranking)

# df_with_pressure = compute_pressure_proxies(df, rivalries_df, media_df, rankings_df )
# print(df_with_pressure.head())
