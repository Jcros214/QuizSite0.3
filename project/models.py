# from sqlalchemy import Column, Integer, VARCHAR
# import sqlalchemy as db


# models.py

# db structure:
# DB: PQA
# |_Orginization            Name,Prefix,Address
#   |_Rooms                 [^Org^],Name,SeatingCap
#   |_Team                  [^Org^],Name
#    |_Individual           [^Team^],Name,Role,B-day
# 
# |_EventType               HumanName,ShortName,HumanDiscription,args
#   
# |_Season                  Material,StartDate
#   |_Question              q,a,r,t
#   |_Event                 [^Season^],[^Host^],Date
#    |_Quiz                 [^Event^],[^Quizmaster],[^Team1^],[^Team2^],([^Team3^]),[^Room^]
#     |_QuizLog             [^Quiz^],([^Individual^]),[QuizRef.EventType],([^Question^]),questionnum
# 

# QuizLog:
#   Contains events (ie:)
#       In `quiz`, `individual` (answered_correct|answered_incorrect|recieved_foul|appealed|) to/on/for `question` asked as `questionNum`

from flask_login import UserMixin
from . import db


class Orginization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    prefix = db.Column(db.String)
    address = db.Column(db.String)
    # Relationships
    rooms = db.relationship('Room')
    teams = db.relationship('Team')


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    org = db.Column(db.Integer, db.ForeignKey('orginization.id'))

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    org = db.Column(db.Integer, db.ForeignKey('orginization.id'))

    individuals = db.relationship('Individual')

class Individual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    birthday = db.Column(db.Date)

    team =  db.Column(db.Integer, db.ForeignKey('team.id'))


# class Season(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass
# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass

# class QuizLog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass


# class EventType(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pass


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    uname = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    church = db.Column(db.String(1000))
    team = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    individualID = db.Column(db.Integer)





# # db.relationship('otherTable')


# class Orginization(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     name = db.Column(db.String)
#     prefix = db.Column(db.String)
#     address = db.Column(db.String)
#     teams = db.relationship('Team', lazy=True)

# class Team(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     name = db.Column(db.String)
#     orginization = db.Column(db.Integer, db.ForeignKey('orginization.id'))
#     individuals = db.relationship('Individual', lazy=True)

# class Individual(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     team = db.Column(db.Integer, db.ForeignKey('team.id'))
#     fname = db.Column(db.String)
#     lname = db.Column(db.String)
#     birthday = db.Column(db.Date)
#     role = db.Column(db.String)


# class Season(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     startDate = db.Column(db.Date)
#     material = db.Column(db.String)
#     events = db.relationship('Event', lazy=True)

# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     season = db.Column(db.Integer, db.ForeignKey('season.id'))
#     date = db.Column(db.Date)
#     host = db.Column(db.Integer, db.ForeignKey('orginization.id'))
#     quizzes = db.relationship('Quiz', lazy=True)

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     event = db.Column(db.Integer, db.ForeignKey('event.id'))
#     room = db.Column(db.String)
#     quizmaster = db.Column(db.Integer, db.ForeignKey('individual.id'))
#     team1 = db.Column(db.Integer, db.ForeignKey('team.id'))
#     team2 = db.Column(db.Integer, db.ForeignKey('team.id'))

# class Log(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     quiz = db.Column(db.Integer, db.ForeignKey('orginization.id'))
#     question_number = db.Column(db.Integer)
#     question_asked = db.Column(db.Integer, db.ForeignKey('question.id'))
#     individual = db.Column(db.Integer, db.ForeignKey('question.id'))
#     type = db.Column(db.Integer)


# # class LogTypes(db.Model):
# {
#     'c': 'Correct',
#     'e': 'Incorrect',
#     't': 'Thrown out',
#     'f': 'foul'
# }

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     q = db.Column(db.String)
#     a = db.Column(db.String)
#     r = db.Column(db.String)
#     t = db.Column(db.String)

