from flask_restful import Resource
from flask import render_template


class Home(Resource):
    def get(self):
        return render_template('dashboard.html')
