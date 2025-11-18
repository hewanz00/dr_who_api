import json

# uses location_coords create to related planet IDs and planet coords

with open("location_coords.json", "r", encoding="utf-8") as f:
    locations = json.load(f)

# Define your planet groups
london_ids = [2, 23, 26, 6,7,8,12,14,15,18,19,20,24,27,28,30,13]  # Earth
mars_ids = [4]
other_earth_ids = [10,11,25,29]
gallifrey_ids = [21, 1]

all_ids = list(range(1,40))
assigned_ids = london_ids + mars_ids + other_earth_ids + gallifrey_ids
remaining_ids = [i for i in all_ids if i not in assigned_ids]

# Map planet ID to location IDs
planet_to_ids = {
    2: london_ids + other_earth_ids,
    4: mars_ids,
    1: gallifrey_ids
}

# Store planet coordinates
planet_coords = {}

# 1. Assign coordinates per planet
planet_coords[2] = {"x": 47.5, "y": 47.0}  # Earth cluster
planet_coords[4] = {"x": 7.5, "y": 85.0}   # Mars
planet_coords[1] = {"x": 35.0, "y": -70.0} # Gallifrey

# 2. Remaining IDs → use their location x/y as planet coordinates
for loc in locations:
    loc_id = loc["ID"]
    if loc_id in remaining_ids:
        planet_coords[loc_id] = {"x": loc["x"], "y": loc["y"]}

# 3. Build final list with Planet_ID + coordinates
coords_list = []

# Add grouped planets
for planet_id, ids in planet_to_ids.items():
    for loc_id in ids:
        coords_list.append({
            "ID": loc_id,
            "Planet_ID": planet_id,
            "x": planet_coords[planet_id]["x"],
            "y": planet_coords[planet_id]["y"]
        })

# Add remaining IDs
for rid in remaining_ids:
    coords_list.append({
        "ID": rid,
        "Planet_ID": rid,
        "x": planet_coords[rid]["x"],
        "y": planet_coords[rid]["y"]
    })

# Save as JSON
with open("planet_coordinates.json", "w", encoding="utf-8") as f:
    json.dump(coords_list, f, ensure_ascii=False, indent=4)

print("Coordinates planet coords saved")
