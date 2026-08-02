from pathlib import Path
import sys 
import csv 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def fetch_nfl(): 
    result_nfl = []
    with open("data/raw/external/nfl_sample.csv") as file_nfl:
        read_nfls = csv.DictReader(file_nfl)

        for read_nfl in read_nfls: 
            dict_nfl = {}
            for key_nfl , val_nfl in read_nfl.items(): 
                try:
                    dict_nfl[key_nfl] = int(val_nfl)
                except ValueError:
                    try: 
                        dict_nfl[key_nfl] = float(val_nfl)
                    except ValueError: 
                        dict_nfl[key_nfl] = val_nfl

            result_nfl.append(dict_nfl)

    return result_nfl


# print(fetch_nfl())