import json

def parse_and_save_to_file(api_response_file, output_file):
    ssid_location_map = {}

    with open(api_response_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            ssid = data.get('ssid', '')
            latitude = data.get('latitude', '')
            longitude = data.get('longitude', '')
            ssid_location_map[ssid] = (latitude, longitude)

    with open(output_file, 'w') as f:
        for ssid, (latitude, longitude) in ssid_location_map.items():
            f.write(f"{ssid} - Location: {latitude}, {longitude}\n")

if __name__ == "__main__":
    api_response_file = "api_response.json"  # Path to your API response JSON file
    output_file = "wifi_locations.txt"  # Path to the output text file

    parse_and_save_to_file(api_response_file, output_file)
