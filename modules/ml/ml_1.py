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

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    # Repetir para otras entradas...

    if st.button('Predecir Retraso'):
        # Aplica target encoding usando los mapeos cargados
        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
        # Repetir para otras variables...

        features = np.array([[ciudad_origen_encoded]])  # Asegúrate de incluir todas las características necesarias
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')

