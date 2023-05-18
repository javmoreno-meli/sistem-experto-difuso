#importar flask (para hacer la API)
from flask import Flask, jsonify, request
from internal.models.fuzzyModel import realizar_diagnostico as diagnostico


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
    
    #realizar el diagnostico
    entrada = {
        'temperatura': datos['temperatura'],
        'dolor_de_cabeza': datos['dolor_de_cabeza'],
        'tos': datos['tos']
    }
    enfermedad_diagnosticada, tratamiento, resultado = diagnostico(entrada)
    return jsonify({
        'enfermedad_diagnosticada': enfermedad_diagnosticada,
        'tratamiento': tratamiento,
        'aproximacion': resultado
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)