# """
# CREATE TABLE [dbo].[logType] (
#     [ID]         INT           IDENTITY (1, 1) NOT NULL,
#     [StrMeaning] VARCHAR (255) NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC)
# );
# GO

# CREATE TABLE [dbo].[log] (
#     [ID]           INT IDENTITY (1, 1) NOT NULL,
#     [EventID]      INT NULL,
#     [QuizID]       INT NULL,
#     [IndividualID] INT NOT NULL,
#     [TypeID]       INT NOT NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC),
#     FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
#     FOREIGN KEY ([IndividualID]) REFERENCES [dbo].[individual] ([ID]),
#     FOREIGN KEY ([QuizID]) REFERENCES [dbo].[quiz] ([ID]),
#     FOREIGN KEY ([TypeID]) REFERENCES [dbo].[logType] ([ID])
# );
# GO

# CREATE TABLE [dbo].[question] (
#     [ID]        INT IDENTITY (1, 1) NOT NULL,
#     [SeasonID] INT           NULL,
#     [Ques]  VARCHAR (255) NOT NULL,
#     [Ans]    VARCHAR (255)  NOT NULL,
#     [Type]      VARCHAR (255) NULL
#     FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
# );
# GO


# -- Create tables
# CREATE TABLE [dbo].[season] (
#     [ID]        INT           IDENTITY (1, 1) NOT NULL,
#     [StartDate] DATE          NULL,
#     [Material]  VARCHAR (255) NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC)
# );
# GO

# CREATE TABLE [dbo].[orginization] (
#     [ID] INT IDENTITY (1, 1) NOT NULL,
#     [Name] VARCHAR (255) NOT NULL,
#     [Prefix] VARCHAR (255) NULL,
#     [Address] VARCHAR (255) NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC)
# );
# GO

# CREATE TABLE [dbo].[team] (
#     [ID]	INT IDENTITY (1, 1) NOT NULL,
#     [OrgID]	INT NULL,
#     [Name]	VARCHAR (255) NULL, --Full name
#     PRIMARY KEY CLUSTERED ([ID] ASC),
#     FOREIGN KEY ([OrgID]) REFERENCES [dbo].[orginization] ([ID])
# );
# GO

# CREATE TABLE [dbo].[individual] (
#     [ID]     INT           IDENTITY (1, 1) NOT NULL,
#     [TeamID] INT           NULL,
#     [FName]  VARCHAR (255) NULL,
#     [LName]  VARCHAR (255) NULL,
#     [DOB]    DATE          NULL,
#     [Role]   VARCHAR (255) NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC),
#     FOREIGN KEY ([TeamID]) REFERENCES [dbo].[team] ([ID])
# );
# GO
# CREATE TABLE [dbo].[event] (
#     [ID]       INT           IDENTITY (1, 1) NOT NULL,
#     [SeasonID] INT           NULL,
#     [Date]     DATE          NULL,
#     [OrgHost]  INT           NULL,
#     [Material] VARCHAR (255) NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC),
#     FOREIGN KEY ([OrgHost]) REFERENCES [dbo].[orginization] ([ID]),
#     FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
# );
# GO
# CREATE TABLE [dbo].[quiz] (
#     [ID]           INT           IDENTITY (1, 1) NOT NULL,
#     [EventID]      INT           NULL,
#     [RoomName]     VARCHAR (255) NULL,
#     [QuizmasterID] INT           NULL,
#     [TeamID1]      INT           NULL,
#     [TeamID2]      INT           NULL,
#     PRIMARY KEY CLUSTERED ([ID] ASC),
#     FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
#     FOREIGN KEY ([QuizmasterID]) REFERENCES [dbo].[individual] ([ID]),
#     FOREIGN KEY ([TeamID1]) REFERENCES [dbo].[team] ([ID]),
#     FOREIGN KEY ([TeamID2]) REFERENCES [dbo].[team] ([ID])
# );
# GO

# """