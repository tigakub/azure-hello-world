from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
  return "Hello, world! The source code for this is continuously deployed."
