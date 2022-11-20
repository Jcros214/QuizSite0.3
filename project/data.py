from flask import Blueprint, render_template, request
from . import global_questionset

data = Blueprint('data', __name__)

@data.route('/practice')
def index():
	try:
		chaplist = str(request.args.get('chapters')).split(",")
	except:
		print("I assume there could be problems here...")
		

	render_template('practice/practice_questions.html', global_questionset.getQuestions(10, chaplist))

@data.route('/dev')
def dev():
	return render_template('dev.html')