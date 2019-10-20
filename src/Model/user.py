import sqlite3
# from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('app.db')
        cursor = connection.cursor()

        query = "SELECT * FROM UserAuth WHERE username=?"
        result = cursor.execute(query, username).fetchone()

        connection.close()

        return cls(*result[:-1]) if result else None

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('app.db')
        cursor = connection.cursor()

        query = "SELECT * FROM UserAuth WHERE id=?"
        result = cursor.execute(query, (_id, ))

        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


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
