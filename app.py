from flask import Flask
from flask import request
import requests
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  if request.is_json:
    dataDict = request.get_json()
    req = requests.post('https://thingsboard.cloud/api/v1/Vxf3gbLjb0jhFtyz4kXJ/telemetry', data=dataDict)
    return 'Success'
  return 'Failed to extract payload'
