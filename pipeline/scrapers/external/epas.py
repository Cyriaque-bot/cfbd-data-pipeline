import pandas as pd 
from pathlib import Path
import sys
import csv 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def fetch_epa(): 
    result_epea = []
    with open("data/raw/external/epa_sample.csv", "r") as fiel_epa:

        read_epas = csv.DictReader(fiel_epa)
   
        for read_epa in read_epas: 
            row_dict_epa = {}
            for key_epa , val_epa in read_epa.items(): 
            # using try  catch exept 
                try: 
                    row_dict_epa[key_epa] = int(val_epa)
                except ValueError:
                        try:
                             row_dict_epa[key_epa] = float(val_epa)
                        except ValueError:
                                        row_dict_epa[key_epa] = val_epa


            result_epea.append(row_dict_epa)

    return result_epea
# print(fetch_epa())

# in order to have the double quote ("")

# def load_epa_final():

#     data_epa = scrape_epa()
#     result_load_epa_final = json.dumps(data_epa)

#     return result_load_epa_final

# print(load_epa_final())