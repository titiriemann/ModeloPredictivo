#API RestFul

from flask import Flask,request
from ModeloPredictivo import predecir

app = Flask(__name__) 
@app.route('/ModeloPredictivo', methods = ['GET']) 
def usandoModelo():

    p_age = int(request.args.get('Edad'))
    p_sex = int(request.args.get('Sexo'))
    p_bmi = float(request.args.get('BMI'))
    p_children = int(request.args.get('Hijos'))
    p_smoker = int(request.args.get('Fuma'))
    p_region = int(request.args.get('Region'))

    if p_age is None or p_sex is None or p_bmi is None or p_children is None or p_smoker is None or p_region is None: 
        return "Faltan Datos"

    return predecir(p_age,p_sex,p_bmi,p_children,p_smoker,p_region)

if __name__=='__main__': app.run(port=1100,debug=True)