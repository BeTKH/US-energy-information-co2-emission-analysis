# config.py
import os

# Load the API key from the config file


def load_api_key():
    with open('keys.config', 'r') as file:
        for line in file:
            if line.startswith("API_KEY"):
                return line.split('=')[1].strip()  # Return the key value


API_KEY = load_api_key()
