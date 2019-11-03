import SQLAlchemyCreateDB as sql
from datetime import datetime


class Questions:
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
            lambda x: x.His_QuesID,
            sql.HistoryQuestion.query.filter_by(StudID=user.id).filter_by(Result=True).all()
        )))

        questions = {
            row.id: {
                'id': row.id,
                'question': row.Question,
                'answer': row.Answer,
                'grade': row.Grade,
                'prof_id': row.ProfID,
                'submitted_on': row.SubmittedOn
            } for row in sql.Question.query.filter_by(Grade=user.Grade).all() if row.id not in submitted_questions
        }
        return questions

    @classmethod
    def getQuestionPerGrade(cls, grade):
        questions = {
            row.id: {
                'id': row.id,
                'question': row.Question,
                'answer': row.Answer,
                'grade': row.Grade,
                'prof_id': row.ProfID,
                'submitted_on': row.SubmittedOn
            } for row in sql.Question.query.filter_by(Grade=grade).all()
        }
        return questions

    @classmethod
    def getHistQuestion(cls, username):
        user_id = sql.User.query.filter_by(Username=username).first().id
        questions = {
            row.id: {
                'id': row.id,
                'his_question_id': row.His_QuesID,
                'stud_id': row.StudID,
                'attempted_ans': row.AttemptedAns,
                'result': 'Pass' if row.Result is True else 'Fail',
                'submitted_on': row.SubmittedOn
            } for row in sql.HistoryQuestion.query.filter_by(StudID=user_id).all()
        }
        return questions


def DummyRun():
    from DummyQuestions import dummy_questions as dq, Dummy_history_questions as dhq

    for i in sorted(list(dq.keys())):
        QuestionsConnection.addQuestion(dq[i])

    for i in sorted(list(dhq.keys())):
        QuestionsConnection.addHistoryQuestion(dhq[i])
