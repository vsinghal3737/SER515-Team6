from flask import Flask, jsonify, request, render_template
# from flask_restful import Api
# from flask_jwt import JWT
# from flask_jwt_extended import JWTManager
import Question
import sqlite3

app = Flask(__name__, template_folder='../View', static_folder='../Controller')
app.config['PROPAGATE_EXCEPTIONS'] = None

# USER AUTH and User Session [for next sprint]
# app.config['JWT_BLACKLIST_ENABLED'] = None
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)

# app.secret_key = KEY_STRING  # app.secret_key = app.config['JWT_SECRET_KEY']


# studentDashboard will be a placeholder for home (login/register) [for next sprint]
@app.route("/")
@app.route("/StudentView")
def home():
    return render_template('StudentView.html')

# API to return list of questions. Currently static, should fetch data from DB


@app.route("/GetQuestions", methods=['GET'])
def getQuestions():
    questions = {
    'Q1': {
        'Question': '5+4=_',
        'QuestionID': 'Q1',
        'Answer': '9',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:33:48'
    },
    'Q2': {
        'Question': '9-7=_',
        'QuestionID': 'Q2',
        'Answer': '2',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:34:48'
    },
    'Q3': {
        'Question': '_+_=6',
        'QuestionID': 'Q3',
        'Answer': 'na',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:35:48'
    },
    'Q4': {
        'Question': '3+4=_',
        'QuestionID': 'Q4',
        'Answer': '7',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:36:48'
    },
    'Q5': {
        'Question': '_-_=2',
        'QuestionID': 'Q5',
        'Answer': 'na',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:37:48'
    }
}
    return jsonify(questions)


@app.route("/SubmitAnswer", methods=['POST'])
def submitQuestion(data):
    question = jsonify(request.args.get())


@app.route("/TeacherView")
def teacherDashboard():
    return render_template('TeacherView.html')


@app.route("/auth")
def auth():
    return render_template('LogReg.html')


app.run(port=5000, debug=True)
