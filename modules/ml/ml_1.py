# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
import random
from modules.carga_todos_df import cargar_todos_df
from modules.ml.carga_mod_df import unir_df_modelo

def load_model(path):
    model = load(path)
    return model

def alinear_columnas_df_todos(df_todos, df_modelo):
    # Obtener las columnas que están en ambos DataFrames, excluyendo la columna 'llega_tarde'
    columnas_comunes = [col for col in df_modelo.columns if col in df_todos.columns and col != 'llega_tarde']
    return df_todos[columnas_comunes]


def load_mappings(path):
    with open(path, 'rb') as file:
        mappings = pickle.load(file)
    return mappings

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/modelo_entrenado.joblib')
    mappings = load_mappings('data/target_encodings.pkl')

    df_todos = cargar_todos_df()
    df_modelo = unir_df_modelo()
    df_todos = alinear_columnas_df_todos(df_todos, df_modelo)  # Asegúrate de que df_todos y df_modelo están alineados

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df_todos['ciudad_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df_todos['ciudad_destino'].unique())
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    if st.button('Predecir Retraso'):
        # Asignar aleatoriamente el resto de las características que no selecciona el usuario
        aerolinea = random.choice(df_modelo['aerolinea'].unique())
        fecha = random.choice(df_modelo['fecha'].unique())  # Suponiendo que 'fecha' puede ser seleccionada aleatoriamente
        numero_cola = random.choice(df_modelo['numero_cola'].unique())
        estado_origen = random.choice(df_modelo['estado_origen'].unique())
        aeropuerto_origen = random.choice(df_modelo['aeropuerto_origen'].unique())
        estado_destino = random.choice(df_modelo['estado_destino'].unique())
        aeropuerto_destino = random.choice(df_modelo['aeropuerto_destino'].unique())

        # Uso de df_modelo para la predicción
        features = np.array([
            aerolinea, fecha, numero_cola, hora_salida,
            ciudad_origen, estado_origen, aeropuerto_origen, dia_semana,
            ciudad_destino, estado_destino, aeropuerto_destino
        ])

        prediction = model.predict([features])
        
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
