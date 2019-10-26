from flask import Flask, jsonify, request, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import os
import jwt
import datetime
from functools import wraps

from security import authenticate, identity


app = Flask(__name__, template_folder='../View', static_folder='../Controller')

app.config['SECRET_KEY'] = 'deadMenTellNoTales'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(str(os.path.abspath(os.path.dirname(__file__))) + '/DataBase.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'dashboard'


@login_manager.user_loader
def load_user(user_id):
    return identity(int(user_id))


@app.route("/")
def home():
    return render_template('dashboard.html')


@app.route('/LogReg', methods=['POST', 'GET'])
def loginOption():
    return render_template('login.html') if request.form['submit'] == 'login' \
        else render_template('signup.html') if request.form['submit'] == 'signup' \
        else render_template('dashboard.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    # data = request.get_json()
    # username = data['username']
    # password = data['password']
    user = authenticate(username, password)
    if user:
        login_user(user)
        if user.Role == 'stud':
            return render_template('StudentView.html')
        elif user.Role == "Prof":
            return render_template("TeacherView")
        elif user.Role == "Admin":
            return render_template("AdminView")
    return render_template('dashboard.html')


@app.route("/signup", methods=['POST', 'GET'])
def register():

    return ''


if __name__ == '__main__':
    app.run(port=5000, debug=True)
