from app import db, UserMixin
from werkzeug.security import generate_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(80), nullable=False)
    FName = db.Column(db.String(50), nullable=False)
    LName = db.Column(db.String(50))
    Grade = db.Column(db.Integer)  # 1, 2, 3
    Role = db.Column(db.String(20))  # 'Admin' (only 1), 'Prof', 'Stud'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(500), nullable=False)
    Answer = db.Column(db.String(100))
    Grade = db.Column(db.Integer)
    ProfID = db.Column(db.Integer)
    SubmittedOn = db.Column(db.Date)


class HistoryQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    His_QuesID = db.Column(db.Integer, nullable=False)
    StudID = db.Column(db.Integer, nullable=False)
    AttemptedAns = db.Column(db.String(50))
    Result = db.Column(db.Boolean)
    SubmittedOn = db.Column(db.Date)


def FirstRun():
    db.create_all()
    FirstUser = \
        User(
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

# from werkzeug.security import check_password_hash
# usr = \
#     User(
#         Username='std1',
#         Password=generate_password_hash('pass', method='sha256'),
#         FName='namit',
#         LName='aneja',
#         Grade=1,
#         Role='Stud'
#     )
# db.session.add(usr)
# db.session.commit()

# from werkzeug.security import check_password_hash
# usr = \
#     User(
#         Username='prof1',
#         Password=generate_password_hash('pass', method='sha256'),
#         FName='Akhil',
#         LName='',
#         Grade=1,
#         Role='Prof'
#     )
# db.session.add(usr)
# db.session.commit()
