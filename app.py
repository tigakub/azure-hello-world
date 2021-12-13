from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
  return "<html><head><title>Azure Python Web App</title></head><body><h1>Hello, World!</h1></body></html>"
