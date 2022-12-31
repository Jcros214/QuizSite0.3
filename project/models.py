# from flask_login import UserMixin

# from . import db

# Column = db.Column
# Integer = db.Integer
# relationship = db.relationship
# ForeignKey = db.ForeignKey
# String = db.String

# import sqlalchemy
# db: sqlalchemy

# # from sqlalchemy import Column, ForeignKey, Integer, String, Date
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import relationship

# Base = db.Model

# class LogType(Base):
#     __tablename__ = 'logType'
#     id = Column(Integer, primary_key=True)
#     str_meaning = Column(String)

# class Log(Base):
#     __tablename__ = 'log'
#     id = Column(Integer, primary_key=True)
#     event_id = Column(Integer, ForeignKey('event.id'))
#     quiz_id = Column(Integer, ForeignKey('quiz.id'))
#     individual_id = Column(Integer, ForeignKey('individual.id'))
#     type_id = Column(Integer, ForeignKey('logType.id'))
#     event = relationship('Event')
#     quiz = relationship('Quiz')
#     individual = relationship('Individual')
#     log_type = relationship('LogType')

# class Question(Base):
#     __tablename__ = 'question'
#     id = Column(Integer, primary_key=True)
#     season_id = Column(Integer, ForeignKey('season.id'))
#     ques = Column(String)
#     ans = Column(String)
#     type = Column(String)
#     season = relationship('Season')

# class Season(Base):
#     __tablename__ = 'season'
#     id = Column(Integer, primary_key=True)
#     start_date = Column(Date)
#     material = Column(String)

# class Orginization(Base):
#     __tablename__ = 'orginization'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     prefix = Column(String)
#     address = Column(String)

# class Team(Base):
#     __tablename__ = 'team'
#     id = Column(Integer, primary_key=True)
#     org_id = Column(Integer, ForeignKey('orginization.id'))
#     name = Column(String)
#     orginization = relationship('Orginization')

# class Individual(Base):
#     __tablename__ = 'individual'
#     id = Column(Integer, primary_key=True)
#     team_id = Column(Integer, ForeignKey('team.id'))
#     fname = Column(String)
#     lname = Column(String)
#     dob = Column(Date)
#     role = Column(String)
#     team = relationship('Team')

# class Event(Base):
#     __tablename__ = 'event'
#     id = Column(Integer, primary_key=True)
#     season_id = Column(Integer, ForeignKey('season.id'))
#     date = Column(Date)
#     org_host = Column(Integer, ForeignKey('orginization.id'))
#     material = Column(String)
#     season = relationship('Season')
#     orginization = relationship('Orginization')


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     uname = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#     church = db.Column(db.String(1000))
#     team = db.Column(db.String(1000))
#     age = db.Column(db.Integer)
#     individualID = db.Column(db.Integer)

#     # Define the User data-model
#     roles = db.relationship('Role', secondary='user_roles')

# # Define the Role data-model
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), unique=True)


# # Define the UserRoles association table
# class UserRoles(db.Model):
#     __tablename__ = 'user_roles'
#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))





# # # models.py

# # # db structure:
# # # DB: PQA
# # # |_Orginization            Name,Prefix,Address
# # #   |_Rooms                 [^Org^],Name,SeatingCap
# # #   |_Team                  [^Org^],Name
# # #    |_Individual           [^Team^],Name,Role,B-day
# # # 
# # # |_EventType               HumanName,ShortName,HumanDiscription,args
# # #   
# # # |_Season                  Material,StartDate
# # #   |_Question              q,a,r,t
# # #   |_Event                 [^Season^],[^Host^],Date
# # #    |_Quiz                 [^Event^],[^Quizmaster],[^Team1^],[^Team2^],([^Team3^]),[^Room^]
# # #     |_QuizLog             [^Quiz^],([^Individual^]),[QuizRef.EventType],([^Question^]),questionnum
# # # 

# # # QuizLog:
# # #   Contains events (ie:)
# # #       In `quiz`, `individual` (answered_correct|answered_incorrect|recieved_foul|appealed|) to/on/for `question` asked as `questionNum`

# # from flask_login import UserMixin

# # from . import db

# # import sqlalchemy
# # db: sqlalchemy

