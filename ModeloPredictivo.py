import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def entrenaModelo():
    #Importacipon del dataset requerido
    insurance_dataset = pd.read_csv('G:/My Drive/Material de estudio/Magister Data Science/Taller de Aplicaciones/Trabajo/insurance.csv',encoding='utf-8',delimiter=',')
    
    # codificando columna 'sex'
    insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

    # codificando columna 'smoker' 
    insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

    # codificando columna 'region' 
    insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

    #Separando el valor de la carga con sus predictores
    X = insurance_dataset.drop(columns='charges', axis=1)
    Y = insurance_dataset['charges']

    # Cargando el modelo de Regresión Lineal
    regressor = LinearRegression()

    #Entrenando el modelo
    regressor.fit(X,Y)

    return regressor

def predecir(p_age,p_sex,p_bmi,p_children,p_smoker,p_region):

    input_data = (p_age,p_sex,p_bmi,p_children,p_smoker,p_region)

    # cambiando input_data a array numpy 
    input_data_as_numpy_array = np.asarray(input_data)

    # reformateando el array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = entrenaModelo().predict(input_data_reshaped)

    return str(prediction[0])    

#print(predecir(35,1,25.74,0,1,0))
