import sys 
import csv 
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def fetch_tv_rating(): 
    result_tv_rating = []
    with open("data/raw/external/tv_rating_sample.csv") as file_tv_rating: 
        read_tv_ratings = csv.DictReader(file_tv_rating)

        for read_tv_rating in read_tv_ratings: 
            dict_tv_rating = {}
            for key_tv_rating, val_tv_rating in read_tv_rating.items(): 
                try: 
                    dict_tv_rating[key_tv_rating] = int(val_tv_rating)
                except ValueError:
                    try: 
                        dict_tv_rating[key_tv_rating] = float(val_tv_rating)
                    except ValueError:
                        dict_tv_rating[key_tv_rating] = val_tv_rating
            
            result_tv_rating.append(dict_tv_rating)

    return result_tv_rating

# print(fetch_tv_rating())