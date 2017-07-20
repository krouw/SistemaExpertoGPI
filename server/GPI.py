import numpy as np
import skfuzzy as fuzz
import time
from skfuzzy import control as ctrl
import os

#Agregar antecedente(s) que contienen el universo de variales y funciones de pertenencia.
#La habilidad sera representada por el rango de valores ingresado.

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

    #Funciones de pertenencia para la variable de salida.
    #La habilidad sera representada por el rango de valores ingresado.

    salida = ctrl.Consequent(np.arange(0, 37, 1), 'salida')

    salida['cargo1'] = fuzz.trapmf(salida.universe, [0, 0, 2, 2.5])
    salida['cargo2'] = fuzz.trapmf(salida.universe, [2, 2.5, 4, 4.5])
    salida['cargo3'] = fuzz.trapmf(salida.universe, [4, 4.5, 6.0, 6.5])
    salida['cargo4'] = fuzz.trapmf(salida.universe, [6, 6.5, 8.0, 8.5])
    salida['cargo5'] = fuzz.trapmf(salida.universe, [8, 8.5, 10.0, 10.5])
    salida['cargo6'] = fuzz.trapmf(salida.universe, [10.0, 10.5, 12, 12.5])
    salida['cargo7'] = fuzz.trapmf(salida.universe, [12, 12.5, 14.0, 14.5])
    salida['cargo8'] = fuzz.trapmf(salida.universe, [14, 14.5, 16.0, 16.5])
    salida['cargo9'] = fuzz.trapmf(salida.universe, [16, 16.5, 18.0, 18.5])
    salida['cargo10'] = fuzz.trapmf(salida.universe, [18, 18.5, 20.0, 20.5])
    salida['cargo11'] = fuzz.trapmf(salida.universe, [20.5, 20.0, 22.0, 22.5])
    salida['cargo12'] = fuzz.trapmf(salida.universe, [22, 22.5, 24.0, 24.5])
    salida['cargo13'] = fuzz.trapmf(salida.universe, [24, 24.5, 26.0, 26.5])
    salida['cargo14'] = fuzz.trapmf(salida.universe, [26, 26.5, 28.0, 28.5])
    salida['cargo15'] = fuzz.trapmf(salida.universe, [28, 28.5, 30.0, 30.5])
    salida['cargo16'] = fuzz.trapmf(salida.universe, [30, 30.5, 32, 32.5])
    salida['cargo17'] = fuzz.trapmf(salida.universe, [32, 32.5, 34.0, 34.5])
    salida['cargo18'] = fuzz.trapmf(salida.universe, [34, 34.5, 35.5, 36.0])

    ##REGLA cargo 1
    rule_cargo1 = ctrl.Rule((habilidad1['armonico'] | habilidad2['empatico'])
                                              | (competencia['basicas'] | necesidad1['relacionar'])
                                              | (necesidad2['supervision']), salida['cargo1'])

    ##REGLA cargo 2
    rule_cargo2 = ctrl.Rule((habilidad1['analitico'] | habilidad2['flexible'])
                                           | (competencia['comportamiento'] | necesidad1['influir'])
                                           | (necesidad2['sueldo']), salida['cargo2'])

    ##REGLA cargo 3
    rule_cargo3 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo3'])

    # REGLA cargo 4
    rule_cargo4 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo4'])

    # REGLA cargo 5
    rule_cargo5 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo5'])

    # REGLA cargo 6
    rule_cargo6 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo6'])

    # REGLA cargo 7
    rule_cargo7 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo7'])

    # REGLA cargo 8
    rule_cargo8 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo8'])

    # REGLA cargo 9
    rule_cargo9 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo9'])

    # REGLA cargo 10
    rule_cargo10 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo10'])

    # REGLA cargo 11
    rule_cargo11 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo11'])

    # REGLA cargo 12
    rule_cargo12 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo12'])

    # REGLA cargo 13
    rule_cargo13 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo13'])

    # REGLA cargo 14
    rule_cargo14 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo14'])

    # REGLA cargo 15
    rule_cargo15 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo15'])

    # REGLA cargo 16
    rule_cargo16 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo16'])

    # REGLA cargo 17
    rule_cargo17 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo17'])

    # REGLA cargo 18
    rule_cargo18 = ctrl.Rule((habilidad1['comunicador'] | habilidad2['responsable'])
                               | (competencia['tecnicas'] | necesidad1['destacarse'])
                               | (necesidad2['condiciones']), salida['cargo18'])

    calidad_ctrl = ctrl.ControlSystem([rule_cargo1, rule_cargo2, rule_cargo3, rule_cargo4, rule_cargo5, rule_cargo6, rule_cargo7, rule_cargo8, rule_cargo9, rule_cargo10, rule_cargo11, rule_cargo11, rule_cargo12, rule_cargo13, rule_cargo14, rule_cargo15, rule_cargo16, rule_cargo17, rulecargo18])
    calidad = ctrl.ControlSystemSimulation(calidad_ctrl)


    calidad.input['habilidad1'] = float(body['habilidad1'])
    calidad.input['habilidad2'] = float(body['habilidad2'])
    calidad.input['competencia'] = float(body['competencia'])
    calidad.input['necesidad1'] = float(body['necesidad1'])
    calidad.input['necesidad2'] = float(body['necesidad2'])

    calidad.compute()

    print "\nResultado"
    print calidad.output['salida']
    print "\n"

    return calidad.output['salida']