# # class Orginization(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
# #     prefix = db.Column(db.String)
# #     address = db.Column(db.String)
# #     # Relationships
# #     rooms = db.relationship('Room')
# #     teams = db.relationship('Team')


# # class Room(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
    
# #     org = db.Column(db.Integer, db.ForeignKey('orginization.id'))

# # class Team(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)

# #     org = db.Column(db.Integer, db.ForeignKey('orginization.id'))

# #     individuals = db.relationship('Individual')

# # class Individual(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
# #     role = db.Column(db.String)
# #     birthday = db.Column(db.Date)

# #     team =  db.Column(db.Integer, db.ForeignKey('team.id'))


# # # class Season(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass

# # # class Question(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass
# # # class Event(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass

# # # class Quiz(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass

# # # class QuizLog(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass


# # # class EventType(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     pass


# # class User(UserMixin, db.Model):
# #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# #     uname = db.Column(db.String(100), unique=True)
# #     password = db.Column(db.String(100))
# #     name = db.Column(db.String(1000))
# #     church = db.Column(db.String(1000))
# #     team = db.Column(db.String(1000))
# #     age = db.Column(db.Integer)
# #     individualID = db.Column(db.Integer)

# #     # Define the User data-model
# #     roles = db.relationship('Role', secondary='user_roles')

# # # Define the Role data-model
# # class Role(db.Model):
# #     __tablename__ = 'roles'
# #     id = db.Column(db.Integer(), primary_key=True)
# #     name = db.Column(db.String(50), unique=True)


# # # Define the UserRoles association table
# # class UserRoles(db.Model):
# #     __tablename__ = 'user_roles'
# #     id = db.Column(db.Integer(), primary_key=True)
# #     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
# #     role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))





# # # # db.relationship('otherTable')


# # # class Orginization(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     name = db.Column(db.String)
# # #     prefix = db.Column(db.String)
# # #     address = db.Column(db.String)
# # #     teams = db.relationship('Team', lazy=True)

# # # class Team(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     name = db.Column(db.String)
# # #     orginization = db.Column(db.Integer, db.ForeignKey('orginization.id'))
# # #     individuals = db.relationship('Individual', lazy=True)

# # # class Individual(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     team = db.Column(db.Integer, db.ForeignKey('team.id'))
# # #     fname = db.Column(db.String)
# # #     lname = db.Column(db.String)
# # #     birthday = db.Column(db.Date)
# # #     role = db.Column(db.String)


# # # class Season(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     startDate = db.Column(db.Date)
# # #     material = db.Column(db.String)
# # #     events = db.relationship('Event', lazy=True)

# # # class Event(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     season = db.Column(db.Integer, db.ForeignKey('season.id'))
# # #     date = db.Column(db.Date)
# # #     host = db.Column(db.Integer, db.ForeignKey('orginization.id'))
# # #     quizzes = db.relationship('Quiz', lazy=True)

# # # class Quiz(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     event = db.Column(db.Integer, db.ForeignKey('event.id'))
# # #     room = db.Column(db.String)
# # #     quizmaster = db.Column(db.Integer, db.ForeignKey('individual.id'))
# # #     team1 = db.Column(db.Integer, db.ForeignKey('team.id'))
# # #     team2 = db.Column(db.Integer, db.ForeignKey('team.id'))

# # # class Log(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     quiz = db.Column(db.Integer, db.ForeignKey('orginization.id'))
# # #     question_number = db.Column(db.Integer)
# # #     question_asked = db.Column(db.Integer, db.ForeignKey('question.id'))
# # #     individual = db.Column(db.Integer, db.ForeignKey('question.id'))
# # #     type = db.Column(db.Integer)


# # # # class LogTypes(db.Model):
# # # {
# # #     'c': 'Correct',
# # #     'e': 'Incorrect',
# # #     't': 'Thrown out',
# # #     'f': 'foul'
# # # }

# # # class Question(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
# # #     q = db.Column(db.String)
# # #     a = db.Column(db.String)
# # #     r = db.Column(db.String)
# # #     t = db.Column(db.String)

# # # """
# # # CREATE TABLE [dbo].[logType] (
# # #     [ID]         INT           IDENTITY (1, 1) NOT NULL,
# # #     [StrMeaning] VARCHAR (255) NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC)
# # # );
# # # GO

