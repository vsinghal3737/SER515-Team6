from flask import Flask, jsonify, request, render_template
# from flask_restful import Api
from flask_jwt import JWT, jwt_required
from user import User
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
    return render_template('dashboard.html')


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
    if User.find_by_username(username):
        return render_template('StudentView.html')
    return render_template('dashboard.html')


@app.route("/register")
def register():
    return render_template('Register.html')


app.run(port=5000, debug=True)
