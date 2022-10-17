import os
from time import sleep
from project import db, create_app, models

try:
	os.remove('QuizSite0.3/project/db.sqlite')
except:
	pass
os.getcwd()
sleep(3)
db.create_all(app=create_app()) # pass the app result so Flask-SQLAlchemy gets the configuration.
