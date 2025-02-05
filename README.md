# HASS to JSON

A small helper script to export Home Assistant data (e.g., sensors, entities, and configurations) into JSON files. This is particularly useful when you want to upload your Home Assistant data into an LLM (Large Language Model) to enable automation creation, data analysis, or to let the LLM know your entity and sensor names.

This tool is designed to make it easier for users to interact with their Home Assistant setups and provide their entity data for external use, such as LLM-assisted automation suggestions.

## Features

- Export selected Home Assistant API data (e.g., entities, services, events, configuration, etc.) into JSON files.
- Simple, interactive CLI interface for selecting endpoints.
- Automatically organizes JSON files into `/data` folder.
- Works securely without hardcoding sensitive data like API keys or URLs.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/juliuswms/hass-to-json.git
   cd hass-data-exporter
   ``` 

    Install the required Python dependencies:

    ```
   pip install -r requirements.txt
    ```

## Usage

 Run the script:
 `python main.py`
 
 Enter your Home Assistant URL and Long-Lived Access Token when prompted.
 
 Select the API endpoints you want to export:
   - Configuration
   - Events
   - Services
   - States
   - Error Log
   - Check Config

 The data will be saved in the `data/` directory as .json files.

## Requirements

 - Python 3.7 or later
 - Home Assistant instance with API access enabled
 - A valid Long-Lived Access Token from Home Assistant

## Generating a Long-Lived Access Token
 1. Go to your Home Assistant profile.
 2. Under the "Security" Tab scroll to Long-Lived Access Tokens and click Create Token.
 3. Copy the token and use it when prompted by the script.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
