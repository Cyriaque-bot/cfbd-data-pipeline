import sys 
from pathlib import Path
import csv 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def fetch_recruiting_external(): 
    result_recruiting_external = []

    with open("data/raw/external/recruiting_external_sample.csv") as file_recruiting_external: 
         read_recruiting_externals = csv.DictReader(file_recruiting_external)

         for read_recruiting_external in read_recruiting_externals: 
                dict_recruiting_external = {}
                for key_recruiting_external, val_recruiting_external in  read_recruiting_external.items(): 
                    try:
                        dict_recruiting_external[key_recruiting_external] = int(val_recruiting_external)
                    except ValueError:
                          try: dict_recruiting_external[key_recruiting_external] = float(val_recruiting_external)
                          except ValueError: 
                               dict_recruiting_external[key_recruiting_external] = val_recruiting_external

                result_recruiting_external.append(dict_recruiting_external)


    return result_recruiting_external          

   
# print(fetch_recruiting_externe())

