# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
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
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique())

    if st.button('Predecir Retraso'):
        # Aplicar target encoding a todas las entradas necesarias
        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
        aeropuerto_origen_encoded = apply_target_encoding(aeropuerto_origen, mappings['aeropuerto_origen'])
        ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
        aerolinea_encoded = apply_target_encoding(aerolinea, mappings['aerolinea'])

        # Preparar features para la predicción
        features = np.array([[ciudad_origen_encoded, aeropuerto_origen_encoded, ciudad_destino_encoded, aerolinea_encoded]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
