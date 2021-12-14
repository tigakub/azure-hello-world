from flask import Flask
from flask import request
import json

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def postJsonHandler():
  if request.is_json:
    post_data = request.get_json()
    return 'JSON posted'

