# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from modules.carga_todos_df import cargar_todos_df

def load_model(path):
    model = load(path)
    return model

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')

    # Cargar modelo
    model = load_model('data/model_nuevo.joblib')

    # Cargar datos y asegurar transformación adecuada
    df = cargar_todos_df()

    # Seleccionar opciones para la predicción
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique())

    if st.button('Predecir Retraso'):
        # Preparar features para la predicción, asegúrate de que están en el formato adecuado
        features = np.array([[ciudad_origen, aeropuerto_origen, ciudad_destino, aerolinea]])
        # Si el modelo fue entrenado con datos codificados, necesitas aplicar la misma transformación aquí
        # Transformar las características aquí si es necesario antes de la predicción
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
