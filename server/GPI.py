import numpy as np
import skfuzzy as fuzz
import time
from skfuzzy import control as ctrl
import os

# Agregar antecedente(s) que contienen el universo de variales
# y funciones de pertenencia

educacion = ctrl.Antecedent(np.arange(0,11.0,1), '1')
educacion['NA'] = fuzz.trapmf(habilidad1.universe, [0.0, 0.0, 2.0, 2.1])
educacion['basica'] = fuzz.trapmf(habilidad1.universe, [2.0, 2.1, 4.0, 4.1])
educacion['media'] = fuzz.trapmf(habilidad1.universe, [4.0, 4.1, 6.0, 6.1])
educacion['tecnicacurso'] = fuzz.trapmf(habilidad1.universe, [6.0, 6.1, 8.0, 8.1])
educacion['tecnicacompleta'] = fuzz.trapmf(habilidad1.universe, [8.0, 8.1, 10.0, 10.0])
educacion['universidadcurso'] = fuzz.trapmf(habilidad1.universe, [8.0, 8.1, 10.0, 10.0])
educacion['universidadcompleto'] = fuzz.trapmf(habilidad1.universe, [8.0, 8.1, 10.0, 10.0])

experiencia = ctrl.Antecedent(np.arange(0, 11.0, 1), '2')
experiencia['cero'] = fuzz.trapmf(competencia.universe, [0.0, 0.0, 2.0, 2.1])
experiencia['mas1'] = fuzz.trapmf(competencia.universe, [0.0, 0.0, 2.0, 2.1])
experiencia['mas2'] = fuzz.trapmf(competencia.universe, [2.0, 2.1, 4.0, 4.1])
experiencia['mas5'] = fuzz.trapmf(competencia.universe, [4.0, 4.1, 6.0, 6.1])

antecedentes = ctrl.Antecedent(np.arange(0, 11.0, 1), '3')
antecedentes['no'] = fuzz.trapmf(necesidad1.universe, [0.0, 0.0, 2.0, 2.1])
antecedentes['si'] = fuzz.trapmf(necesidad1.universe, [2.0, 2.1, 4.0, 4.1])

duraciontrabajo = ctrl.Antecedent(np.arange(0, 11.0, 1), '4')
duraciontrabajo['cero'] = fuzz.trapmf(competencia.universe, [0.0, 0.0, 2.0, 2.1])
duraciontrabajo['mas1'] = fuzz.trapmf(competencia.universe, [0.0, 0.0, 2.0, 2.1])
duraciontrabajo['mas2'] = fuzz.trapmf(competencia.universe, [2.0, 2.1, 4.0, 4.1])
duraciontrabajo['mas5'] = fuzz.trapmf(competencia.universe, [4.0, 4.1, 6.0, 6.1])

# # Funciones de pertenencia para la variable de salida

salida = ctrl.Consequent(np.arange(0, 11, 1), 'salida')

salida['cargo1'] = fuzz.trapmf(salida.universe, [0, 0, 2, 2.5])
salida['cargo2'] = fuzz.trapmf(salida.universe, [2, 2.5, 4.0, 4.5])
salida['cargo3'] = fuzz.trapmf(salida.universe, [4, 4.5, 6.0, 6.5])
salida['cargo4'] = fuzz.trapmf(salida.universe, [6, 6.5, 8.0, 8.5])
salida['cargo5'] = fuzz.trapmf(salida.universe, [8, 8.5, 10.0, 11.0])

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

calidad.input['habilidad1'] = 1
calidad.input['habilidad2'] = 4
calidad.input['competencia'] = 7
calidad.input['necesidad1'] = 9
calidad.input['necesidad2'] = 2


calidad.compute()

print "\nResultado"
print calidad.output['salida']
print "\n"
