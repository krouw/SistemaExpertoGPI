from flask import Flask, abort, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from motor import fuzzyLogic
from roles import Roles

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

def validate(body):
    if body:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')

class RestRole(Resource):
    def get(seft, id_role):
        return { 'role': id_role, 'data': Roles[id_role], 'keys': Roles[id_role].keys() }

class RestFuzzy(Resource):
    def post(self):
        content = request.get_json(silent=True)
        if(validate(content)):
            resultado = fuzzyLogic(content)
            print resultado
            return { 'resultado': resultado }
        else:
            return { 'error': 'Problemas con el servidor' }, 400

api.add_resource(RestFuzzy, '/api/test')
api.add_resource(RestRole, '/api/role/<int:id_role>')

if __name__ == '__main__':
    app.run()
