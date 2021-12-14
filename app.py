from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/', methods=['POST'])

def postJsonHandler():
  return 'Fucking unreliable piece of shit'
