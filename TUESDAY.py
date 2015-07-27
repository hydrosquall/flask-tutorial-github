from flask import Flask, jsonify
import requests

# Create an Flask app object.  We'll use this to create the routes.
app = Flask(__name__)

# Allow Flask to autoreload when we make changes to `app.py`.
app.config['DEBUG'] = True # Enable this only while testing!

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/name')
def my_name():
	return "Dan Schlosser"

@app.route('/website')
def website():
	return "adicu.com"

@app.route('/search/<search_query>')
def search(search_query):

	url = "https://api.github.com/search/repositories?q=" + search_query

	response = requests.get(url)
	response_dict = response.json()

	return jsonify(response_dict)

@app.route('/add/<x>/<y>')
def add(x, y):
	return int(x) + int(y)

# Handle
@app.errorhandler(404)
def not_found(error):
	return "Sorry, I haven't coded that yet.", 404

@app.errorhandler(500)
def internal_server_error(error):
	return "My code broke, my bad.", 500


# If the user executed this python file (typed `python app.py` in their
# terminal), run our app.
if __name__ == '__main__':
	app.run(host='0.0.0.0')