# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
from modules.ml.carga_mod_df import unir_df_modelo

def load_model(path):
    model = load(path)
    return model

def load_mappings(path):
    with open(path, 'rb') as file:
        mappings = pickle.load(file)
    return mappings

def apply_target_encoding(value, mapping):
    return mapping.get(value, np.nan)  # Retorna NaN si el valor no está en el mapeo

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/modelo_entrenado.joblib')
    mappings = load_mappings('data/target_encodings.pkl')

    df = unir_df_modelo()

    # Recolección de características
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique())
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)  # Ejemplo de slider para hora de salida

    # Aplicar target encoding
    ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
    aeropuerto_origen_encoded = apply_target_encoding(aeropuerto_origen, mappings['aeropuerto_origen'])
    ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
    aerolinea_encoded = apply_target_encoding(aerolinea, mappings['aerolinea'])
    estado_origen_encoded = apply_target_encoding(df['estado_origen'].iloc[0], mappings['estado_origen'])  # Ejemplo de cómo manejarlo si no es interactivo
    estado_destino_encoded = apply_target_encoding(df['estado_destino'].iloc[0], mappings['estado_destino'])
    dia_semana_encoded = apply_target_encoding(df['dia_semana'].iloc[0], mappings['dia_semana'])  

    # Preparar features para la predicción
    features = np.array([[
        ciudad_origen,
        aeropuerto_origen,
        ciudad_destino,
        aerolinea,
        dia_semana,  # Asumiendo que día de semana ya es numérico o ha sido codificado adecuadamente
        hora_salida  # Asumiendo que es una entrada numérica directa
    ]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success('El vuelo probablemente llegará con retraso.')
    else:
        st.success('El vuelo probablemente llegará a tiempo.')
