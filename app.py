from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return """<div style="width:100%; height:100%; display: flex; justify-content: center"><h1>HELLO WORLD</h1></div>"""

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
