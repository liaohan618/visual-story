import json

# Read data from text file
with open('harvard_park_homicides.txt', 'r') as file:
    lines = file.readlines()

# Structure data into a list of dictionaries
homicides_data = []
for line in lines:
    # Assuming each line contains data separated by commas
    data = line.strip().split(',')
    homicide = {
        'case_number': data[0],
        'date': data[1],
        'location': data[2],
        'description': data[3]
        # Add more fields as needed
    }
    homicides_data.append(homicide)

# Write data to JSON file
with open('harvard_park_homicides.json', 'w') as json_file:
    json.dump(homicides_data, json_file, indent=4)
