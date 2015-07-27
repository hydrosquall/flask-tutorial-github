from flask import Flask, jsonify, render_template

# Create an Flask app object.  We'll use this to create the routes.
app = Flask(__name__)

# Allow Flask to autoreload when we make changes to `app.py`.
app.config['DEBUG'] = True # Enable this only while testing!

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
    return "Cameron Yick"

@app.route("/website")
def website():
    return "http://cameronyick.us"

@app.route("/search/<search_query>")
def search(search_query):
  return search_query

@app.route("/add/<x>/<y>")
def add(x,y):
  return str(int(x) + int(y)) #we can only return strings

# Handle
@app.errorhandler(404)
def not_found(error):
    return "Sorry, I haven't coded that yet.", 404

@app.errorhandler(500)
def internal_server_error(error):
    return "My code broke, my bad.", 500

# Forwards to localhost 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0")
