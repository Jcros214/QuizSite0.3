# from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

from . import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    shorthand = db.Column(db.String(10), nullable=False)
    teams = db.relationship('Team', backref=db.backref('organization', lazy=True))
    rooms = db.relationship('Room', backref=db.backref('organization', lazy=True))

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    members = db.relationship('Member', backref=db.backref('team', lazy=True))

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    role = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    questions = db.relationship('Question', backref=db.backref('season', lazy=True))
    events = db.relationship('Event', backref=db.backref('season', lazy=True))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q = db.Column(db.String, nullable=False)
    a = db.Column(db.String, nullable=False)
    r = db.Column(db.String, nullable=False)
    t = db.Column(db.String, nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    season = db.relationship('Season', backref=db.backref('events', lazy=True))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    organization = db.relationship('Organization', backref=db.backref('events', lazy=True))
    quiz = db.relationship('Quiz', uselist=False, backref=db.backref('event', uselist=False))

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quizmaster_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    quizmaster = db.relationship('Member', backref=db.backref('quizzes', lazy=True))
    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team1 = db.relationship('Team', backref=db.backref('quizzes1', lazy=True))
    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2 = db.relationship('Team', backref=db.backref('quizzes2', lazy=True))
    team3_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team3 = db.relationship('Team', backref=db.backref('quizzes3', lazy=True))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('quizzes', lazy=True))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    event = db.relationship('Event', backref=db.backref('quiz', uselist=False))
    logs = db.relationship('QuizLog', backref='quiz', lazy=True)

class QuizLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    member = db.relationship('Member', backref=db.backref('quiz_logs', lazy=True))
    type = db.Column(db.String, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', backref=db.backref('quiz_logs', lazy=True))
    question_number = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    church = db.relationship('Organization', backref=db.backref('users', lazy=True))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team = db.relationship('Team', backref=db.backref('users', lazy=True))
    age = db.Column(db.Integer, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'), nullable=False)
    role = db.relationship('UserRoles', backref=db.backref('users', lazy=True))

    def has_role(self, role_name):
        return self.role.name == role_name

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


