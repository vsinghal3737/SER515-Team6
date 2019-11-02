from flask import Flask
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from model.Question import QuestionsConnection

class QuestionsPerStud(Resource):
	@login_required
	def get(self):
    	questions = QuestionsConnection.getQuestionPerStud(current_user.Username)
    	return jsonify({'Questions': questions})

class QuestionsPerGrade(Resource):
	@login_required
	def get(self):
	    if not request.form or 'grade' not in request.form:
	        return jsonify({'message': 'grade not found'})
	    questions = QuestionsConnection.getQuestionPerGrade(request.form['grade'])
	    return jsonify({'Questions': questions})


class HistoryQuestions(Resource):
	@login_required
	def get(self):
    	hisQues = QuestionsConnection.getHistQuestion(current_user.Username)
    	return jsonify({'Questions': hisQues})

class SubmitAnswer(Resource):
	@login_required
	def post(self):
	    data = request.form
	    if current_user.Role == 'Stud':
	        QuestionsConnection.addHistoryQuestion(
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
	def post(self):
		pass

	