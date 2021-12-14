from flask import Flask
from flask import request
import json

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def postJsonHandler():
  return "Hello world!"
