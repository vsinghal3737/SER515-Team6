from flask import jsonify
import SQLAlchemyCreateDB as sql
from sqlalchemy.sql.expression import false, true
from DummyQuestions import Questions


def addQuestion(Question):
    sql.db.session.add(
        sql.Question(
            QuestionID=Question['QuestionID'],
            Question=Question['Question'],
            Answer=Question['Answer'],
            Grade=Question['Grade'],
            ProfPublicID=Question['ProfPublicID'],
            SubmittedOn=Question['SubmittedOn']
        )
    )
    sql.db.commit()
    return True


'''
remove all from questions which contains this unique(
    studentID filter
    remove True attempted
    get unique
)
'''


def getQuestionPerStud(PublicID):
    user = sql.User.query.filter_by(PublicID=PublicID).first()

    submittedQuestions = list(set(map(
        lambda x: x[1],
        sql.HistoryQuestion.query.filter_by(StudPublicID=user[1]).filter_by(Result=True).all()
    )))

    Questions = {
        row[0]: {
            'QuestionID': row[0],
            'Question': row[1],
            'Answer': '',
            'Grade': row[3],
            'ProfPublicID': row[4],
            'SubmittedOn': ''
        } for row in sql.Question.query.filter_by(Grade=user[6]).all() if row[0] not in submittedQuestions
    }
    return jsonify({'questions': Questions})


def getQuestion(PublicID):
    user = sql.User.query.filter_by(PublicID=PublicID).first()
    Questions = {
        row[0]: {
            'QuestionID': row[0],
            'Question': row[1],
            'Answer': row[2],
            'Grade': row[3],
            'ProfPublicID': row[4],
            'SubmittedOn': row[5]
        } for row in sql.Question.query.filter_by(Grade=user[6]).all()
    }
    return jsonify({'questions': Questions})


def getHistQuestion(PublicID):
    userID = sql.User.query.filter_by(PublicID=PublicID).first()[1]

    Questions = {
        row[0]: {
            'HisID': row[0],
            'HisQuestionID': row[1],
            'StudPublicID': row[2],
            'AttemptedAns': row[3],
            'Result': 'Pass' if row[4] is True else 'Fail',
            'SubmittedOn': row[5]
        } for row in sql.HistoryQuestion.query.filter_by(StudPublicID=userID).all()
    }
    return jsonify({'questions': Questions})


def DummyRun():
    for i in Questions.keys():
        addQuestion(Questions[i])
