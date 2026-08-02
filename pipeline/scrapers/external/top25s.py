import sys 
import csv 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def fetch_top25(): 
    result_top25 = []
    with open("data/raw/external/top25_sample.csv") as file_top25: 
        read_top25s = csv.DictReader(file_top25)

        for read_top25 in read_top25s: 
            dict_top25 = {}
            for key_read_top25 , val_read_top25 in read_top25.items(): 
                try:
                    dict_top25[key_read_top25] =  int(val_read_top25)
                except ValueError: 
                      try: 
                          dict_top25[key_read_top25] =  float(val_read_top25)
                      except ValueError:
                          dict_top25[key_read_top25] = val_read_top25

            result_top25.append(dict_top25)

    return result_top25

# print(fetch_top25())