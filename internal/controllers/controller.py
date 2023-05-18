from internal.models.fuzzyModel import diagnostico, enfermedad
import skfuzzy as fuzz


def realizar_diagnostico(datos):
     #asignar los datos a las variables de entrada
    diagnostico.input['temperatura'] = datos['temperatura']
    diagnostico.input['dolor_de_cabeza'] = datos['dolor_de_cabeza']
    diagnostico.input['tos'] = datos['tos']
    #evaluar el sistema de control
    diagnostico.compute()
    #obtener el resultado
    resultado = diagnostico.output['enfermedad']
    #imprimir el resultado  
    print(resultado)
    pert_gripa = fuzz.interp_membership(enfermedad.universe, enfermedad['gripa'].mf, resultado)
    pert_bronquitis = fuzz.interp_membership(enfermedad.universe, enfermedad['bronquitis'].mf, resultado)
    pert_neumonia = fuzz.interp_membership(enfermedad.universe, enfermedad['neumonia'].mf, resultado)
    #seleccionar la enfermedad con mayor pertenencia
    if pert_gripa >= pert_bronquitis and pert_gripa >= pert_neumonia:
        enfermedad_diagnosticada = 'Gripa'
        tratamiento = 'Descanso, hidratación y medicamentos para aliviar los síntomas'
    elif pert_bronquitis >= pert_gripa and pert_bronquitis >= pert_neumonia:
        enfermedad_diagnosticada = 'Bronquitis'
        tratamiento = 'Descanso, hidratación y medicamentos para aliviar los síntomas, puede requerir antibióticos'
    else:
        enfermedad_diagnosticada = 'Neumonía'
        tratamiento = 'Hospitalización, antibióticos y cuidados intensivos'

    return {'enfermedad_diagnosticada': enfermedad_diagnosticada, 'tratamiento': tratamiento, 'aproximacion': resultado}
