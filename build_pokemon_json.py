import json
import requests

OUTPUT_FILE = "coveo_pokemon_power_bands.json"

def fetch_all_pokemon():
    # First, get the full list of Pokémon + forms
    url = "https://pokeapi.co/api/v2/pokemon?limit=20000"
    response = requests.get(url)
    response.raise_for_status()
    results = response.json()["results"]

    pokemon_data = []

    for entry in results:
        api_url = entry["url"]
        p = requests.get(api_url).json()

        # Extract stats
        stats = {s["stat"]["name"]: s["base_stat"] for s in p["stats"]}

        pokemon_data.append({
            "name": p["name"],
            "dex": p["id"],
            "types": [t["type"]["name"] for t in p["types"]],
            "hp": stats.get("hp", 0),
            "attack": stats.get("attack", 0),
            "defense": stats.get("defense", 0),
            "sp_atk": stats.get("special-attack", 0),
            "sp_def": stats.get("special-defense", 0),
            "speed": stats.get("speed", 0),
            "total": stats.get("hp", 0) + stats.get("attack", 0) + stats.get("defense", 0),
            "api_url": api_url
        })

    return pokemon_data

def compute_quartiles(pokemon_list):
    totals = sorted([p["total"] for p in pokemon_list])
    n = len(totals)

    q1 = totals[int(0.25 * n)]
    q2 = totals[int(0.50 * n)]
    q3 = totals[int(0.75 * n)]

    return q1, q2, q3

def assign_power_bands(pokemon_list, q1, q2, q3):
    for p in pokemon_list:
        total = p["total"]
        if total <= q1:
            p["power_band"] = "Lightweights"
        elif total <= q2:
            p["power_band"] = "Midweights"
        elif total <= q3:
            p["power_band"] = "Heavyweights"
        else:
            p["power_band"] = "Titans"

def main():
    print("Fetching Pokémon data from PokéAPI...")
    pokemon_list = fetch_all_pokemon()

    print(f"Fetched {len(pokemon_list)} Pokémon and forms.")

    print("Computing quartiles...")
    q1, q2, q3 = compute_quartiles(pokemon_list)

    print("Assigning power bands...")
    assign_power_bands(pokemon_list, q1, q2, q3)

    print("Writing compact JSON output...")
    output = {"pokemon": pokemon_list}

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, separators=(",", ":"))

    print(f"Done! Generated {OUTPUT_FILE} with {len(pokemon_list)} Pokémon.")

if __name__ == "__main__":
    main()
