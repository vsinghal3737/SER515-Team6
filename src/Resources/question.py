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
        questions = Questions.getQuestionPerGrade(current_user.Grade)
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
                    'Answer': '',
                    'Grade': current_user.Grade,
                    'ProfID': current_user.id,
                    'SubmittedOn': data['Date']
                }
            )
            return jsonify({'message': 'Question Submitted'})
        return jsonify({'message': '{} role is not valid for this Task'.format(current_user.Username)})


class DeleteHistoryQuestions(Resource):
    @login_required
    def post(cls):
        data = request.form
        if current_user.Role != 'Admin':
            return jsonify({'mesasge': 'Admin user only'}), 401

        if Questions.deleteHistoryQuestionPerStud(Questions.allALlQuestionsPerStud(data['username'])):
           return jsonify({'message': 'Dleted HistoryQuestions for {}'.format(data['Username'])}), 200

        return jsonify({'message': 'No History Questions for {}'.format(data['Username'])}), 204          
