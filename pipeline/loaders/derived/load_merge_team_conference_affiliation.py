import sys
from pathlib import Path
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_merge_team_conference_affiliation():
    with open("data/raw/derived/merge_team_conference_affiliation_sample.json") as json_merge_team_conference_affiliation_sample: 
         result_merge_team_conference_affiliation_sample = json.load(json_merge_team_conference_affiliation_sample)
    return result_merge_team_conference_affiliation_sample

# print(load_merge_team_conference_affiliation())