from flask import Flask
from flask import request
import requests
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    dataDict = request.get_json()
    headers = {'Content-Type': 'application/json'} 
    req = requests.post('https://thingsboard.cloud/api/v1/Vxf3gbLjb0jhFtyz4kXJ/telemetry', json=dataDict, headers=headers)
    return req.text
  return 'Failed to extract payload'
