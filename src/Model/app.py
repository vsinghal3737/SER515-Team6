from flask import Flask, jsonify, request, render_template
import flask_mongoalchemy
# from flask_restful import Api
# from flask_jwt import JWT
# from flask_jwt_extended import JWTManager


app = Flask(__name__)


# app.config['MONGOALCHEMY_DATABASE_URI'] = None
# app.config['MONGOALCHEMY_TRACK_MODIFICATIONS'] = None
# app.config['PROPAGATE_EXCEPTIONS'] = None
# app.config['JWT_BLACKLIST_ENABLED'] = None
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
# app.secret_key = KEY_STRING  # app.secret_key = app.config['JWT_SECRET_KEY']

userIDs = \
    [
        {
            "username": "FirstUser",
            "password": "password"
        }
    ]


@app.route("/")  # Home
def home():
    return render_template('html')


@app.route('/loginReg')
def auth():
    # return render_template('html')
    return jsonify({'user': userIDs})


# To create table
# @app.before_first_request
# def create_table():
#     db.create_all()


app.run(port=5000, debug=True)
