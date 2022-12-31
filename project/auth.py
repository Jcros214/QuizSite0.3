# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .new_models import User
from . import db

auth = Blueprint('auth', __name__) 

# # @auth.route('/createAdmin')
# # def createAdmin():
# #     # create new user with the form data. Hash the password so plaintext version isn't saved.
# #     church, team, name, age, uname, password = 'COG', 'N/A', 'SA', 0, 'admin', 'password' 
# #     new_user = User(church=church, team=team, name=name, age=age, uname=uname, password=generate_password_hash(password, method='sha256'))

# #     # new_user.church = church
# #     # new_user.team = team
# #     # new_user.age = age

# #     # add the new user to the database
# #     db.session.add(new_user)
# #     db.session.commit()

# #     return redirect(url_for('auth.login'))

# @auth.route('/login')  
# def login():
#     return render_template('login.html')

# @auth.route('/login', methods=['POST'])
# def login_post():
#     args = request.form
#     # print(args)
#     uname, password = args.get('uname'), args.get('password')

#     remember = True if request.form.get('remember') else False

    

#     user = User.query.filter_by(uname=uname).first()

#     # check if user actually exists
#     # take the user supplied password, hash it, and compare it to the hashed password in database
#     # try:
#     #     # print(user)
#     #     # print(password)
#     #     # print(user.password)
#     # except:
#     #     print("User not found or password incorrect")
#     if not user or not check_password_hash(user.password, password): 
#         flash('Please check your login details and try again.')
#         return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

#     # if the above check passes, then we know the user has the right credentials
#     login_user(user, remember=remember)
#     return redirect(url_for('main.profile'))

# @auth.route('/signup')
# def signup():
#     return render_template('signup.html', churches=['COG', 'Comm'])

# @auth.route('/signup', methods=['POST'])
# def signup_post():
#     # print('\n\n')
#     # print(request.form)

#     args = request.form
#     church, team, name, age, uname, password = args['church'], args['team'], args['name'], args['age'], args['uname'], args['password']

#     # print('\n', church, team, name, age, username, password, '\n')

#     user = User.query.filter_by(uname=uname).first() # if this returns a user, then the uname already exists in database

#     if user: # if a user is found, we want to redirect back to signup page so user can try again  
#         flash('Username address already exists')
#         return redirect(url_for('auth.signup'))

#     # create new user with the form data. Hash the password so plaintext version isn't saved.
#     new_user = User(church=church, team=team, name=name, age=age, uname=uname, password=generate_password_hash(password, method='sha256'))

#     # new_user.church = church
#     # new_user.team = team
#     # new_user.age = age

#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect(url_for('auth.login'))

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))





from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required


# configure the login manager
login_manager = LoginManager()
login_manager.init_app(auth)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['uname']
        password = request.form['password']
        church_id = request.form['church']
        team_id = request.form['team_id']
        age = request.form['age']
        role_id = request.form['role_id']
        user = User(name=name, username=username, password=password, church_id=church_id, team_id=team_id, age=age, role_id=role_id)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        from .new_models import Organization, Team
        churches = Organization.query.all()
        teams = Team.query.all()
        return render_template('register.html', churches=churches, teams=teams)
        

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/')
@login_required
def index():
    return render_template('index.html')
