import json

# Load real coordinates
with open("location_coords.json", "r", encoding="utf-8") as f:
    location_coords = json.load(f)

# Load names
with open("all_locations.json", "r", encoding="utf-8") as f:
    location_names = json.load(f)

# Lookups
coord_lookup = {item["ID"]: item for item in location_coords}
name_lookup = {item["id"]: item["name"] for item in location_names}

# Define groups
earth_ids = [2, 23, 26, 6,7,8,12,14,15,18,19,20,24,27,28,30,13, 10,11,25,29]
mars_ids = [4]
gallifrey_ids = [1, 21]

# All possible IDs (1–39)
all_ids = list(range(1,40))
grouped_ids = earth_ids + mars_ids + gallifrey_ids
remaining_ids = [i for i in all_ids if i not in grouped_ids]

# Map each ID → planet ID
planet_lookup = {}

for i in earth_ids:
    planet_lookup[i] = 2  # Earth
for i in mars_ids:
    planet_lookup[i] = 4  # Mars
for i in gallifrey_ids:
    planet_lookup[i] = 1  # Gallifrey


# Remaining planets are their own ID
for i in remaining_ids:
    planet_lookup[i] = i

# Map Planet_ID → Planet_Name
planet_name_lookup = {
    1: "Gallifrey",
    2: "Earth",
    4: "Mars"
}

# Build final combined dataset
combined = []

for id_ in all_ids:
    if id_ not in coord_lookup:
        continue

    planet_id = planet_lookup[id_]

    # Default planet name → if not Earth/Mars/Gallifrey, use location name
    planet_name = planet_name_lookup.get(planet_id, name_lookup.get(id_, "Unknown"))

    combined.append({
        "ID": id_,
        "Planet_ID": planet_id,
        "Planet_Name": planet_name,
        "Name": name_lookup.get(id_, "Unknown"),
        "x": coord_lookup[id_]["x"],
        "y": coord_lookup[id_]["y"]
    })

# Save merged dataset
with open("locations_with_planet_coords.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=4)



print("Saved combined_locations_planets.json ")
