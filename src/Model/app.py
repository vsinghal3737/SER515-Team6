from flask import Flask, jsonify, request, render_template
# from flask_restful import Api
from flask_jwt import JWT, jwt_required
from user import UserDB
# from flask_jwt_extended import JWTManager

from security import authenticate, identity

app = Flask(__name__, template_folder='../View', static_folder='../Controller')
app.config['PROPAGATE_EXCEPTIONS'] = None

# USER AUTH and User Session [for next sprint]
# app.config['JWT_BLACKLIST_ENABLED'] = None
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)

app.secret_key = 'SER515TEAM6'  # app.secret_key = app.config['JWT_SECRET_KEY']

jwt = JWT(app, authenticate, identity)  # /auth


# studentDashboard will be a placeholder for home (login/register) [for next sprint]
@app.route("/")
def home():
    return render_template('dashboard.html', retry=False)


@app.route("/StudentView")
def studentView():
    return render_template('StudentView.html')


@app.route("/TeacherView")
def teacherDashboard():
    return render_template('TeacherView.html')


# Login Api
@app.route("/login", methods=['POST'])
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
    return render_template('dashboard.html', retry=True)


@app.route("/register")
def register():
    return render_template('Register.html')


app.run(port=5000, debug=True)
