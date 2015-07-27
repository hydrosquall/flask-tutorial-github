from flask import Flask

import requests #pip install requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)
response_dict = response.json()
# Use this to parse out specific parts of the JSON array: response_dict["items"][0]["language"]

print response_dict
