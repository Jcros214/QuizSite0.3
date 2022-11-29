# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
db: SQLAlchemy


from .static.python.getQuestions import QuestionSet, makeQuestions

global_questionset = QuestionSet(makeQuestions())

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        try:
            return User.query.get(int(user_id))
        except:
            pass

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    from .quiz import quiz as quiz_blueprint
    from .main import main as main_blueprint
    from .data import data as misc_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(misc_blueprint)



    


    # blueprint for non-auth parts of app
    # blueprint for quiz parts of app
    # blueprint for quiz parts of app
    

    return app

app = create_app()
# print(__name__)