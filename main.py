import requests
import json
import os
import inquirer
from urllib.parse import urljoin

# Helper function to create folders
def create_folders():
    os.makedirs("data", exist_ok=True)

# Validate URL
def validate_url(url):
    if not url.startswith("http"):
        print("Invalid URL. Ensure it starts with http:// or https://")
        return False
    return True

# Fetch data from endpoint
def fetch_endpoint(base_url, headers, endpoint, timeout=10):
    url = urljoin(base_url, endpoint)
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

# Save data to JSON
def save_to_json(data, filepath):
    with open(filepath, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to JSON: {filepath}")

# Main program
def main():
    create_folders()

    base_url = input("Enter Home Assistant URL (e.g., http://192.168.1.100:8123): ").strip()
    api_key = input("Enter your Home Assistant Long-Lived Access Token: ").strip()

    if not validate_url(base_url) or not api_key:
        print("Error: Valid URL and API key are required.")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    endpoints = {
        "Configuration": "/api/config",
        "Events": "/api/events",
        "Services": "/api/services",
        "States": "/api/states",
        "Error Log": "/api/error_log",
        "Check Config": "/api/config/core/check_config",
    }

    questions = [
        inquirer.Checkbox(
            "endpoints", 
            message="Select endpoints to fetch data from", 
            choices=list(endpoints.keys())
        )
    ]
    selected = inquirer.prompt(questions)

    if not selected or not selected.get("endpoints"):
        print("No endpoints selected. Exiting.")
        return

    for option in selected["endpoints"]:
        endpoint = endpoints[option]
        data = fetch_endpoint(base_url, headers, endpoint)
        if data is not None:
            filename = f"{option.replace(' ', '_').lower()}.json"
            filepath = os.path.join("data", filename)
            save_to_json(data, filepath)

if __name__ == "__main__":
    main()
