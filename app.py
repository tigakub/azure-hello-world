from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    data = request.get_json()
    return 'Fuck Microsoft to infinity'
  return 'Fucking unreliable piece of shit'
