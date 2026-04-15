import requests

API_KEY = "dDuqMTZh6n4v/fvF3i9q60GYrRucVjFh10864qWU+JRN+arazUzTz0SJN26W19QS"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

url = "https://api.collegefootballdata.com/teams"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Body:", response.text[:500])

import os
print(os.path.dirname(__file__))
print(os)