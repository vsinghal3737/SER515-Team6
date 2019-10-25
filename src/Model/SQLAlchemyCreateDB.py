'''

DO NOT RUN THIS FILE

'''
from app import db, generate_password_hash
import uuid


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80), nullable=False)
    FName = db.Column(db.String(50), nullable=False)
    LName = db.Column(db.String(50))
    Phone = db.Column(db.Integer)
    Grade = db.Column(db.Integer)
    Role = db.Column(db.String(20))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(500), nullable=False)
    Answer = db.Column(db.String(100))
    Grade = db.Column(db.String(50))
    ProfID = db.Column(db.Integer)
    SubmittedOn = db.Column(db.Date)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, nullable=False)
    HISID_QuestionID = db.Column(db.Integer, nullable=False)
    AttemptedAns = db.Column(db.String(50))
    SubmittedOn = db.Column(db.Date)


def firstRun():
    db.create_all()
    FirstUser = \
        User(
            public_id=str(uuid.uuid4()),
            username='Admin',
            password=generate_password_hash('password', method='sha256'),
            FName='Vaibhav',
            LName='Singhal',
            Phone=1234567890,
            Grade=1,
            Role='Admin'
        )
    db.session.add(FirstUser)
    db.session.commit()
