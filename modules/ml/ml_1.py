# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from modules.ml.carga_previa import carga_inicial

def load_model(path):
    return load(path)

def load_mappings(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

def alinear_columnas_df_todos(df_todos, df_modelo):
    columnas_comunes = [col for col in df_modelo.columns if col in df_todos.columns and col != 'llega_tarde']
    return df_todos[columnas_comunes]

def apply_target_encoding(value, mapping, default_value=np.nan):
    return mapping.get(value, default_value)

def display_ml_page():
    df_todos, df_modelo, rutas, model, mappings = carga_inicial()  # Carga todo lo necesario
    st.title('Predicción de Retrasos de Vuelos')

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df_todos['ciudad_origen'].unique())
    ciudades_destino_validas = rutas[rutas['ciudad_origen'] == ciudad_origen]['ciudad_destino'].unique()
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=ciudades_destino_validas)
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)
    dia_semana_map = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
    if st.button('Predecir Retraso'):
        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
        ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
        dia_semana_encoded = dia_semana_map[dia_semana]
        aerolinea_encoded = np.random.choice(list(mappings['aerolinea']))
        numero_cola_encoded = np.random.choice(list(mappings['numero_cola']))
        estado_origen_encoded = np.random.choice(list(mappings['estado_origen']))
        aeropuerto_origen_encoded = np.random.choice(list(mappings['aeropuerto_origen']))
        estado_destino_encoded = np.random.choice(list(mappings['estado_destino']))
        aeropuerto_destino_encoded = np.random.choice(list(mappings['aeropuerto_destino']))
        fecha_encoded = np.random.choice(range(1, 13))  # Meses del año
        hora_salida_programada_encoded = np.random.choice(range(24))  # Hora del día
        features = [
            aerolinea_encoded, fecha_encoded, numero_cola_encoded, hora_salida_programada_encoded, ciudad_origen_encoded, estado_origen_encoded, aeropuerto_origen_encoded, dia_semana_encoded, ciudad_destino_encoded, estado_destino_encoded, aeropuerto_destino_encoded
        ]
        features_df = pd.DataFrame([features], columns=['aerolinea', 'fecha', 'numero_cola', 'hora_salida_programada', 'ciudad_origen', 'estado_origen', 'aeropuerto_origen', 'dia_semana', 'ciudad_destino', 'estado_destino', 'aeropuerto_destino'])
        prediction = model.predict(features_df)
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')

