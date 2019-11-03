from flask import Flask, request, render_template, jsonify, make_response
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os


from Resources.home import Home
# from Resources.user import LogReg, Login, Logout, Register, User, UserList, Check
# from Resources.question import QuestionsPerStud, QuestionsPerGrade, HistoryQuestions, SubmitAnswer, SubmitQuestion

app = Flask(__name__, template_folder='View', static_folder='Controller')

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
api.add_resource(Home, '/')

# api.add_resource(Login, '/login')  # /auth endpoint
# api.add_resource(Logout, '/logout')  # /auth endpoint

# api.add_resource(LogReg, '/logreg')  # /auth endpoint

# api.add_resource(Register, '/register')
# api.add_resource(User, '/user/<int:user_id>')
# api.add_resource(UserList, '/users')
# api.add_resource(Check, '/check')

# api.add_resource(QuestionsPerStud, '/GetQuestionsPerStud')
# api.add_resource(QuestionsPerGrade, '/GetQuestionsPerGrade')
# api.add_resource(HistoryQuestions, '/GetHistoryQuestions')
# api.add_resource(SubmitAnswer, '/SubmitAnswer')
# api.add_resource(SubmitQuestion, '/SubmitQuestion')


if __name__ == '__main__':
    from security import Security
    app.run(port=5000, debug=True)
