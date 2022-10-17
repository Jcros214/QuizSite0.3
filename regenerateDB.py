import os
from time import sleep
from project import db, create_app, models
from werkzeug.security import generate_password_hash
from project.models import User
# from project.auth import create_user

try:
	os.remove('QuizSite0.3/project/db.sqlite')
except:
	pass
os.getcwd()
# sleep(3)
db.create_all(app=create_app()) # pass the app result so Flask-SQLAlchemy gets the configuration.

# church, team, name, age, uname, password = '', '', 'SA', 0, 'admin', 'password' 
# create_user(church=church, team=team, name=name, age=age, uname=uname, password=generate_password_hash(password, method='sha256'))
