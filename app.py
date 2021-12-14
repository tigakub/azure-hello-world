from flask import Flask
from flask import request
import json

#thingsboard_url = "https://thingsboard.cloud/api/v1/1nVPRLsj7bhDTGKLOidD/telemetry"

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def postJsonHandler():
  if request.is_json:
    post_data = request.get_json()
    return post_data['voltage_1']
    #repost = requests.post(thingsboard_url, json=post_data)
    #return repost.status_code
