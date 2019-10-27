from flask import jsonify
import SQLAlchemyCreateDB as sql
from datetime import datetime


class QuestionsConnection:
    @classmethod
    def addQuestion(cls, question):
        x = question['SubmittedOn']
        sql.db.session.add(
            sql.Question(
                Question=question['Question'],
                Answer=question['Answer'],
                Grade=question['Grade'],
                ProfID=question['ProfID'],
                SubmittedOn=datetime(int(x[0:4]), int(x[5:7]), int(x[8:10]), int(x[11:13]), int(x[14:16]), int(x[17:19]))
            )
        )
        sql.db.session.commit()
        return True

    @classmethod
    def addHistoryQuestion(cls, question):
        x = question['SubmittedOn']
        sql.db.session.add(
            sql.HistoryQuestion(
                His_QuesID=question['His_QuesID'],
                StudID=question['StudID'],
                AttemptedAns=question['AttemptedAns'],
                Result=True if question['Result'] == 'Pass' else False,
                SubmittedOn=datetime(int(x[0:4]), int(x[5:7]), int(x[8:10]), int(x[11:13]), int(x[14:16]), int(x[17:19]))
            )
        )
        sql.db.session.commit()
        return True

    @classmethod
    def getQuestionPerStud(cls, username):
        '''
        remove all from questions which contains this unique(
            studentID filter
            remove True attempted
            get unique
        )
        '''
        user = sql.User.query.filter_by(Username=username).first()

        submitted_questions = list(set(map(
            lambda x: x[1],
            sql.HistoryQuestion.query.filter_by(StudID=user[0]).filter_by(Result=True).all()
        )))

        questions = {
            row[0]: {
                'id': row[0],
                'question': row[1],
                'answer': row[2],
                'grade': row[3],
                'prof_id': row[4],
                'submitted_on': row[5]
            } for row in sql.Question.query.filter_by(Grade=user[5]).all() if row[0] not in submitted_questions
        }
        return jsonify({'questions': questions})

    @classmethod
    def getQuestionPerGrade(cls, grade):
        questions = {
            row[0]: {
                'id': row[0],
                'question': row[1],
                'answer': row[2],
                'grade': row[3],
                'prof_id': row[4],
                'submitted_on': row[5]
            } for row in sql.Question.query.filter_by(Grade=grade).all()
        }
        return jsonify({'questions': questions})

    @classmethod
    def getHistQuestion(cls, username):
        user_id = sql.User.query.filter_by(Username=username).first()[0]
        questions = {
            row[0]: {
                'id': row[0],
                'his_question_id': row[1],
                'stud_id': row[2],
                'attempted_ans': row[3],
                'result': 'Pass' if row[4] is True else 'Fail',
                'submitted_on': row[5]
            } for row in sql.HistoryQuestion.query.filter_by(StudID=user_id).all()
        }
        return jsonify({'questions': questions})


def DummyRun():
    from DummyQuestions import dummy_questions as dq, Dummy_history_questions as dhq

    for i in sorted(list(dq.keys())):
        QuestionsConnection.addQuestion(dq[i])

    for i in sorted(list(dhq.keys())):
        QuestionsConnection.addHistoryQuestion(dhq[i])
