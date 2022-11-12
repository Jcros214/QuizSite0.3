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


# DUMP:
"""
INSERT INTO user VALUES(1,'admin','sha256$y4k261mZQVqXv3IX$02421bd5ec162e3e5d820d44cdecac1e0f2cd1187339aeaed17dc9816b44d462','','','','',NULL);
"""

"""
INSERT INTO user VALUES(1,'admin','sha256$D35bsSmg96MFDzCS$8a168f085034e7f000d8c727f8af90ec877e5883493a6a43e45be15bc8946645','SA','','',0);
INSERT INTO user VALUES(2,'Landyn M.','sha256$UAuadyA5R4BbDqA8$b549c4a6e7ec65bac9787102e8fe96317d378cd793c66aa40d77c0386e85ef4b','','','','');
INSERT INTO user VALUES(3,'Jrunger','sha256$338g5VmCt8tYlvGs$022f8afbc6e6033a9038d230bc31ef4fa89d1b43380b1653b1c07c5b22bc7344','Jonah Unger','The church of Greenville','Zealous',20);
"""