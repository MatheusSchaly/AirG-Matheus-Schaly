import requests
import json


# Connect to the API using a GET request
response = requests.get("https://swapi.dev/api/vehicles/")

if response.status_code == 200:
    # Retrieve the JSON data
    data = json.loads(response.text)
    results = data["results"]

    # List the first 5 unique manufacturers
    unique_ordered_manufacturers = []
    unique_manufacturers = set()
    for result in results:
        manufacturer = result["manufacturer"]
        manufacturer_lower = manufacturer.lower()

        if manufacturer_lower not in unique_manufacturers:
            unique_ordered_manufacturers.append(manufacturer)
            unique_manufacturers.add(manufacturer_lower)
            
    print(f"The first 5 unique manufacturers are: {unique_ordered_manufacturers[:5]}")
else:
    print("Error: Failed to retrieve data from API")
