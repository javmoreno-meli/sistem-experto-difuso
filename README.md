# Sistema experto difuso para la detección de enfermedades 

**Resíratorias** 
- Gripe
- Neumonía
- Bronquitis

**Infecciosas y parasitarias**
- Dengue
- Malaria
- Parasitosis intestinal

**Digestivas**
- Gastritis
- Colitis
- Ulcera

**Mentales**
- Depresión
- Retraso mental
- Anorexia

## Descripción del proyecto

Consiste en crear un sistema experto difuso basado en conocimiento para la detección de enfermedades, el cual se basa en un conjunto de reglas que se le proporcionan al sistema para que este pueda inferir y llegar a una conclusión. Inicalmente se recibe un json con la gravedad de los sintomas presentando y en base a eso se llega a una conclusion 

## Requisitos

- [x] **Python**
- [x] **Flask**
- [x] **Skfuzzy**
- [x] **Heroku**


Ejemplo JSON de entrada

```json
{
     "temperatura": 36,
     "dolor_de_cabeza": 6,
     "tos": 6

 }
```

Ejemplo JSON de salida

```json
{
    "aproximacion": 50.0,
    "enfermedad_diagnosticada": "Bronquitis",
    "tratamiento": "Descanso, hidratación y medicamentos para aliviar los síntomas, puede requerir antibióticos"
}
```

- [x] **[HEROKU]
**Instrucciones para el despliegue de la aplicacion en Heroku**

1. Crear una cuenta en Heroku
2. Crear una nueva aplicacion
3. Seleccionar la opcion de GitHub
4. Seleccionar el repositorio que contiene el proyecto
5. Seleccionar la opcion de Deploy Branch
6. Seleccionar la opcion de View
7. Seleccionar la opcion de Open app


## instalar dependencias

```bash
pip install -r requirements.txt
```

Entorno virtual > sirve para aislar las dependencias de un proyecto y evitar conflictos con otros proyectos

se activa con el comando desde la powershell o cmd (windows) en mac o linux se usa el comando source

```bash
./entorno/Scripts/activate
```
```bash
`
```bash
python -m venv entorno
```
