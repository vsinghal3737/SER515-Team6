from flask import Flask, jsonify, request, render_template
# from flask_restful import Api
# from flask_jwt import JWT
# from flask_jwt_extended import JWTManager


app = Flask(__name__, template_folder='../View')
app.config['PROPAGATE_EXCEPTIONS'] = None

# USER AUTH and User Session [for next sprint]
# app.config['JWT_BLACKLIST_ENABLED'] = None
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)

# app.secret_key = KEY_STRING  # app.secret_key = app.config['JWT_SECRET_KEY']


# studentDashboard will be a placeholder for home (login/register) [for next sprint]
@app.route("/")
@app.route("/StudentView")
def home():
    return render_template('StudentView.html')


app.run(port=5000, debug=True)
