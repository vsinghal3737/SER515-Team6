from flask import Flask, jsonify, Api
import flask_mongoalchemy
# from flask_restful import Api
# from flask_jwt import JWT
# from flask_jwt_extended import JWTManager


app = Flask(__name__)


# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
app.secret_key = 'vaibhav'  # app.secret_key = app.config['JWT_SECRET_KEY']


# app.config['MONGOALCHEMY_DATABASE_URI'] = None
# app.config['MONGOALCHEMY_TRACK_MODIFICATIONS'] = None
# app.config['PROPAGATE_EXCEPTIONS'] = None
# app.config['JWT_BLACKLIST_ENABLED'] = None
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
