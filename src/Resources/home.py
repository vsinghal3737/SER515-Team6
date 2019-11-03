from flask_restful import Resource
from flask import render_template, make_response


class Home(Resource):
    # @api.representation('text/html')
    def get(self):
        return make_response(render_template('dashboard.html'), 200)
