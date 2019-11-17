from flask import jsonify, request
from flask_login import login_required, current_user
from Model.question import Questions
from flask_restful import Resource


class QuestionsPerStud(Resource):

    @login_required
    def get(cls):
        questions = Questions.getQuestionPerStud(current_user.Username)
        return jsonify({'Questions': questions})


class QuestionsPerGrade(Resource):

    @login_required
    def get(cls):
        if not request.form or 'grade' not in request.form:
            return jsonify({'message': 'grade not found'})
        questions = Questions.getQuestionPerGrade(request.form['grade'])
        return jsonify({'Questions': questions})


class HistoryQuestions(Resource):

    @login_required
    def get(cls):
        hisQues = Questions.getHistQuestion(current_user.Username)
        return jsonify({'Questions': hisQues})


class SubmitAnswer(Resource):

    @login_required
    def post(cls):
        data = request.form
        if current_user.Role == 'Stud':
            Questions.addHistoryQuestion(
                {
                    'His_QuesID': data['His_QuesID'][1:],
                    'Result': data['Result'],
                    'SubmittedOn': data['Date'],
                    'AttemptedAns': data['Attempt'],
                    'StudID': current_user.id
                }
            )
            return jsonify({'message': 'Answer Submitted'})
        return jsonify({'message': '{} role is not valid for this Task'.format(current_user.Username)})


class SubmitQuestion(Resource):

    @login_required
    def post(cls):
        data = request.form
        if current_user.Role == 'Prof':
            Questions.addQuestion(
                {
                    'Question': data['Question'],
                    'Answer': data['Answer'],
                    'Grade': data['Grade'],
                    'ProfID': data['ProfID'],
                    'SubmittedOn': data['SubmittedOn']
                }
            )
            return jsonify({'message': 'Question Submitted'})
        return jsonify({'message': '{} role is not valid for this Task'.format(current_user.Username)})
