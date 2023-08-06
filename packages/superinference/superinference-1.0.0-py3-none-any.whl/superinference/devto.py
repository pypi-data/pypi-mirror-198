import requests
from rich.console import Console
from rich.theme import Theme

console = Console(theme=Theme({"repr.str":"#54A24B", "repr.number": "#FF7F0E", "repr.none":"#808080"}))

class DevtoProfile:
    def __init__(self, username):
        self.username = username
        self.api_url = "https://dev.to/api"

    def perform_inference(self):
        url = f"{self.api_url}/users/by_username?url={self.username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 404:
            raise Exception("Invalid Dev.to username inputted.")
        else:
            raise Exception(f"Error with status code of: {response.status_code}")
    
    def pprint_inference(self):
        data = self.perform_inference()
        console.print(data)