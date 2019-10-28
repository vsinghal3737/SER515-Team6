from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os


app = Flask(__name__, template_folder='../View', static_folder='../Controller')

app.config['SECRET_KEY'] = 'deadMenTellNoTales'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(str(os.path.abspath(os.path.dirname(__file__))) + '/DataBase.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'


@login_manager.user_loader
def load_user(user_id):
    return Security.identity(int(user_id))


@app.route("/")
def home():
    return render_template('dashboard.html')


@app.route('/LogReg', methods=['POST', 'GET'])
def loginOption():
    return render_template('login.html') if request.form['submit'] == 'login' \
        else render_template('signup.html') if request.form['submit'] == 'signup' \
        else render_template('dashboard.html')


@app.route("/Login")
@app.route("/login")
def Login():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = Security.authenticate(username, password)
    if user:
        login_user(user)
        jsonUser = {
            'username': user.Username,
            'first_name': user.FName,
            'last_name': user.LName,
            'grade': user.Grade,
            'role': user.Role
        }
        if user.Role == 'Stud':
            return render_template('StudentView.html', userInfo=jsonify({'user': jsonUser}))
        elif user.Role == "Prof":
            return render_template('TeacherView.html', userInfo=jsonify({'user': jsonUser}))
        elif user.Role == "Admin":
            return render_template('AdminView.html', userInfo=jsonify({'user': jsonUser}))
    return render_template('dashboard.html')


@app.route("/signup", methods=['POST', 'GET'])
def register():
    return ''


@app.route('/check')
@login_required
def check():
    return '{} {} {}'.format(current_user.Username, current_user.Grade, current_user.Role)


@app.route("/logout")
@app.route("/Logout")
@login_required
def logout():
    logout_user()
    return render_template('dashboard.html')


if __name__ == '__main__':
    from security import Security
    app.run(port=5000, debug=True)
