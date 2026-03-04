import requests

def check_site():
    response = requests.get("https://www.saucedemo.com/")
    if response.status_code == 200:
        Log.Checkpoint("Site is online!")