# modelos/ml/ml_1.py
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from modules.carga_todos_df import cargar_todos_df  # Importa la función para cargar todos los DataFrames

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')

    # Cargar modelo
    model = load_model('data/modelo_entrenado.pkl')

    # Cargar datos
    df = cargar_todos_df()  # Usar la función importada para cargar todos los datos

    # Interfaces de usuario para seleccionar entradas
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuertos_disponibles = df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique()
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=aeropuertos_disponibles)
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolineas_disponibles = df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique()
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=aerolineas_disponibles)

    # Botón para realizar predicción
    if st.button('Predecir Retraso'):
        features = np.array([[ciudad_origen, aeropuerto_origen, ciudad_destino, aerolinea]])
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')