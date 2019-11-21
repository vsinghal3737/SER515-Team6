import SQLAlchemyCreateDB as sql
from datetime import datetime


class Questions:
    dateFormat = '%Y-%m-%d %H:%M:%S'

    @classmethod
    def addQuestion(cls, question):
        sql.db.session.add(
            sql.Question(
                Question=question['Question'],
                Answer=question['Answer'],
                Grade=question['Grade'],
                ProfID=question['ProfID'],
                SubmittedOn=datetime.strptime(question['SubmittedOn'], cls.dateFormat)
            )
        )
        sql.db.session.commit()
        return True

    @classmethod
    def addHistoryQuestion(cls, question):
        sql.db.session.add(
            sql.HistoryQuestion(
                His_QuesID=question['His_QuesID'],
                StudID=question['StudID'],
                AttemptedAns=question['AttemptedAns'],
                Result=True if question['Result'] == 'Pass' else False,
                SubmittedOn=datetime.strptime(question['SubmittedOn'], cls.dateFormat)
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

        submitted_questions = \
            list(
                set(
                    map(
                        lambda x: x.His_QuesID,
                        sql.HistoryQuestion.query.filter_by(StudID=user.id).filter_by(Result=True).all()
                    )
                )
            )

        return {
            row.id: {
                'id': row.id,
                'question': row.Question,
                'answer': row.Answer,
                'grade': row.Grade,
                'prof_id': row.ProfID,
                'submitted_on': row.SubmittedOn
            } for row in sql.Question.query.filter_by(Grade=user.Grade).all()[::-1] if row.id not in submitted_questions
        }

    @classmethod
    def getQuestionPerGrade(cls, grade):
        return {
            row.id: {
                'id': row.id,
                'question': row.Question,
                'answer': row.Answer,
                'grade': row.Grade,
                'prof_id': row.ProfID,
                'submitted_on': row.SubmittedOn
            } for row in sql.Question.query.filter_by(Grade=grade).all()[::-1]
        }

    @classmethod
    def getHistQuestion(cls, username):

        return {
            row.id: {
                'id': row.id,
                'his_question_id': row.His_QuesID,
                'stud_id': row.StudID,
                'attempted_ans': row.AttemptedAns,
                'result': 'Pass' if row.Result is True else 'Fail',
                'submitted_on': row.SubmittedOn
            } for row in sql.HistoryQuestion.query.filter_by(
                StudID=sql.User.query.filter_by(Username=username).first().id).all()
        }


def DummyRun():
    from DummyQuestions import dummy_questions as dq, Dummy_history_questions as dhq

    for i in sorted(list(dq.keys())):
        QuestionsConnection.addQuestion(dq[i])

    for i in sorted(list(dhq.keys())):
        QuestionsConnection.addHistoryQuestion(dhq[i])
