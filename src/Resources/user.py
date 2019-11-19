from security import Security
from Model.user import UserList

from flask_restful import Resource
from flask import request, render_template, jsonify, make_response, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user


class LogReg(Resource):
    def post(cls):
        return make_response(render_template('login.html')) if request.form['submit'] == 'login' \
            else make_response(render_template('signup.html')) if request.form['submit'] == 'signup' \
            else make_response(render_template('dashboard.html'))

    def get(cls):
        return "logreg"


class Login(Resource):
    def post(cls):
        username = request.form['username']
        password = request.form['password']
        user = Security.authenticate(username, password)
        if user:
            login_user(user)
            jsonUser = cls.__getUser(user)
            if user.Role == 'Stud':
                print(user.FName)
                return make_response(render_template('StudentView.html', userInfo={'user': user.FName}))
            elif user.Role == "Prof":
                return make_response(render_template('TeacherView.html', userInfo=jsonify({'user': jsonUser})))
            elif user.Role == "Admin":
                return make_response(render_template('AdminView.html', userInfo=jsonify({'user': jsonUser})))
        return make_response(render_template('login.html'))

    def get(cls):
        return make_response(render_template('login.html'))

    def __getUser(cls, user):
        return {
            'username': user.Username,
            'first_name': user.FName,
            'last_name': user.LName,
            'grade': user.Grade,
            'role': user.Role
        }


class Logout(Resource):

    @login_required
    def get(cls):
        logout_user()
        # return make_response(render_template('dashboard.html'))
        return redirect('/')

# class Register(Resource):
#     def post(self):
#         data = _user_parser.parse_args()
#         if UserModel.find_by_username(data['username']):
#             return {"message": "Username Already Exists."}, 400
#         user = UserModel(**data)
#         user.save_to_db()
#         return {"message": "User Created successfully."}, 201


# class User(Resource):
#     @classmethod
#     def get(cls, user_id):
#         user = UserModel.find_by_id(user_id)
#         if user:
#             return user.json()
#         return {'message': 'user not found'}, 404

#     @classmethod
#     def delete(cls, user_id):
#         user = UserModel.find_by_id(user_id)
#         if user:
#             user.delete_from_db()
#             return {"message": "User deleted successfully."}, 200
#         return {'message': 'user not found'}, 404


class AllUserList(Resource):
    @login_required
    def get(self):
        if current_user.Role != 'Admin':
            return {'mesasge': 'admin user only'}, 401

        return {'Users': UserList.GetAllUsers()}


class Check(Resource):
    @login_required
    def get(cls):
        return '{} {} {}'.format(current_user.Username, current_user.Grade, current_user.Role)
