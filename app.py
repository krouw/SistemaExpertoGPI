from flask import Flask, abort, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

Roles = { 1: {'name': 'Presidente', 'realizacion': 4, 'reconocimiento': 4, 'responsabilidad': 4, 'progeso':4, 'desarollo':4, 'identidad':4, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':4, 'condiciones':4, 'sueldos':0, 'ascenso':4, 'analitico':4, 'armonico':2, 'competitivo':4, 'comunicador':4, 'conector':4, 'desarollador':4, 'disciplinado':4, 'empatico':4, 'emprendedor':4, 'flexible':2, 'mandatario':4, 'responsable':4, 'competencia':4},
          2: {'name': 'Vicepresidente', 'realizacion': 3, 'reconocimiento': 4, 'responsabilidad': 4, 'progeso':4, 'desarollo':4, 'identidad':4, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':4, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':4, 'armonico':2, 'competitivo':3, 'comunicador':4, 'conector':4, 'desarollador':4, 'disciplinado':4, 'empatico':4, 'emprendedor':4, 'flexible':2, 'mandatario':4, 'responsable':4, 'competencia':4},
          3: {'name': 'Asesor', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':3, 'identidad':4, 'politicas':3, 'administracion':4, 'supervision':4, 'interpersonal':4, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':3, 'comunicador':4, 'conector':4, 'desarollador':3, 'disciplinado':4, 'empatico':4, 'emprendedor':3, 'flexible':2, 'mandatario':3, 'responsable':4, 'competencia':4},
          4: {'name': 'Ingeniero de Proyectos', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':4, 'identidad':3, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':4, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':4, 'armonico':3, 'competitivo':3, 'comunicador':3, 'conector':3, 'desarollador':4, 'disciplinado':4, 'empatico':3, 'emprendedor':4, 'flexible':2, 'mandatario':4, 'responsable':4, 'competencia':4},
          5: {'name': 'Jefe Departamento', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':4, 'identidad':3, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':4, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':4, 'armonico':3, 'competitivo':3, 'comunicador':4, 'conector':4, 'desarollador':4, 'disciplinado':4, 'empatico':4, 'emprendedor':3, 'flexible':2, 'mandatario':4, 'responsable':4, 'competencia':4},
          6: {'name': 'Subjefe Departamento', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':3, 'identidad':3, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':3, 'comunicador':4, 'conector':3, 'desarollador':4, 'disciplinado':4, 'empatico':3, 'emprendedor':3, 'flexible':3, 'mandatario':3, 'responsable':4, 'competencia':4},
          7: {'name': 'Auditor', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':3, 'identidad':2, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':3, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':4, 'armonico':3, 'competitivo':2, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':4, 'empatico':3, 'emprendedor':2, 'flexible':4, 'mandatario':3, 'responsable':4, 'competencia':3},
          8: {'name': 'Contador', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':4, 'identidad':3, 'politicas':4, 'administracion':4, 'supervision':4, 'interpersonal':3, 'condiciones':4, 'sueldos':0, 'ascenso':3, 'analitico':4, 'armonico':4, 'competitivo':3, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':4, 'empatico':3, 'emprendedor':3, 'flexible':4, 'mandatario':3, 'responsable':4, 'competencia':4},
          9: {'name': 'Enfermera', 'realizacion': 2, 'reconocimiento': 2, 'responsabilidad': 4, 'progeso':2, 'desarollo':3, 'identidad':2, 'politicas':4, 'administracion':3, 'supervision':3, 'interpersonal':3, 'condiciones':2, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':2, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':4, 'empatico':3, 'emprendedor':2, 'flexible':4, 'mandatario':3, 'responsable':4, 'competencia':3},
          10: {'name': 'Medico General', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':3, 'identidad':3, 'politicas':3, 'administracion':3, 'supervision':3, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':3, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':3, 'empatico':3, 'emprendedor':3, 'flexible':3, 'mandatario':2, 'responsable':3, 'competencia':3},
          11: {'name': 'Medico Especialista', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 4, 'progeso':3, 'desarollo':3, 'identidad':3, 'politicas':3, 'administracion':3, 'supervision':3, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':3, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':3, 'empatico':3, 'emprendedor':3, 'flexible':3, 'mandatario':3, 'responsable':3, 'competencia':4},
          12: {'name': 'Coordinador Planes Salud', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 3, 'progeso':3, 'desarollo':3, 'identidad':3, 'politicas':3, 'administracion':3, 'supervision':3, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':3, 'analitico':3, 'armonico':3, 'competitivo':3, 'comunicador':3, 'conector':3, 'desarollador':3, 'disciplinado':3, 'empatico':3, 'emprendedor':3, 'flexible':3, 'mandatario':3, 'responsable':3, 'competencia':4},
          13: {'name': 'Ayudante Mantenimiento', 'realizacion': 2, 'reconocimiento': 2, 'responsabilidad': 3, 'progeso':2, 'desarollo':2, 'identidad':2, 'politicas':2, 'administracion':2, 'supervision':3, 'interpersonal':2, 'condiciones':3, 'sueldos':0, 'ascenso':2, 'analitico':3, 'armonico':3, 'competitivo':1, 'comunicador':2, 'conector':2, 'desarollador':2, 'disciplinado':2, 'empatico':2, 'emprendedor':2, 'flexible':2, 'mandatario':2, 'responsable':2, 'competencia':2},
          14: {'name': 'Auxiliar Aseo', 'realizacion': 1, 'reconocimiento': 2, 'responsabilidad': 2, 'progeso':2, 'desarollo':1, 'identidad':2, 'politicas':3, 'administracion':2, 'supervision':3, 'interpersonal':1, 'condiciones':2, 'sueldos':0, 'ascenso':1, 'analitico':1, 'armonico':1, 'competitivo':1, 'comunicador':2, 'conector':2, 'desarollador':1, 'disciplinado':3, 'empatico':1, 'emprendedor':2, 'flexible':2, 'mandatario':1, 'responsable':3, 'competencia':1},
          15: {'name': 'Despachador Farmaceutica', 'realizacion': 4, 'reconocimiento': 3, 'responsabilidad': 2, 'progeso':3, 'desarollo':3, 'identidad':3, 'politicas':3, 'administracion':2, 'supervision':4, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':1, 'analitico':3, 'armonico':2, 'competitivo':1, 'comunicador':2, 'conector':2, 'desarollador':2, 'disciplinado':3, 'empatico':2, 'emprendedor':2, 'flexible':2, 'mandatario':1, 'responsable':4, 'competencia':2},
          16: {'name': 'Secretario', 'realizacion': 3, 'reconocimiento': 3, 'responsabilidad': 2, 'progeso':2, 'desarollo':3, 'identidad':3, 'politicas':3, 'administracion':2, 'supervision':4, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':1, 'analitico':3, 'armonico':2, 'competitivo':1, 'comunicador':1, 'conector':2, 'desarollador':2, 'disciplinado':3, 'empatico':2, 'emprendedor':1, 'flexible':2, 'mandatario':1, 'responsable':4, 'competencia':2},
17: {'name': 'Guardia', 'realizacion': 2, 'reconocimiento': 3, 'responsabilidad': 3, 'progeso':2, 'desarollo':2, 'identidad':2, 'politicas':4, 'administracion':1, 'supervision':2, 'interpersonal':3, 'condiciones':3, 'sueldos':0, 'ascenso':2, 'analitico':2, 'armonico':2, 'competitivo':2, 'comunicador':1, 'conector':1, 'desarollador':1, 'disciplinado':3, 'empatico':1, 'emprendedor':1, 'flexible':1, 'mandatario':3, 'responsable':3, 'competencia':1}}


def fuzzyLogic(body):
    Hacone = []
    FactBio=[]
    FactAmb=[]
    HCN=0
    FA=0
    FB=0
    contador = 0
    Total = 0

    for i in range(1,3):
        pregunta = float(body[i])
        FactBio.append(pregunta)
        FB = FB+pregunta
        contador = contador + 1

    for i in range(3,5):
        pregunta = float(body[i])
        FactAmb.append(pregunta)
        FA = FA+pregunta
        contador = contador + 1

    for i in range(5,32):
        pregunta = float(body[i])
        Hacone.append(pregunta)
        HCN = HCN+pregunta
        contador = contador + 1

        Total=FB+FA+HCN
    print contador
    print Total

    cargouni = { 'presidente':4057099, 'vicepresidente':4057095, 'asesor financiero':4057086, 'jefe de proyecto':4027088, 'jefe de departamentos':4057086, 'subjefe de departamentos':4027085, 'auditor':4026081, 'contador':4026083, 'medico general':4026075, 'medico especialista':4026077, 'coordinador':4027076 }
    cargotec = { 'ayudante mantenimiento':3000060, 'despachador farmacia':3015659, 'secretaria':3010658, 'enfermera':3000073 }
    cargomedia = { 'aseo':43, 'guardia':52 }

    result = []

    if Total >= 4027076:
        for k,v in cargouni.iteritems():
            if Total >= v:
                result.append(k)
    elif Total >= 3000060:
        for k,v in cargotec.iteritems():
            if Total>=v:
                result.append(k)
    elif Total < 3000000:
        for k,v in cargomedia.iteritems():
            if Total>=v:
                result.append(k)
    return result

def validate(body):
    if body:
        return True
    else:
        return False

class index(Resource):
    def get(self):
        return { 'hola': 'apiSistemaDePerfiles' }

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

api.add_resource(index, '/')
api.add_resource(RestFuzzy, '/api/test')
api.add_resource(RestRole, '/api/role/<int:id_role>')

if __name__ == '__main__':
    app.run()
