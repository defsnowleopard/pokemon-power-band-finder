import json
import requests

API_KEY = "xx21170fd1-2e4f-4309-ae10-152882285ae7"
ORG_ID = "katpokemonchallengecezvmacy"
SOURCE_ID = "katpokemonchallengecezvmacy-uvnbl4k4r4ysova3xzo6xscjjy"

ENDPOINT = f"https://api.cloud.coveo.com/push/v1/organizations/{ORG_ID}/sources/{SOURCE_ID}/documents"

# Load your JSON file
with open("coveo_pokemon_power_bands.json", "r") as f:
    data = json.load(f)

pokemon_list = data["pokemon"]

for p in pokemon_list:
    uri = f"pokemon://{p['dex']}/{p['name']}"
    document = {
        "documentId": uri,
        "title": p["name"],
        "data": p
    }

    response = requests.put(
        ENDPOINT,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=document
    )

    print(p["name"], response.status_code)
