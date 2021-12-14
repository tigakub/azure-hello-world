from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    data = request.get_json()
    v1 = data['voltage_1']
    return v1
  return 'Fucking unreliable piece of shit'
