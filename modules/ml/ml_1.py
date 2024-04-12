# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
import random
from modules.carga_todos_df import cargar_todos_df

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
    df = cargar_todos_df()

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    # Variables aleatorias o predeterminadas
    aerolinea = random.choice(df['aerolinea'].unique())
    aeropuerto_origen = random.choice(df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique())
    aeropuerto_destino = random.choice(df[df['ciudad_destino'] == ciudad_destino]['aeropuerto_destino'].unique())
    
    # Aplicar target encoding
    features_encoded = [
        apply_target_encoding(ciudad_origen, mappings['ciudad_origen']),
        apply_target_encoding(aeropuerto_origen, mappings['aeropuerto_origen']),
        apply_target_encoding(ciudad_destino, mappings['ciudad_destino']),
        apply_target_encoding(aerolinea, mappings['aerolinea']),
        dia_semana,  # Asumiendo que día de semana ya es numérico o ha sido codificado adecuadamente
        hora_salida  # Asumiendo que es una entrada numérica directa
    ]
    
    if st.button('Predecir Retraso'):
        # Preparar features para la predicción
        features = np.array([features_encoded])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')


