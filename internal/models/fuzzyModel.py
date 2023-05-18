#importar skfuzzy (para crear el sistema difuso)

import skfuzzy as fuzz
from skfuzzy import control as ctrl # para crear las reglas
import numpy as np # para crear los rangos de las variables

#Definir las variables de entrada para el diagnositco de enfermedades

temperatura = ctrl.Antecedent(np.arange(35, 41, 1), 'temperatura') # 35, 41, 1 quiere decir que la temperatura va de 35 a 41 grados con un paso de 1 grado (con un paso de 1 grado quiere decir que se puede medir la temperatura en decimales)
dolor_de_cabeza = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_de_cabeza') # 0, 11, 1 quiere decir que el dolor de cabeza va de 0 a 11 con un paso de 1
tos = ctrl.Antecedent(np.arange(0, 11, 1), 'tos') # 0, 11, 1 quiere decir que la tos va de 0 a 11 con un paso de 1


#Definir la variable de salida para el diagnostico de enfermedades
enfermedad = ctrl.Consequent(np.arange(0, 101, 1), 'enfermedad') # 0, 101, 1 quiere decir que la enfermedad va de 0 a 101 con un paso de 1 ) 

#Definir las funciones de pertenencia para las variables de entrada y salida (membership functions)
temperatura['baja'] = fuzz.trimf(temperatura.universe, [35, 35, 37]) # trimf es una funcion triangular, el primer parametro es el universo de la variable, el segundo parametro es el rango de la funcion triangular
temperatura['media'] = fuzz.trimf(temperatura.universe, [35, 37, 39])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [37, 39, 41])

dolor_de_cabeza['leve'] = fuzz.trimf(dolor_de_cabeza.universe, [0, 0, 5])
dolor_de_cabeza['moderado'] = fuzz.trimf(dolor_de_cabeza.universe, [0, 5, 10])
dolor_de_cabeza['severo'] = fuzz.trimf(dolor_de_cabeza.universe, [5, 10, 10])

tos['leve'] = fuzz.trimf(tos.universe, [0, 0, 5])
tos['moderado'] = fuzz.trimf(tos.universe, [0, 5, 10])
tos['severo'] = fuzz.trimf(tos.universe, [5, 10, 10])

enfermedad['gripa'] = fuzz.trimf(enfermedad.universe, [0, 25, 50])
enfermedad['bronquitis'] = fuzz.trimf(enfermedad.universe, [25, 50, 75])
enfermedad['neumonia'] = fuzz.trimf(enfermedad.universe, [50, 75, 100])


#Definir las reglas
regla1 = ctrl.Rule(temperatura['baja'] & dolor_de_cabeza['leve'] & tos['leve'], enfermedad['gripa'])
regla2 = ctrl.Rule(temperatura['media'] & dolor_de_cabeza['moderado'] & tos['moderado'], enfermedad['bronquitis'])
regla3 = ctrl.Rule(temperatura['alta'] & dolor_de_cabeza['severo'] & tos['severo'], enfermedad['neumonia'])

#Definir el sistema de control
diagnostico_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])

#crearmos el controlador del sistema
diagnostico = ctrl.ControlSystemSimulation(diagnostico_ctrl)


