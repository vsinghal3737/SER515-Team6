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


@app.route("/GetQuestions", methods=['POST'])
def getQuestions():
    questions = {
    'Q1': {
        'Question': '5+4=_',
        'QuestionID': 'Q1',
        'Answer': '',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': ''
    },
    'Q2': {
        'Question': '9-7=_',
        'QuestionID': 'Q2',
        'Answer': '',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': ''
    },
    'Q3': {
        'Question': '_+_=6',
        'QuestionID': 'Q3',
        'Answer': '',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': ''
    },
    'Q4': {
        'Question': '3+4=_',
        'QuestionID': 'Q4',
        'Answer': '',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': ''
    },
    'Q5': {
        'Question': '_-_=2',
        'QuestionID': 'Q5',
        'Answer': '',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': ''
    }
    }
    return jsonify(questions)


@app.route("/SubmitAnswer", methods=['POST'])
def submitAnswer(data):
    question = jsonify(request.args.get())

@app.route("/GetHistoryQuestions" methods=['POST'])
def getHistoryQuestions():
    historyQuestions = {
    'HQ1': {
        'HisID': 'HQ1',
        'StudentID': 'S1',
        'QuestionID': 'Q4',
        'AttemptedAns': '9-7=2',
        'Result': 'Pass',
        'Date': '2019-10-24 17:55:21'
    },
    'HQ1': {
        'HisID': 'HQ1',
        'StudentID': 'S1',
        'QuestionID': 'Q4',
        'AttemptedAns': '9-7=3',
        'Result': 'Pass',
        'Date': '2019-10-24 17:55:21'
    },
    'HQ1': {
        'HisID': 'HQ1',
        'StudentID': 'S1',
        'QuestionID': 'Q4',
        'AttemptedAns': '9-7=2',
        'Result': 'Pass',
        'Date': '2019-10-24 17:55:21'
    },
    'HQ1': {
        'HisID': 'HQ1',
        'StudentID': 'S1',
        'QuestionID': 'Q4',
        'AttemptedAns': '9-7=2',
        'Result': 'Pass',
        'Date': '2019-10-24 17:55:21'
    }
    }

@app.route("/TeacherView")
def teacherDashboard():
    return render_template('TeacherView.html')


@app.route("/auth")
def auth():
    return render_template('LogReg.html')


app.run(port=5000, debug=True)
