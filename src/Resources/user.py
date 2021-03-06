from security import Security
from Model.user import UserList, UserMode

from flask_restful import Resource
from flask import request, render_template, jsonify, make_response, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user


class LogReg(Resource):
    def post(cls):
        return redirect(url_for('login')) if request.form['submit'] == 'login' \
            else redirect(url_for('playground')) if request.form['submit'] == 'playground' \
            else make_response(render_template('dashboard.html'))
        # return make_response(render_template('login.html')) if request.form['submit'] == 'login' \
        #     # else make_response(render_template('signup.html')) if request.form['submit'] == 'signup' \
        #     else make_response(render_template('playground.html')) if request.form['submit'] == 'playground' \
        #     else make_response(render_template('dashboard.html'))

    def get(cls):
        return "logreg"

class Playground(Resource):
    def get(cls):
        return make_response(render_template('playground.html'))

class Login(Resource):
    def post(cls):
        username = request.form['username']
        password = request.form['password']
        user = Security.authenticate(username, password)
        if user:
            login_user(user)
            jsonUser = cls.__getUser(user)
            if user.Role == 'Stud':
                if jsonUser['grade'] == 1:
                    return make_response(render_template('StudentView.html', userInfo={'user': user.FName}))
                if jsonUser['grade'] == 4:
                    return make_response(render_template('StudentViewGrade4.html', userInfo={'user': user.FName}))
            elif user.Role == "Prof":
                if jsonUser['grade'] == 1:
                    return make_response(render_template('TeacherViewGrade1.html', userInfo={'user': user.FName}))
                if jsonUser['grade'] == 4:
                    return make_response(render_template('professor4.html', userInfo={'user': user.FName}))
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


class UpdateGrade(Resource):
    @login_required
    def post(cls):
        data = request.form
        if current_user.Role != 'Admin':
            return {'mesasge': 'Admin user only'}

        return jsonify({'message': 'Grade Updated'}) if UserMode.UpdateGrade(data['Username'], data['Grade']) \
            else jsonify({'message': 'Grade Not Updated for {}'.format(data['Username'])})


class DeleteUser(Resource):
    @login_required
    def post(cls):
        data = request.form
        if current_user.Role != 'Admin':
            return jsonify({'mesasge': 'Admin user only'})

        return jsonify({'message': 'User Deleted'}) if UserMode.DeleteUser(data['Username']) \
            else jsonify({'message': 'User {} not found'.format(data['Username'])})
