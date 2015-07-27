from flask import Flask, jsonify

import requests #pip install requests

# Create an Flask app object.  We'll use this to create the routes.
app = Flask(__name__)

# Allow Flask to autoreload when we make changes to `app.py`.
app.config['DEBUG'] = True # Enable this only while testing!

#debug: localhost:5000/search/Space%20Invaders%20HTML5
@app.route("/search/<search_query>")
def search(search_query):
  url = "https://api.github.com/search/repositories?q=" + search_query
  response_dict = requests.get(url).json()
  return jsonify(response_dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# TO GET AN APPLICATION TOKEN for 20 requests/minute
# http://learn.adicu.com/webdev/#api-basics
# import requests
# import json

# gh_username = raw_input('GitHub username: ')
# gh_password = raw_input('GitHub password: ')
# payload = json.dumps({'scopes': []})

# gh_response = requests.post('https://api.github.com/authorizations', auth=(gh_username, gh_password), data=payload)
# print gh_response.json()['token']
