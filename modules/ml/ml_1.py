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
    # Retorna el valor codificado, o NaN si no existe en el mapeo
    return mapping.get(value, np.nan)

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/modelo_entrenado.joblib')
    mappings = load_mappings('data/target_encodings.pkl')

    # Cargar datos y asegurar transformación adecuada
    df = cargar_todos_df()

    # Seleccionar opciones para la predicción
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique())

    if st.button('Predecir Retraso'):
        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])

        # Preparar features para la predicción, asegúrate de que están en el formato adecuado
        features = np.array([[ciudad_origen_encoded]])  # Asegúrate de incluir todas las características necesarias
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
