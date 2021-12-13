from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	var result = "<html><head><title>Hello World, Python Test App</title></head>\\n<body><h1>Hello, World!</h1><p>From python via Azure.</p></body></html>\\n"
	return result

