from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os


from Resources.home import *
from Resources.user import *
from Resources.question import *


app = Flask(__name__, template_folder='../View', static_folder='../Controller')

app.config['SECRET_KEY'] = 'deadMenTellNoTales'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(str(os.path.abspath(os.path.dirname(__file__))) + '/DataBase.db')

api = Api(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Security.identity(int(user_id))


# Resources
api.add_resource(Home, '/')  # /auth endpoint

api.add_resource(Login, '/login')  # /auth endpoint
api.add_resource(Logout, '/logout')  # /auth endpoint

api.add_resource(LogReg, '/logout')  # /auth endpoint

# api.add_resource(Register, '/register')
# api.add_resource(User, '/user/<int:user_id>')
# api.add_resource(UserList, '/users')

api.add_resource(QuestionsPerStud, '/GetQuestionsPerStud')
api.add_resource(QuestionsPerGrade, '/GetQuestionsPerGrade')
api.add_resource(HistoryQuestions, '/GetHistoryQuestions')
api.add_resource(SubmitAnswer, '/SubmitAnswer')
api.add_resource(SubmitQuestion, '/SubmitQuestion')

if __name__ == '__main__':
    from security import Security
    from Question import QuestionsConnection
    app.run(port=5000)
