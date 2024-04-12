# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
from modules.carga_todos_df import cargar_todos_df
from modules.ml.carga_mod_df import unir_df_modelo

def load_model(path):
    model = load(path)
    return model

def alinear_columnas_df_todos(df_todos, df_modelo):
    columnas_modelo = df_modelo.columns.tolist()  # Asume que df_modelo ya está cargado o pasa como parámetro
    return df_todos[columnas_modelo]

def load_mappings(path):
    with open(path, 'rb') as file:
        mappings = pickle.load(file)
    return mappings

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/modelo_entrenado.joblib')
    mappings = load_mappings('data/target_encodings.pkl')
    
    df_todos = cargar_todos_df()
    df_modelo = unir_df_modelo()
    df_todos = alinear_columnas_df_todos(df_todos, df_modelo)  # Asegúrate de que df_todos y df_modelo están alineados

    # Selección de usuario usando df_todos
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df_todos['ciudad_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df_todos['ciudad_destino'].unique())
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    # Uso de df_modelo para la predicción
    # Asumiendo que tienes una forma de mapear las selecciones del usuario a sus valores codificados en df_modelo
    indices = df_todos[(df_todos['ciudad_origen'] == ciudad_origen) & (df_todos['ciudad_destino'] == ciudad_destino)].index
    features = df_modelo.loc[indices, :].iloc[0]  # Asume que obtienes la primera fila que coincide o adapta según sea necesario

    if st.button('Predecir Retraso'):
        prediction = model.predict([features.values])
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')
