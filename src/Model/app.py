from flask import Flask, jsonify, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import os
import jwt
import datetime
from functools import wraps

import Question

# from user import UserDB
# from security import authenticate, identity

app = Flask(__name__, template_folder='../View', static_folder='../Controller')

app.config['SECRET_KEY'] = 'deadMenTellNoTales'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(str(os.path.abspath(os.path.dirname(__file__))) + '/new.db')

db = SQLAlchemy(app)


@app.route("/")
@app.route("/StudentView")
def home():
    return render_template('StudentView.html')


# API to return list of questions. Currently static, should fetch data from DB
@app.route("/GetQuestions", methods=['POST'])
def getQuestions():

    if not request.json or 'grade' not in request.json:
        return jsonify({'message': 'grade not found'})
    Questions = Question.getQuestions(request.json['grade'])

    return jsonify({'Questions': Question})

    # jsonify(request.args.get())


@app.route("/SubmitAnswer", methods=['POST'])
def submitAnswer(data):
    question = jsonify(request.args.get())


@app.route("/GetHistoryQuestions", methods=['POST'])
def getHistoryQuestions():
    if not request.json:
        return jsonify({'message': 'request not found'})
    elif 'PublicID' not in request.json:
        return jsonify({'message': 'id not found'})

    hisQues = Question.getHistQuestions(request.json['PublicID'])

    return jsonify({'Questions': hisQues})


@app.route("/TeacherView")
def teacherDashboard():
    return render_template('TeacherView.html')


@app.route("/auth")
def auth():
    return render_template('LogReg.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
