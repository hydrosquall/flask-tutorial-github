from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "Pete Penguin"

@app.route("/website")
def website():
    return "http://www.google.com"

@app.route("/linkamp")
def linkamp():
    return "Hello, Dan Shao"

@app.route("/search/<search_query>")
def search(search_query):
  return search_query

# Handle
@app.errorhandler(404)
def not_found(error):
    return "Sorry, I haven't coded that yet.", 404

@app.errorhandler(500)
def internal_server_error(error):
    return "My code broke, my bad.", 500
 
if __name__ == "__main__":
    app.run()
