"""
This script uses the requests library to connect to the
https://swapi.dev/api/vehicles/ API, retrieve its information,
parses the JSON data, and lists the 5 first unique manufacturers
"""

import json
import requests


if __name__ == "__main__":
    # Connects to the API using a GET request
    try:
        response = requests.get("https://swapi.dev/api/vehicles/", timeout=10)
    except requests.exceptions.Timeout:
        print("Error: Request Timed Out")

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

        print(
            f"The first 5 unique manufacturers are: {unique_ordered_manufacturers[:5]}"
        )
    else:
        print("Error: Failed to retrieve data from API")