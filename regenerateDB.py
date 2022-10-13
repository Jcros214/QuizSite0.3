import os
from time import sleep
from project import db, create_app, models
os.getcwd()
os.remove('/Users/jon/Documents/DEV/pythonanywhere/QuizSite0.3/project/db.sqlite')
sleep(3)
db.create_all(app=create_app()) # pass the app result so Flask-SQLAlchemy gets the configuration.
