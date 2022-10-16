# models.py

from flask_login import UserMixin
from . import db

# from sqlalchemy import Column, Int

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    uname = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    church = db.Column(db.String(1000))
    team = db.Column(db.String(1000))
    age = db.Column(db.Integer)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    startDate = db.Column(db.Date)
    material = ()

"""-- Create tables
CREATE TABLE [dbo].[season] (
	[ID]        INT           IDENTITY (1, 1) NOT NULL,
	[StartDate] DATE          NULL,
	[Material]  VARCHAR (255) NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC)
);
GO

CREATE TABLE [dbo].[orginization] (
	[ID] INT IDENTITY (1, 1) NOT NULL,
	[Name] VARCHAR (255) NOT NULL,
	[Prefix] VARCHAR (255) NULL,
	[Address] VARCHAR (255) NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC)
);
GO

CREATE TABLE [dbo].[team] (
	[ID]	INT IDENTITY (1, 1) NOT NULL,
	[OrgID]	INT NULL,
	[Name]	VARCHAR (255) NULL, --Full name
	PRIMARY KEY CLUSTERED ([ID] ASC),
	FOREIGN KEY ([OrgID]) REFERENCES [dbo].[orginization] ([ID])
);
GO

CREATE TABLE [dbo].[individual] (
	[ID]     INT           IDENTITY (1, 1) NOT NULL,
	[TeamID] INT           NULL,
	[FName]  VARCHAR (255) NULL,
	[LName]  VARCHAR (255) NULL,
	[DOB]    DATE          NULL,
	[Role]   VARCHAR (255) NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC),
	FOREIGN KEY ([TeamID]) REFERENCES [dbo].[team] ([ID])
);
GO

CREATE TABLE [dbo].[event] (
	[ID]       INT           IDENTITY (1, 1) NOT NULL,
	[SeasonID] INT           NULL,
	[Date]     DATE          NULL,
	[OrgHost]  INT           NULL,
	[Material] VARCHAR (255) NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC),
	FOREIGN KEY ([OrgHost]) REFERENCES [dbo].[orginization] ([ID]),
	FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
);
GO

CREATE TABLE [dbo].[quiz] (
	[ID]           INT           IDENTITY (1, 1) NOT NULL,
	[EventID]      INT           NULL,
	[RoomName]     VARCHAR (255) NULL,
	[QuizmasterID] INT           NULL,
	[TeamID1]      INT           NULL,
	[TeamID2]      INT           NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC),
	FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
	FOREIGN KEY ([QuizmasterID]) REFERENCES [dbo].[individual] ([ID]),
	FOREIGN KEY ([TeamID1]) REFERENCES [dbo].[team] ([ID]),
	FOREIGN KEY ([TeamID2]) REFERENCES [dbo].[team] ([ID])
);
GO

CREATE TABLE [dbo].[logType] (
	[ID]         INT           IDENTITY (1, 1) NOT NULL,
	[StrMeaning] VARCHAR (255) NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC)
);
GO

CREATE TABLE [dbo].[log] (
	[ID]           INT IDENTITY (1, 1) NOT NULL,
	[EventID]      INT NULL,
	[QuizID]       INT NULL,
	[IndividualID] INT NOT NULL,
	[TypeID]       INT NOT NULL,
	PRIMARY KEY CLUSTERED ([ID] ASC),
	FOREIGN KEY ([EventID]) REFERENCES [dbo].[event] ([ID]),
	FOREIGN KEY ([IndividualID]) REFERENCES [dbo].[individual] ([ID]),
	FOREIGN KEY ([QuizID]) REFERENCES [dbo].[quiz] ([ID]),
	FOREIGN KEY ([TypeID]) REFERENCES [dbo].[logType] ([ID])
);
GO

CREATE TABLE [dbo].[question] (
	[ID]        INT IDENTITY (1, 1) NOT NULL,
	[SeasonID] INT           NULL,
	[Ques]  VARCHAR (255) NOT NULL,
	[Ans]    VARCHAR (255)  NOT NULL,
	[Type]      VARCHAR (255) NULL
	FOREIGN KEY ([SeasonID]) REFERENCES [dbo].[season] ([ID])
);
GO"""