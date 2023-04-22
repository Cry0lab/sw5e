import requests

# Make a GET request to the API endpoint
response = requests.get("https://sw5eapi.azurewebsites.net/api/enhancedItem")

# Get the JSON data from the response
data = response.json()

# Create a dictionary to store the equipment by their category
equipment_by_category = {}

# Iterate over the equipment and group them by their category
for equipment in data:
    category = equipment["type"]
    #if the category doesn't exist yet, create it
    if category not in equipment_by_category:
        equipment_by_category[category] = []
    #Add the equipment to its category
    equipment_by_category[category].append(equipment)
