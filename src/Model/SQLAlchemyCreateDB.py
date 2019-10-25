from app import db, generate_password_hash
import uuid


class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    PublicID = db.Column(db.String(100), nullable=False)
    Username = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(80), nullable=False)
    FName = db.Column(db.String(50), nullable=False)
    LName = db.Column(db.String(50))
    Grade = db.Column(db.Integer)  # 1, 2, 3
    Role = db.Column(db.String(20))  # 'Admin' (only 1), 'Prof', 'Stud'


class Question(db.Model):
    QuestionID = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(500), nullable=False)
    Answer = db.Column(db.String(100))
    Grade = db.Column(db.Integer)
    ProfPublicID = db.Column(db.Integer)
    SubmittedOn = db.Column(db.Date)


class HistoryQuestion(db.Model):
    HisID = db.Column(db.Integer, primary_key=True)
    HisQuestionID = db.Column(db.Integer, nullable=False)
    StudPublicID = db.Column(db.Integer, nullable=False)
    AttemptedAns = db.Column(db.String(50))
    Result = db.Column(db.Boolean)
    SubmittedOn = db.Column(db.Date)


def FirstRun():
    db.create_all()
    FirstUser = \
        User(
            PublicID=str(uuid.uuid4()),
            Username='Admin',
            Password=generate_password_hash('password', method='sha256'),
            FName='Vaibhav',
            LName='Singhal',
            Grade=1,
            Role='Admin'
        )
    db.session.add(FirstUser)
    db.session.commit()


'''
how to add user
dir -> where SQLAlchemyCreateDB is located

import SQLAlchemyCreateDB as sql
from SQLAlchemyCreateDB import generate_password_hash
import uuid

user = \
    sql.User(
        PublicID=str(uuid.uuid4()),
        Username='<UniqueUserName>',
        Password=generate_password_hash('<Password>', method='sha256'),
        FName='<FName>',
        LName='<LName>',
        Grade=1/2/3,
        Role='Prof'/'Stud'
    )
sql.db.session.add(user)
sql.db.session.commit()


to check if its working (Install sqlite3)
dir -> where SQLAlchemyCreateDB is located
sqlite3 DataBase.db
.tables  # to see all the tables
select * from User  # To see PublicID if needed

'''
