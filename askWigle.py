import requests
import json

def send_to_api(ssid):
    # Replace 'API_ENDPOINT' with the actual API endpoint URL
    api_endpoint = 'API_ENDPOINT'
    payload = {'ssid': ssid}
    
    try:
        response = requests.post(api_endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get location for SSID {ssid}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    log_file = "wifi_event_log.txt"  # Path to your log file

    with open(log_file, "r") as file:
        for line in file:
            if line.startswith("Network SSID:"):
                ssid = line.split(":")[1].strip()
                location_info = send_to_api(ssid)
                if location_info:
                    print(f"SSID: {ssid} - Location: {location_info['latitude']}, {location_info['longitude']}")
