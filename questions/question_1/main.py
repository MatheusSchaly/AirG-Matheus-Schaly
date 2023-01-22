"""
This script uses the requests library to connect to the https://swapi.dev/api/vehicles/ API,
retrieve its information, parses the JSON data, and lists the 5 first unique manufacturers
"""

import json
import requests


def list_unique_manufacturers(num_manufacturers=5):
    """
    Retrieve and list the first 'n' unique manufacturers from the https://swapi.dev/api/vehicles/ API.
    If num_manufacturers is greater than the actuall available number of manufacturers,
    then list all available manufacturers

    Arguments:
    num_manufacturers: Number of unique manufacturers to list

    Returns:
    None
    """

    if num_manufacturers > 0:
        # Connects to the API using a GET request
        try:
            response = requests.get("https://swapi.dev/api/vehicles/", timeout=10)
        except requests.exceptions.Timeout:
            print("Error: Request Timed Out")

        if response.status_code == 200:
            # Retrieve the JSON data
            data = json.loads(response.text)
            results = data["results"]

            # List the first num_manufacturers unique manufacturers
            unique_ordered_manufacturers = []
            unique_manufacturers = set()
            for result in results:
                manufacturer = result["manufacturer"]
                manufacturer_lower = manufacturer.lower()

                if manufacturer_lower not in unique_manufacturers:
                    unique_ordered_manufacturers.append(manufacturer)
                    unique_manufacturers.add(manufacturer_lower)
                    if len(unique_manufacturers) == num_manufacturers:
                        break  # We only need the first num_manufacturers manufacturers

            print(f"Listing the first {num_manufacturers} unique manufacturers:")
            for i, manufacturer in enumerate(unique_ordered_manufacturers):
                print(f"{i+1}: {manufacturer}")

        else:
            print("Error: Failed to retrieve data from API")
    else:
        print("Invalid number of manufacturers provided, it must be greater than 0")


if __name__ == "__main__":
    list_unique_manufacturers(5)
