import sys
from pathlib import Path
import pandas as pd 
import math


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.merge_team_conference_affiliation import fetch_merge_team_conference_affiliation
from pipeline.transformation.derived.parse_merge_team_conference_affiliation import parse_merge_team_conference_affiliation

def compute_conference_strength_cfbd(raw_merge_team_conference_affiliation): 
       list_compute_conference_strenght_cfbd_final_total = []
       list_compute_conference_strenght_cfbd_start = []
       list_compute_conference_strenght_cfbd_int = []
       list_compute_conference_strenght_cfbd_final = []
       list_compute_conference_raw_strenght_cfbd = []
       list_avg_sp_overall = []
       list_avg_fpi_overall = []
       list_avg_srs = []
       list_avg_elo = []

       list_avg_off_ppa = []
       list_avg_def_ppa = []

       list_avg_off_success = []
       list_avg_def_success = []

       list_avg_off_explosiveness = []
       list_avg_def_explosiveness = []

       # mean 
       list_mean_sp = []
       list_mean_fpi = []
       list_mean_srs = []
       list_mean_elo = []

       list_mean_off_ppa = [] 
       list_mean_def_ppa = []

       list_mean_off_success = []
       list_mean_def_success = []

       list_mean_off_explosiveness = []
       list_mean_def_explosiveness = []
       # standart deviation
       list_isp = []
       list_fpi = [] 
       list_srs = []
       list_elo = []

       list_off_ppa = []
       list_def_ppa = []

       for i_compute_conference_strenght_cfbd in raw_merge_team_conference_affiliation: 
       
  
              dict_compute_conference_strenght_cfbd = {
                # Time  
                "season": i_compute_conference_strenght_cfbd["season"],

                # conference
                "conference_id" : i_compute_conference_strenght_cfbd["conference_id"], 
                "conference_name": i_compute_conference_strenght_cfbd["conference_name"], 
                "conference_short_name": i_compute_conference_strenght_cfbd["conference_short_name"], 
                "conference_classification": i_compute_conference_strenght_cfbd["conference_classification"], 

                # team_count
                "team_count": i_compute_conference_strenght_cfbd["conference_member_count"]
             
         
              }

              for j_compute_conference_strenght_cfbd in raw_merge_team_conference_affiliation: 
                     if j_compute_conference_strenght_cfbd["conference_id"] ==  i_compute_conference_strenght_cfbd["conference_id"]: 
              # SP, FPI, SRS, ELO
                            list_avg_sp_overall.append(j_compute_conference_strenght_cfbd["sp_overall"])
                            list_avg_fpi_overall.append(j_compute_conference_strenght_cfbd["fpi_overall"])
                            list_avg_srs.append(j_compute_conference_strenght_cfbd["srs"])
                            list_avg_elo.append(j_compute_conference_strenght_cfbd["elo"])

                            # off_ppa , def ppa
                            list_avg_off_ppa.append(j_compute_conference_strenght_cfbd["off_ppa"])
                            list_avg_def_ppa.append(j_compute_conference_strenght_cfbd["def_ppa"])

                            # off_success, def_success
                            list_avg_off_success.append(j_compute_conference_strenght_cfbd["off_success"])
                            list_avg_def_success.append(j_compute_conference_strenght_cfbd["def_success"])

                            # def_explosiveness, off_explosiveness
                            list_avg_off_explosiveness.append(j_compute_conference_strenght_cfbd["off_explosiveness"])
                            list_avg_def_explosiveness.append(j_compute_conference_strenght_cfbd["def_explosiveness"])

           
       # add everything in dict_compute_conference_strenght_cfbd
              
               # SP, FPI, SRS, ELO
              dict_compute_conference_strenght_cfbd["avg_sp_overall"] = round(sum(list_avg_sp_overall)/ len(list_avg_sp_overall), 2)
              dict_compute_conference_strenght_cfbd["avg_fpi_overall"] = round(sum(list_avg_fpi_overall)/ len(list_avg_fpi_overall), 2)
              dict_compute_conference_strenght_cfbd["avg_srs"] = round(sum(list_avg_srs)/ len(list_avg_srs), 2)
              dict_compute_conference_strenght_cfbd["avg_elo"] = round(sum(list_avg_elo)/ len(list_avg_elo), 2)

                     # off_ppa , def ppa
              dict_compute_conference_strenght_cfbd["avg_off_ppa"] = round(sum(list_avg_off_ppa)/ len(list_avg_off_ppa), 2)
              dict_compute_conference_strenght_cfbd["avg_def_ppa"] = round(sum(list_avg_def_ppa)/ len(list_avg_def_ppa), 2)

                     # off_success, def_success
              dict_compute_conference_strenght_cfbd["avg_off_success"] = round(sum(list_avg_off_success)/ len(list_avg_off_success), 2)
              dict_compute_conference_strenght_cfbd["avg_def_success"] = round(sum(list_avg_def_success)/ len(list_avg_off_success), 2)

                     # off_explosiveness, def_explosiveness
              dict_compute_conference_strenght_cfbd["avg_off_explosiveness"] = round(sum(list_avg_off_explosiveness)/ len(list_avg_off_explosiveness), 2)
              dict_compute_conference_strenght_cfbd["avg_def_explosiveness"] = round(sum(list_avg_def_explosiveness)/ len(list_avg_def_explosiveness), 2)

              # clear all the list in order to set it free again

                     # clear sp, fpi, srs, elo
              list_avg_sp_overall.clear()
              list_avg_fpi_overall.clear()
              list_avg_srs.clear()
              list_avg_elo.clear()

                    # off_ppa , def ppa
              list_avg_off_ppa.clear()
              list_avg_def_ppa.clear()

                    # off_success, def_success
              list_avg_off_success.clear()
              list_avg_def_success.clear()

                    # off_explosiveness, def_explosiveness
              list_avg_off_explosiveness.clear()
              list_avg_def_explosiveness.clear()
           
              list_compute_conference_strenght_cfbd_start.append(dict_compute_conference_strenght_cfbd)

              # empty the list
       
       
     
       view_compute_conference_strenght_cfbd_int = set()
       for dict_compute_conference_strenght_cfbd in list_compute_conference_strenght_cfbd_start: 
              if dict_compute_conference_strenght_cfbd["conference_id"] not in view_compute_conference_strenght_cfbd_int: 
                     view_compute_conference_strenght_cfbd_int.add(dict_compute_conference_strenght_cfbd["conference_id"])
                     list_compute_conference_strenght_cfbd_int.append(dict_compute_conference_strenght_cfbd)
       # calculation of all SP, FPI, SRS, ELO for all the conference by distinct
       
       for i_list_compute_conference_strenght_cfbd_int in list_compute_conference_strenght_cfbd_int: 

              # SP , FPI, SRS, ELO
              list_mean_sp.append(i_list_compute_conference_strenght_cfbd_int["avg_sp_overall"])
              list_mean_fpi.append(i_list_compute_conference_strenght_cfbd_int["avg_fpi_overall"])
              list_mean_srs.append(i_list_compute_conference_strenght_cfbd_int["avg_srs"])
              list_mean_elo.append(i_list_compute_conference_strenght_cfbd_int["avg_elo"])

              #  OFF_PPA , DEF PPA
              list_mean_off_ppa.append(i_list_compute_conference_strenght_cfbd_int["avg_off_ppa"])
              list_mean_def_ppa.append(i_list_compute_conference_strenght_cfbd_int["avg_def_ppa"])

              # OFF_SUCCESS, DEF_SUCCESS
              list_mean_off_success.append(i_list_compute_conference_strenght_cfbd_int["avg_off_success"])
              list_mean_def_success.append(i_list_compute_conference_strenght_cfbd_int["avg_def_success"])

              list_mean_off_explosiveness.append(i_list_compute_conference_strenght_cfbd_int["avg_off_explosiveness"])
              list_mean_def_explosiveness.append(i_list_compute_conference_strenght_cfbd_int["avg_def_explosiveness"])


      
       # all average 
             #  sp,fpi,srs,elo 

       mean_sp = round(sum(list_mean_sp) / len(list_mean_sp), 4)
       mean_fpi = round(sum(list_mean_fpi) / len(list_mean_fpi), 4)
       mean_srs = round(sum(list_mean_srs) / len(list_mean_srs), 4)
       mean_elo = round(sum(list_mean_elo) / len(list_mean_elo), 4)

       mean_off_ppa = round(sum(list_mean_off_ppa)/ len(list_mean_off_ppa), 4)
       mean_def_ppa = round(sum(list_mean_def_ppa)/ len(list_mean_def_ppa), 4)

      
       # return mean_sp, mean_fpi, mean_srs, mean_elo, mean_off_ppa, mean_def_ppa
             # off_ppa, def_ppa

       # deviation for all of theme 
             # mean_sp
       for i_sp in list_mean_sp:
            list_isp.append(round((i_sp - mean_sp)**2 , 4))
       std_sp = round(sum(list_isp)** 0.5, 2)

             # mean_fpi
       for i_fpi in list_mean_fpi: 
              list_fpi.append(round((i_fpi - mean_fpi)**2, 4))
       std_fpi = round(sum(list_fpi)** 0.5, 2)

             # mean_srs
       for i_srs in list_mean_srs: 
              list_srs.append(round((i_srs - mean_srs)**2, 4)) 
       std_srs = round(sum(list_srs)** 0.5, 2)

             # mean_elo
       for i_elo in list_mean_elo: 
              list_elo.append(round((i_elo - mean_elo)**2, 4))
       std_elo = round(sum(list_elo)** 0.5, 2)

             # mean_off_ppa
       for i_off_ppa in list_mean_off_ppa: 
              list_off_ppa.append(round((i_off_ppa - mean_off_ppa)**2, 4))
       std_off_ppa = round(sum(list_off_ppa)** 0.5, 2)

             # mean_def_ppa
       for i_def_ppa in list_mean_def_ppa: 
              list_def_ppa.append(round((i_def_ppa - mean_def_ppa)**2, 4))
       std_def_ppa = round(sum(list_def_ppa)** 0.5, 2)

     
     
       # return std_def_ppa
       for i_list_compute in  list_compute_conference_strenght_cfbd_int: 

              dict_i_list_compute = {
                "season": i_list_compute["season"],

                # conference
                "conference_id" : i_list_compute["conference_id"], 
                "conference_name": i_list_compute["conference_name"], 
                "conference_short_name": i_list_compute["conference_short_name"], 
                "conference_classification": i_list_compute["conference_classification"], 

                # team_count
                "team_count": i_list_compute["team_count"], 

                "avg_sp_overall": i_list_compute["avg_sp_overall"], 
                "avg_fpi_overall": i_list_compute["avg_fpi_overall"], 
                "avg_srs": i_list_compute["avg_srs"], 
                "avg_elo": i_list_compute["avg_elo"], 

                "avg_off_ppa": i_list_compute["avg_off_ppa"], 
                "avg_def_ppa": i_list_compute["avg_def_ppa"], 

                "avg_off_success": i_list_compute["avg_off_success"], 
                "avg_def_success": i_list_compute["avg_def_success"], 

                "avg_off_explosiveness": i_list_compute["avg_off_explosiveness"], 
                "avg_def_explosiveness": i_list_compute["avg_def_explosiveness"],
                "conference_strength_raw": round(
                            
                                           (
                                           0.35 * ((i_list_compute["avg_sp_overall"] - mean_sp)/std_sp)
                                         + 0.25 * ((i_list_compute["avg_fpi_overall"] - mean_fpi)/std_fpi)
                                         + 0.15 * ((i_list_compute["avg_srs"] - mean_srs)/std_srs)
                                         + 0.10 * ((i_list_compute["avg_elo"] - mean_elo)/std_elo)
                                         + 0.10 * ((i_list_compute["avg_off_ppa"] - mean_off_ppa)/std_off_ppa)
                                         + 0.05 * ((i_list_compute["avg_def_ppa"] - mean_def_ppa)/std_def_ppa)
                                   
                                    ), 2

                )

              }
               
              list_compute_conference_strenght_cfbd_final.append(dict_i_list_compute)

       # normalization
              
       for i_list_compute_conference_strenght_cfbd_final in list_compute_conference_strenght_cfbd_final: 
              list_compute_conference_raw_strenght_cfbd.append(i_list_compute_conference_strenght_cfbd_final["conference_strength_raw"])
     

           # min max or normalisation conference_strength_raw
       max_conference_strength_raw = max(list_compute_conference_raw_strenght_cfbd)
       min_conference_strength_raw = min(list_compute_conference_raw_strenght_cfbd)

       # final result 
       for i_list_compute_final in  list_compute_conference_strenght_cfbd_final: 
       
                     dict_i_list_compute_final = {
                       "season": i_list_compute_final["season"],
       
                       # conference
                       "conference_id" : i_list_compute_final["conference_id"], 
                       "conference_name": i_list_compute_final["conference_name"], 
                       "conference_short_name": i_list_compute_final["conference_short_name"], 
                       "conference_classification": i_list_compute_final["conference_classification"], 
       
                       # team_count
                       "team_count": i_list_compute_final["team_count"], 
       
                       "avg_sp_overall": i_list_compute_final["avg_sp_overall"], 
                       "avg_fpi_overall": i_list_compute_final["avg_fpi_overall"], 
                       "avg_srs": i_list_compute_final["avg_srs"], 
                       "avg_elo": i_list_compute_final["avg_elo"], 
       
                       "avg_off_ppa": i_list_compute_final["avg_off_ppa"], 
                       "avg_def_ppa": i_list_compute_final["avg_def_ppa"], 
       
                       "avg_off_success": i_list_compute_final["avg_off_success"], 
                       "avg_def_success": i_list_compute_final["avg_def_success"], 
       
                       "avg_off_explosiveness": i_list_compute_final["avg_off_explosiveness"], 
                       "avg_def_explosiveness": i_list_compute_final["avg_def_explosiveness"],
                       "conference_strength_raw": i_list_compute_final["conference_strength_raw"], 
                       "conference_strength_norm": round( 
                                                  (i_list_compute_final["conference_strength_raw"] - min_conference_strength_raw) /
                                                     (max_conference_strength_raw - min_conference_strength_raw)
                                                  , 2)

       
                     }
                     list_compute_conference_strenght_cfbd_final_total.append(dict_i_list_compute_final)


       return list_compute_conference_strenght_cfbd_final_total

# val = fetch_merge_team_conference_affiliation()
# valparse = parse_merge_team_conference_affiliation(val)
# print(compute_conference_strength_cfbd(valparse))