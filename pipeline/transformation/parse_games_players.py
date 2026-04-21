import os 
import sys 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)



def parse_games_players_stats(raws_value): 
    vallitgame_id = []
    valliteam = []
    vallcategories = []
    valltype = []
    vallathlest = []
    vallistfinal = []
    

    # loop on each match 
    for key, val in raws_value.items():
        if key == "id": 
           vallitgame_id.append(val)
    # print(vallitgame_id)
    vallistfinal.append(vallitgame_id)

    # loop on each teams 
    for i in raws_value["teams"]: 
        for keyi , vali in i.items(): 
            if keyi not in "categories":
  
               valliteam.append(vali) 

    vallistfinal.append(valliteam)
    
    # loop on categories 
    for key, val in raws_value.items(): 
        if key == "teams": 
           for j in val : 
               for keyj, valj in j.items():
                   if  keyj == "categories":
                    #    print(valj)
                    for l in valj: 
                        for keyl, vall, in l.items(): 
                            if keyl == "name": 
                               vallcategories.append(vall)
    vallistfinal.append(vallcategories)

    # loop  on  types 

    for key, val in raws_value.items(): 
        if key == "teams": 
           for j in val : 
               for keyj, valj in j.items():
                   if  keyj == "categories":
                    for l in valj: 
                        for keyl, vall, in l.items(): 
                            if keyl == "types": 
                               for k in vall: 
                                   for keyk, vallk in k.items() : 
                                       if keyk == "name": 
                                          valltype.append(vallk)
    # print(valltype)
    vallistfinal.append(valltype)

    for key, val in raws_value.items(): 
        if key == "teams": 
           for j in val : 
               for keyj, valj in j.items():
                   if  keyj == "categories":
                    for l in valj: 
                        for keyl, vall, in l.items(): 
                            if keyl == "types": 
                               for k in vall: 
                                   for keyk, vallk in k.items() : 
                                       if keyk == "athletes": 
                                          for m in vallk: 
                                              for keym, vallm in m.items(): 
                                                 vallathlest.append(vallm)
    vallistfinal.append(vallathlest)




from pipeline.loaders.load_games_players_stats import load_games_players

raw = load_games_players()
parsed = parse_games_players_stats(raw)

