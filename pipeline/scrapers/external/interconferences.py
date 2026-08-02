import sys 
import csv
from  pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def fetch_interconference(): 
    result_interconference = []
    with open("data/raw/external/interconference_sample.csv") as file_interconference: 
        read_interconferences = csv.DictReader(file_interconference)
       
        for read_interconference in read_interconferences: 
            dict_interconference = {}
            for key_interconference , val_interconference in read_interconference.items(): 
                try: 
                    dict_interconference[key_interconference] = int(val_interconference)
                except ValueError: 
                    try: 
                         dict_interconference[key_interconference] = float(val_interconference)
                    except ValueError: 
                         dict_interconference[key_interconference] = val_interconference

            result_interconference.append(dict_interconference)

    return result_interconference

# print(fetch_interconference())