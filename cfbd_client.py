import requests

# Ecriture de ma clé API en dure 
API_KEY = "dDuqMTZh6n4v/fvF3i9q60GYrRucVjFh10864qWU+JRN+arazUzTz0SJN26W19QS"

# definir mon Headers précis 

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

BASE_URL = "https://api.collegefootballdata.com"

def get(valendpoint, params=None):
    # fonction generique pour appeler l'API CFBD
# construit l' URL
    url = BASE_URL + valendpoint 
# Envoie la requête
    valresponse =  requests.get(url, headers = headers, params = params)
# Verification du code HTTP
    if valresponse.status_code != 200:
        print(f"Erreur{valresponse.status_code} lors de l'appel à {valendpoint}")
        print(valresponse.text)
        return None
    # print(valresponse.text)
    return valresponse.json()

# Fonction spécifique
def get_teams(year):
    return get("/teams", params = {"year":year})

def get_games(year):
    return get("/games", params = {"year":year})

def get_coaches(year):
    return get("/coaches", params = {"year":year})

def get_rosters(year):
    return get("/roster", params = {"year":year})

def get_rankings(year):
    return get("/rankings", params = {"year":year})

def get_venues(): 
    return get("/venues")

def get_calendar(year):
    return get("/calendar", params = {"year": year} )
    
def get_game_team_stats(year, week):
    return get("/games/teams", params = {"year": year, "week": week})

def get_game_player_stats(year, week):
    return get("/games/players", params = {"year": year , "week": week})

def get_recruiting(year):
    return get("/recruiting/players", params = {"year": year})

# print(get_teams())
# print(get_games(2023))
