import requests
import json

BASE_URL = "https://doctor-who-api.onrender.com/api"
SPECIES_ENDPOINT = f"{BASE_URL}/location"

def get_all_species():
    try:
        resp = requests.get(SPECIES_ENDPOINT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"Error fetching species: {e}")
        return []

def main():
    species_list = get_all_species()
    
    if not species_list:
        print("No location data returned.")
        return
    
    # Save to a JSON file
    with open("all_locations.json", "w", encoding="utf-8") as f:
        json.dump(species_list, f, ensure_ascii=False, indent=4)
    
    print(f"Saved {len(species_list)} species list to all_locations.json")

if __name__ == "__main__":
    main()