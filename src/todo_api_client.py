import requests
import json

from src.config import Config

class TodoApiClient:
    def __init__(self):
        self.base_url = Config.API_ENDPOINT

    def get_todos(self, params):
        try:
            url = f"{Config.API_ENDPOINT}todos"
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            try:
                json_data = response.json()
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None

            return json_data
        except requests.exceptions.RequestException as e:
            print(f"Error making HTTP GET request: {e}")
            return None