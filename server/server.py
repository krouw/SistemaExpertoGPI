from flask import Flask, abort, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from motor import fuzzyLogic

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

def validate(body):
    if body:
        return True
    else:
        return False


class RestFuzzy(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        content = request.get_json(silent=True)
        if(validate(content)):
            resultado = fuzzyLogic(content)
            return { 'resultado': 'resultado' }
        else:
            return { 'error': 'Problemas con el servidor' }, 400

api.add_resource(RestFuzzy, '/api/test')

if __name__ == '__main__':
    app.run(debug=True)
