import numpy as np
import skfuzzy as fuzz
import time
from skfuzzy import control as ctrl
import os

# Agregar antecedente(s) que contienen el universo de variales
# y funciones de pertenencia
def fuzzyLogic(body):
    habilidad1 = ctrl.Antecedent(np.arange(0,11.0,1), 'habilidad1')
    habilidad1['armonico'] = fuzz.trapmf(habilidad1.universe, [0.0, 0.0, 2.0, 2.1])
    habilidad1['analitico'] = fuzz.trapmf(habilidad1.universe, [2.0, 2.1, 4.0, 4.1])
    habilidad1['comunicador'] = fuzz.trapmf(habilidad1.universe, [4.0, 4.1, 6.0, 6.1])
    habilidad1['competitivo'] = fuzz.trapmf(habilidad1.universe, [6.0, 6.1, 8.0, 8.1])
    habilidad1['disciplinado'] = fuzz.trapmf(habilidad1.universe, [8.0, 8.1, 10.0, 10.0])

    habilidad2 = ctrl.Antecedent(np.arange(0,11.0,1), 'habilidad2')
    habilidad2['empatico'] = fuzz.trapmf(habilidad2.universe, [0.0, 0.0, 2.0, 2.1])
    habilidad2['flexible'] = fuzz.trapmf(habilidad2.universe, [2.0, 2.1, 4.0, 4.1])
    habilidad2['responsable'] = fuzz.trapmf(habilidad2.universe, [4.0, 4.1, 6.0, 6.1])
    habilidad2['emprendedor'] = fuzz.trapmf(habilidad2.universe, [6.0, 6.1, 8.0, 8.1])
    habilidad2['mandatario'] = fuzz.trapmf(habilidad2.universe, [8.0, 8.1, 10.0, 10.0])

    competencia = ctrl.Antecedent(np.arange(0, 11.0, 1), 'competencia')
    competencia['basicas'] = fuzz.trapmf(competencia.universe, [0.0, 0.0, 2.0, 2.1])
    competencia['comportamiento'] = fuzz.trapmf(competencia.universe, [2.0, 2.1, 4.0, 4.1])
    competencia['tecnicas'] = fuzz.trapmf(competencia.universe, [4.0, 4.1, 6.0, 6.1])
    competencia['intelectuales'] = fuzz.trapmf(competencia.universe, [6.0, 6.1, 8.0, 8.1])
    competencia['orden y seguridad'] = fuzz.trapmf(competencia.universe, [8.0, 8.1, 10.0, 10.0])

    necesidad1 = ctrl.Antecedent(np.arange(0, 11.0, 1), 'necesidad1')
    necesidad1['relacionar'] = fuzz.trapmf(necesidad1.universe, [0.0, 0.0, 2.0, 2.1])
    necesidad1['influir'] = fuzz.trapmf(necesidad1.universe, [2.0, 2.1, 4.0, 4.1])
    necesidad1['destacarse'] = fuzz.trapmf(necesidad1.universe, [4.0, 4.1, 6.0, 6.1])
    necesidad1['exito'] = fuzz.trapmf(necesidad1.universe, [6.0, 6.1, 8.0, 8.1])
    necesidad1['desafios'] = fuzz.trapmf(necesidad1.universe, [8.0, 8.1, 10.0, 10.0])

    necesidad2 = ctrl.Antecedent(np.arange(0, 11.0, 1), 'necesidad2')
    necesidad2['supervision'] = fuzz.trapmf(necesidad2.universe, [0.0, 0.0, 2.0, 2.1])
    necesidad2['sueldo'] = fuzz.trapmf(necesidad2.universe, [2.0, 2.1, 4.0, 4.1])
    necesidad2['condiciones'] = fuzz.trapmf(necesidad2.universe, [4.0, 4.1, 6.0, 6.1])
    necesidad2['politicas'] = fuzz.trapmf(necesidad2.universe, [6.0, 6.1, 8.0, 8.1])
    necesidad2['administracion'] = fuzz.trapmf(necesidad2.universe, [8.0, 8.1, 10.0, 10.0])

    # # Funciones de pertenencia para la variable de salida

    salida = ctrl.Consequent(np.arange(0, 11, 1), 'salida')

    salida['cargo1'] = fuzz.trapmf(salida.universe, [0, 0, 2, 2.5])
    salida['cargo2'] = fuzz.trapmf(salida.universe, [2, 2.5, 4.0, 4.5])
    salida['cargo3'] = fuzz.trapmf(salida.universe, [4, 4.5, 6.0, 6.5])
    salida['cargo4'] = fuzz.trapmf(salida.universe, [6, 6.5, 8.0, 8.5])
    salida['cargo5'] = fuzz.trapmf(salida.universe, [8, 8.5, 10.0, 11.0])

    #
    # salida.view()
    # time.sleep(115)
    #


    ##REGLA alta probabilidad de incendio
    rule_cargo1 = ctrl.Rule((habilidad1['armonico'] | habilidad2['empatico'])
                                              | (competencia['basicas'] | necesidad1['relacionar'])
                                              | (necesidad2['supervision']), salida['cargo1'])

    ##REGLA media probabilidad de incendio
    rule_cargo2 = ctrl.Rule((habilidad1['analitico'] | habilidad2['flexible'])
                                           | (competencia['comportamiento'] | necesidad1['influir'])
                                           | (necesidad2['sueldo']), salida['cargo2'])

    ##REGLA baja probabilidad de incendio
    rule_cargo3 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo3'])

    rule_cargo4 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo4'])

    rule_cargo5 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo5'])



    calidad_ctrl = ctrl.ControlSystem([rule_cargo1, rule_cargo2, rule_cargo3, rule_cargo4, rule_cargo5])
    calidad = ctrl.ControlSystemSimulation(calidad_ctrl)


    calidad.input['habilidad1'] = float(body['habilidad1'])
    calidad.input['habilidad2'] = float(body['habilidad2'])
    calidad.input['competencia'] = float(body['competencia'])
    calidad.input['necesidad1'] = float(body['necesidad1'])
    calidad.input['necesidad2'] = float(body['necesidad2'])


    calidad.compute()

    #
    print "\nResultado"
    print calidad.output['salida']
    print "\n"

    return calidad.output['salida']
