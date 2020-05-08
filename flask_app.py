import os

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask import request
from flask import Response
import base64
from PIL import Image
from io import BytesIO
import json


import image_recognition as neuronet

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdPXfQUAAAAAFT8uzmNl3tPW4zNZBe8zJf9tgFO',
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdPXfQUAAAAAI4qQv1wEIH6TuWPPehbLJ6obOa0'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
Bootstrap(app)

# fcount, fimage = neuronet.read_image_files(10, './static')
# decode = neuronet.getresult(fimage)


class NetForm(FlaskForm):
	openid = StringField('Openid', validators=[DataRequired()])
	upload = FileField('Load image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
	# recaptcha = RecaptchaField()
	submit = SubmitField('send')


@app.route("/")
def hello():
	return "<html><head></head><body><h1>Hello!!!</h1></body></html>"


@app.route("/data_to")
def data_to():
	some_pars = {'user': 'Ksenia', 'color': 'blue'}
	some_str = 'Hello for all!'
	some_value = 10
	return render_template('simple.html', some_str=some_str, some_pars=some_pars,some_value=some_value)


@app.route("/net", methods=['GET', 'POST'])
def net():
	form = NetForm()
	filename = None
	neurodic = {}
	if form.validate_on_submit():
		filename = os.path.join('./static', secure_filename(form.upload.data.filename))
		fcount, fimage = neuronet.read_image_files(10, './static')
		decode = neuronet.getresult(fimage)
		for elem in decode:
			neurodic[elem[0][1]] = elem[0][2]
		form.upload.data.save(filename)
	return render_template('net.html', form=form, image_name=filename, neurodic=neurodic)


@app.route("/apinet", methods=["GET", "POST"])
def apinet():
	if request.mimetype == "application/json":
		data = request.get_json()
		filebytes = data['imagebin'].encode('utf-8')
		cfile = base64.b64decode(filebytes)
		img = Image.open(BytesIO(cfile))
		decode = neuronet.getresult([img])
		neurodic = {}
		for elem in decode:
			neurodic[elem[0][1]] = elem[0][2]
			print(elem)
		ret = json.dumps(neurodic)
		resp = Response(response=ret, status=200, mimetype="application/json")
		return resp


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000)

