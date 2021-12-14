from flask import Flask
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def hello():
  return 'Fucking unreliable piece of shit'
