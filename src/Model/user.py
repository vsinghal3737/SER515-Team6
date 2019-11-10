# from flask_restful import Resource, reqparse
import SQLAlchemyCreateDB as sql


class User:
    @classmethod
    def find_by_username(cls, username):
        return sql.User.query.filter_by(Username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return sql.User.query.get(_id)

    @classmethod
    def NewPassword(cls, username, newPassword):
        sql.User.query.filter_by(Username=username).first().Password = newPassword


class UserList:
    @classmethod
    def GetAllUsers(cls):
        return [
            {
                'Username': user.Username,
                'FName': user.FName,
                'LName': user.LName,
                'Grade': user.Grade,
                'Role': user.Role,
            } for user in sql.User.query.filter_by(Username != 'Admin').all()
        ]

# In testing phase

# class UserRegister(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('username', type=str, required=True, help="This field cannot be left black!")
#     parser.add_argument('password', type=str, required=True, help="This field cannot be left black!")

#     def post(self):

#         data = UserRegister.parser.parse_args()

#         # if cursor.execute("SELECT * FROm users WHERE username=?", data['username']):
#         #     return {"message": "Username Already Exists."}, 400

#         if User.find_by_username(data['username']):
#             return {"message": "Username Already Exists."}, 400

#         connection = sqlite3.connect('app.db')
#         cursor = connection.cursor()

#         query = "INSERT INTO users Values (NULL, ?, ?)"
#         cursor.execute(query, (data['username'], data['password'], ))

#         connection.commit()
#         connection.close()

#         return {"message": "User Created successfully."}, 201
