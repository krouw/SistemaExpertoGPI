from flask import Flask, abort, request
from flask_restful import Resource, Api
from GPI import fuzzyLogic

app = Flask(__name__)
api = Api(app)

class RestFuzzy(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        resultado = fuzzyLogic(request.form)
        return { 'resultado': resultado }

api.add_resource(RestFuzzy, '/')

if __name__ == '__main__':
    app.run(debug=True)
