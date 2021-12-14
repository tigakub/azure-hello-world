from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    payload = request.get_json()
    if payload == None:
      return 'Failed to retrieve json payload'
    v1 = payload.get('voltage_1')
    if v1 == None:
      return 'Failed to retrieve voltage_1 from payload'
    return v1
  return 'Fucking unreliable piece of shit'
