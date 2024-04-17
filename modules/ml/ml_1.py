# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
from modules.ml.import_df import cargar_df_modelo
from modules.ml.rutas_unicas import obtener_rutas_unicas

def load_model(path):
    return load(path)

def load_mappings(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

def apply_target_encoding(value, mapping, default_value=np.nan):
    return mapping.get(value, default_value)

def display_ml_page():
    model = load_model('data/model.joblib')  # Asumimos la ruta correcta al modelo
    mappings = load_mappings('data/target_encodings.pkl')  # Asumimos la ruta correcta a los mappings
    df_modelo = cargar_df_modelo()
    rutas = obtener_rutas_unicas()

    st.title('Predicción de Retrasos de Vuelos')

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=rutas['ciudad_origen'].unique())
    ciudades_destino_validas = rutas[rutas['ciudad_origen'] == ciudad_origen]['ciudad_destino'].unique()
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=ciudades_destino_validas)
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    if st.button('Predecir Retraso'):
        dia_semana_map = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
        dia_semana_encoded = dia_semana_map[dia_semana]
        hora_salida_programada_encoded = hora_salida
        fecha_encoded = 12  # Dado que todos los vuelos son en diciembre.

        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
        ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
        aerolinea_encoded = np.random.choice(list(mappings['aerolinea']))
        numero_cola_encoded = np.random.choice(list(mappings['numero_cola']))
        estado_origen_encoded = np.random.choice(list(mappings['estado_origen']))
        aeropuerto_origen_encoded = np.random.choice(list(mappings['aeropuerto_origen']))
        estado_destino_encoded = np.random.choice(list(mappings['estado_destino']))
        aeropuerto_destino_encoded = np.random.choice(list(mappings['aeropuerto_destino']))

        features = [
            aerolinea_encoded, fecha_encoded, numero_cola_encoded, hora_salida_programada_encoded,
            ciudad_origen_encoded, estado_origen_encoded, aeropuerto_origen_encoded,
            dia_semana_encoded, ciudad_destino_encoded, estado_destino_encoded, aeropuerto_destino_encoded
        ]
        features_df = pd.DataFrame([features], columns=df_modelo.columns.drop('llega_tarde'))  # Asumimos 'llega_tarde' como target.
        prediction = model.predict(features_df)
        
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
