# Pokémon Power Band Finder

This repository contains the Python scripts and supporting files I used to build a 
Coveo‑ready dataset for my Forward Deployed Engineer technical challenge.

The goal of the project was to treat each Pokémon as a retail product and derive a 
“Power Band” performance tier using attack, defense, and HP stats. The final dataset 
is exported as a clean JSON file ready for ingestion into a Coveo Push Source.

---

## Repository Structure

### /scripts
- **build_pokemon_json.py**  
  Fetches Pokémon data from PokéAPI, flattens the nested JSON, calculates total 
  performance scores, assigns Power Band tiers using quartiles, and exports the final dataset.

- **push_to_coveo.py**  
  (Prepared but not executed due to org‑level permissions.)  
  Demonstrates how I would push documents into a Coveo Push Source using the Push API.

### /data
- **raw_pokeapi_samples.json**  
  Example raw responses from PokéAPI before normalization.

### /output
- **coveo_pokemon_power_bands.json**  
  The final flattened, enriched dataset ready for Coveo ingestion.

### /docs
- **architecture_overview.md**  
  Explanation of the ingestion pipeline, metadata model, and relevance strategy.

- **metadata_model.md**  
  Detailed breakdown of facet fields, sortable fields, derived fields, and display fields.

---

## Summary of the Process

1. I defined a retail‑style metadata model for Pokémon.
2. I used Python to fetch all Pokémon from PokéAPI.
3. I flattened the nested API responses into a clean product‑like structure.
4. I calculated a total performance score using attack + defense + HP.
5. I computed quartiles across all Pokémon.
6. I assigned each Pokémon a Power Band tier (Lightweight → Titan).
7. I exported the final dataset as `coveo_pokemon_power_bands.json`.

---

## Next Steps (If Full Access Were Available)

- Push the dataset into the Coveo Push Source.
- Build an Atomic search interface.
- Add query pipeline rules and relevance tuning.
- Enable semantic enrichment for intent‑aware search.

---

## Contact

If you have any questions, feel free to reach out. >> klitton1776@hotmail.com
