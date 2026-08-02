import sys 
import csv 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def fetch_coaching():
    result_coaching = []
    with open("data/raw/external/coaching_sample.csv") as file_coaching: 
        read_coachings = csv.DictReader(file_coaching)
        for read_coaching in read_coachings: 
            dict_coaching = {}
            for key_coaching, val_coaching in read_coaching.items(): 
                try: 
                    dict_coaching[key_coaching] = int(val_coaching)
                except ValueError:
                    try: 
                         dict_coaching[key_coaching] = float(val_coaching)
                    except ValueError:

                            dict_coaching[key_coaching] = val_coaching

            result_coaching.append(dict_coaching)
    return result_coaching

# print(fetch_coaching())
