from flask import Flask, jsonify, request, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
import os
import jwt
import datetime
from functools import wraps

# from user import UserDB
# from security import authenticate, identity

app = Flask(__name__, template_folder='../View', static_folder='../Controller')

app.config['SECRET_KEY'] = 'deadMenTellNoTales'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(str(os.path.abspath(os.path.dirname(__file__))) + '/DataBase.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return render_template('dashboard.html')


@app.route('/LogReg', methods=['POST', 'GET'])
def loginOption():
    return render_template('login.html') if request.form['submit'] == 'login' \
        else render_template('signup.html') if request.form['submit'] == 'signup' \
        else render_template('dashboard.html')


# @app.route("/StudentView")
# def studentView():
#     return render_template('StudentView.html')


# @app.route("/TeacherView")
# def teacherDashboard():
#     return render_template('TeacherView.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    usr = authenticate(username, password)
    if usr:
        userRole = UserDB.getRole(usr.username)
        userGrade = UserDB.getGrade(usr.username)
        if userRole == "Student":
            HistoryQuestions = UserDB.getHistoryQuestions(usr.username)
            Questions = UserDB.getQuestions(usr.username)
            return render_template('StudentView.html', grade=userGrade, HistoryQuestions=HistoryQuestions, Questions=Questions)
        elif userRole == "Teacher":
            Questions = UserDB.getQuestions(usr.username)
            return render_template("TeacherView", grade=userGrade, Questions=Questions)
        elif userRole == "Admin":
            AllUsers = UserDB.getAllUsers(usr.username)
            return render_template("AdminView", AllUsers=AllUsers)
    return render_template('dashboard.html')


@app.route("/register")
def register():
    return render_template('Register.html')


if __name__ == '__main__':
    from SQLAlchemyCreateDB import User
    app.run(port=5000, debug=True)
