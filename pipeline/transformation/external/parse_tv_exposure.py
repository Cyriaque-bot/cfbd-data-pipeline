import sys 
import csv 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.tv_ratings import fetch_tv_rating


def parse_tv_exposure(raw_tv_exposure): 
    list_tv_exposure = []
    list_tv_exposure_avg_viewer = []
    list_tv_exposure_peak_viewers = []
    list_tv_exposure_prime_time_games = []

    for i_tv_exposure in raw_tv_exposure: 

        list_tv_exposure_avg_viewer.append(i_tv_exposure["avg_viewers"])
        list_tv_exposure_peak_viewers.append(i_tv_exposure["peak_viewers"])
        list_tv_exposure_prime_time_games.append(i_tv_exposure["prime_time_games"])

    # min max avg_viewer
    max_avg_viewer = max(list_tv_exposure_avg_viewer)
    min_avg_viewer = min(list_tv_exposure_avg_viewer)
    # min max peak_viewers
    max_peak_viewers = max(list_tv_exposure_peak_viewers)
    min_peak_viewers = min(list_tv_exposure_peak_viewers)
    # min max prime_time_games
    max_prime_time_games = max(list_tv_exposure_prime_time_games)
    min_prime_time_games = min(list_tv_exposure_prime_time_games)

    for i_tv_exposure in raw_tv_exposure: 
        dict_tv_exposure = {
            "school" : i_tv_exposure["team"], 
            "tv_exposure": round(
                          0.30 * ((i_tv_exposure["avg_viewers"] - min_avg_viewer)/(max_avg_viewer - min_avg_viewer)) +
                          0.15 *((i_tv_exposure["peak_viewers"] - min_peak_viewers)/(max_peak_viewers - min_peak_viewers)) + 
                          0.15 * ((i_tv_exposure["prime_time_games"] - min_prime_time_games)/(max_prime_time_games - min_prime_time_games)) +
                          0.15 * i_tv_exposure["network_exposure"] +
                          0.10 * i_tv_exposure["market_size"] +
                          0.15 * i_tv_exposure["network_importance"]
           , 2 )
            
        }
        list_tv_exposure.append(dict_tv_exposure)

    return list_tv_exposure

# vall = fetch_tv_rating()
# print(parse_tv_exposure(vall))