from flask import Flask, jsonify, request, render_template
# from flask_restful import Api
# from flask_jwt import JWT
# from flask_jwt_extended import JWTManager

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
        1: "5+4=_",
        2: "9-7=_",
        3: "_+_=6",
        4: "3+4=_",
        5: "_-_=2"
    }
    return jsonify(questions)


@app.route("/TeacherView")
def teacherDashboard():
    return render_template('TeacherView.html')


@app.route("/auth")
def auth():
    return render_template('LogReg.html')


app.run(port=5000, debug=True)
