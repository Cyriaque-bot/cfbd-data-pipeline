import json 
def load_raw_team_matchup(path: str = "data/raw/team_matchup_sample.json")-> list: 

    with open(path, "r" , encoding ="utf-8") as f : 
        data = json.load(f)
    return data

