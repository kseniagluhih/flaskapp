from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><head></head><body><h1>Hello!!!</h1></body></html>"

@app.route("/data_to")
def data_to():
	some_pars = {'user': 'Ksenia', 'color': 'blue'}
	some_str = 'Hello for all!'
	some_value = 10
	return render_template(
		'simple.html', 
		some_str=some_str, 
		some_pars=some_pars,
		some_value=some_value)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

