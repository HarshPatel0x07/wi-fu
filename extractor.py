import os
import subprocess
import re

def extract_wifi_logs(output_file):
    log_name = "Microsoft-Windows-WLAN-AutoConfig/Operational"
    cmd = f"wevtutil qe {log_name} /rd:true /f:text > {output_file}"
    subprocess.run(cmd, shell=True)

def parse_log_file(log_file, output_text_file):
    with open(log_file, "r") as log_file:
        log_lines = log_file.readlines()

    wifi_events = []
    current_event = {}
    for line in log_lines:
        if line.startswith("Event["):
            if current_event:
                wifi_events.append(current_event)
                current_event = {}

        match = re.match(r"\s+([^:]+):\s(.+)", line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            current_event[key] = value

    if current_event:
        wifi_events.append(current_event)

    with open(output_text_file, "w") as output_file:
        for event in wifi_events:
            output_file.write("Event:\n")
            for key, value in event.items():
                output_file.write(f"{key}: {value}\n")
            output_file.write("\n")

if __name__ == "__main__":
    log_file = "wifi_event_log.evtx"
    output_text_file = "wifi_log.txt"

    extract_wifi_logs(log_file)

    parse_log_file(log_file, output_text_file)

    os.remove(log_file)

    print("Wi-Fi log extraction completed and saved to", output_text_file)
