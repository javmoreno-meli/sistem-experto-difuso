#importar flask (para hacer la API)
from flask import Flask, jsonify, request
from internal.controllers.controller import realizar_diagnostico as diagnostico


#Definir la API
app = Flask(__name__)

#Definir la ruta de la API
@app.route('/diagnostico', methods=['POST'])
def realizar_diagnostico():
    #obtener los datos del request
    datos = request.get_json()
    #imprimir los datos
    print(datos)
    #que no se haga nada si no hay datos
    if not datos:
        return jsonify({'mensaje': 'No hay datos'})
    #si falta algun dato, que no se haga nada
    if not ('temperatura' in datos and 'dolor_de_cabeza' in datos and 'tos' in datos):
        return jsonify({'mensaje': 'Faltan datos'})
    
    #si algun dato no es un numero, que no se haga nada
    if not (isinstance(datos['temperatura'], (int, float)) and isinstance(datos['dolor_de_cabeza'], (int, float)) and isinstance(datos['tos'], (int, float))):
        return jsonify({'mensaje': 'Los datos deben ser números'})
    #si algun dato no esta en el rango, que no se haga nada
    if not (datos['temperatura'] >= 35 and datos['temperatura'] <= 42 and datos['dolor_de_cabeza'] >= 0 and datos['dolor_de_cabeza'] <= 10 and datos['tos'] >= 0 and datos['tos'] <= 10):
        return jsonify({'mensaje': 'Los datos deben estar en el rango, temperatura: [35, 42], dolor_de_cabeza: [1, 10], tos: [1, 10]'})
    #Si los datos son iguales o menores a 0, que no se haga nada
    if not (datos['temperatura'] > 0 and datos['dolor_de_cabeza'] > 0 and datos['tos'] > 0):
        return jsonify({'mensaje': 'Los datos deben ser mayores a 0'})




    #realizar el diagnostico
    resultado = diagnostico(datos)
    #imprimir el resultado
    print(resultado)
    #regresar el resultado al cliente
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, port=9001)


