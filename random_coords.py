import random
import json

# defines random location coords based on planet
# Define location_ID groups
london_ids = [2, 23, 26, 6,7,8,12,14,15,18,19,20,24,27,28,30,13]  # all ldn IDs
mars_ids = [4]
other_ids = [10,11,25,29]  # US, Italy, France, Australia
gallifrey_ids = [21, 1]
all_ids = list(range(1,40))
assigned_ids = london_ids + gallifrey_ids + other_ids + mars_ids
remaining_ids = [i for i in all_ids if i not in assigned_ids]

# List to store coordinate objects
coords_list = []

# 1. ldn cluster
for lid in london_ids:
    x = round(random.uniform(45, 50),2)
    y = round(random.uniform(45, 50),2)
    coords_list.append({"ID": lid, "x": x, "y": y})

# 2. Other earth locations
for oid in other_ids:
    x = round(random.uniform(50,55),2)
    y = round(random.uniform(50,55),2)
    coords_list.append({"ID": oid, "x": x, "y": y})

# 3. Mars (close to earth)
for mid in mars_ids:
    x = round(random.uniform(5,10),2)
    y = round(random.uniform(80,90),2)
    coords_list.append({"ID": mid, "x": x, "y": y})

# 4. Gallifrey coordinates (close together points)
for gid in gallifrey_ids:
    gx = round(random.uniform(30, 50),2)
    gy = round(random.uniform(-80,-60),2)
    coords_list.append({"ID": gid, "x": gx, "y": gy})

# 5. Other planets random
for rid in remaining_ids:
    x = round(random.uniform(-200,200),2)
    y = round(random.uniform(-200,200),2)
    coords_list.append({"ID": rid, "x": x, "y": y})

# Save to JSON
with open("location_coords.json", "w", encoding="utf-8") as f:
    json.dump(coords_list, f, ensure_ascii=False, indent=4)

print("Coordinates saved to location_coords.json in list")



