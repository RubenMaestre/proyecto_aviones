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
    model = load_model('data/modelo_entrenado.joblib')

    # Cargar datos y asegurar transformación adecuada
    df = cargar_todos_df()

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuertos_disponibles = df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique()
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=aeropuertos_disponibles)
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolineas_disponibles = df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique()
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=aerolineas_disponibles)

    if st.button('Predecir Retraso'):
        # Aquí necesitas asegurarte de que las entradas estén en el formato adecuado
        features = np.array([[ciudad_origen, aeropuerto_origen, ciudad_destino, aerolinea]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
