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

@app.route("/search/<search_query>")
def search(search_query):
  return search_query
 
if __name__ == "__main__":
    app.run()