# # # CREATE TABLE [dbo].[log] (
# # #     [ID]           INT IDENTITY (1, 1) NOT NULL,
# # #     [EventID]      INT NULL,
# # #     [QuizID]       INT NULL,
# # #     [IndividualID] INT NOT NULL,
# # #     [TypeID]       INT NOT NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC),
# # #     FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
# # #     FOREIGN KEY ([IndividualID]) REFERENCES [dbo].[individual] ([ID]),
# # #     FOREIGN KEY ([QuizID]) REFERENCES [dbo].[quiz] ([ID]),
# # #     FOREIGN KEY ([TypeID]) REFERENCES [dbo].[logType] ([ID])
# # # );
# # # GO

# # # CREATE TABLE [dbo].[question] (
# # #     [ID]        INT IDENTITY (1, 1) NOT NULL,
# # #     [SeasonID] INT           NULL,
# # #     [Ques]  VARCHAR (255) NOT NULL,
# # #     [Ans]    VARCHAR (255)  NOT NULL,
# # #     [Type]      VARCHAR (255) NULL
# # #     FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
# # # );
# # # GO


# # # -- Create tables
# # # CREATE TABLE [dbo].[season] (
# # #     [ID]        INT           IDENTITY (1, 1) NOT NULL,
# # #     [StartDate] DATE          NULL,
# # #     [Material]  VARCHAR (255) NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC)
# # # );
# # # GO

# # # CREATE TABLE [dbo].[orginization] (
# # #     [ID] INT IDENTITY (1, 1) NOT NULL,
# # #     [Name] VARCHAR (255) NOT NULL,
# # #     [Prefix] VARCHAR (255) NULL,
# # #     [Address] VARCHAR (255) NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC)
# # # );
# # # GO

# # # CREATE TABLE [dbo].[team] (
# # #     [ID]	INT IDENTITY (1, 1) NOT NULL,
# # #     [OrgID]	INT NULL,
# # #     [Name]	VARCHAR (255) NULL, --Full name
# # #     PRIMARY KEY CLUSTERED ([ID] ASC),
# # #     FOREIGN KEY ([OrgID]) REFERENCES [dbo].[orginization] ([ID])
# # # );
# # # GO

# # # CREATE TABLE [dbo].[individual] (
# # #     [ID]     INT           IDENTITY (1, 1) NOT NULL,
# # #     [TeamID] INT           NULL,
# # #     [FName]  VARCHAR (255) NULL,
# # #     [LName]  VARCHAR (255) NULL,
# # #     [DOB]    DATE          NULL,
# # #     [Role]   VARCHAR (255) NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC),
# # #     FOREIGN KEY ([TeamID]) REFERENCES [dbo].[team] ([ID])
# # # );
# # # GO
# # # CREATE TABLE [dbo].[event] (
# # #     [ID]       INT           IDENTITY (1, 1) NOT NULL,
# # #     [SeasonID] INT           NULL,
# # #     [Date]     DATE          NULL,
# # #     [OrgHost]  INT           NULL,
# # #     [Material] VARCHAR (255) NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC),
# # #     FOREIGN KEY ([OrgHost]) REFERENCES [dbo].[orginization] ([ID]),
# # #     FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
# # # );
# # # GO
# # # CREATE TABLE [dbo].[quiz] (
# # #     [ID]           INT           IDENTITY (1, 1) NOT NULL,
# # #     [EventID]      INT           NULL,
# # #     [RoomName]     VARCHAR (255) NULL,
# # #     [QuizmasterID] INT           NULL,
# # #     [TeamID1]      INT           NULL,
# # #     [TeamID2]      INT           NULL,
# # #     PRIMARY KEY CLUSTERED ([ID] ASC),
# # #     FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
# # #     FOREIGN KEY ([QuizmasterID]) REFERENCES [dbo].[individual] ([ID]),
# # #     FOREIGN KEY ([TeamID1]) REFERENCES [dbo].[team] ([ID]),
# # #     FOREIGN KEY ([TeamID2]) REFERENCES [dbo].[team] ([ID])
# # # );
# # # GO

# # # """