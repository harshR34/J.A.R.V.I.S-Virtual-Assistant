import requests

api_key = "YOUR_API_KEY" # Replace with your API key from https://www.mapquestapi.com

def search_location(start_location, destination_location):
    url = "https://www.mapquestapi.com/directions/v2/route"

    params = {
        "key": "YOUR_API_KEY",
        "from": start_location,
        "to": destination_location
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error for bad response status

        data = response.json()

        if 'route' in data:
            return data['route']['locations']
        else:
            return "Error: Unable to find locations. Please check your inputs."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    start_location = input("Enter your starting location: ")
    destination_location = input("Enter your destination location: ")
    api_key = "YOUR_MAPQUEST_API_KEY"  # Replace with your actual MapQuest API key

    locations = search_location(start_location, destination_location)
    print(locations)
