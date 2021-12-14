from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    return 'Request is fucking json'
  return 'Fucking unreliable piece of shit'
