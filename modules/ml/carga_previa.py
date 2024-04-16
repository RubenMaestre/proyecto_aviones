import pandas as pd
import streamlit as st
import pickle
from joblib import load
import requests
from io import BytesIO
from modules.carga_todos_df import cargar_todos_df
from modules.ml.import_df import cargar_df_modelo
from modules.ml.rutas_unicas import obtener_rutas_unicas

def carga_inicial():
    if 'df_todos' not in st.session_state:
        st.session_state.df_todos = cargar_todos_df()

    if 'df_modelo' not in st.session_state:
        st.session_state.df_modelo = cargar_df_modelo()

    if 'rutas' not in st.session_state:
        st.session_state.rutas = obtener_rutas_unicas()

    if 'model' not in st.session_state:
        # Descargar el modelo de la URL
        response = requests.get('https://www.rubenmaestre.com/modelos/model.joblib')
        # Asegurarte de que la solicitud fue exitosa
        response.raise_for_status()
        # Cargar el modelo desde los datos descargados
        st.session_state.model = load(BytesIO(response.content))

    if 'mappings' not in st.session_state:
        with open('data/target_encodings.pkl', 'rb') as file:
            st.session_state.mappings = pickle.load(file)

    return st.session_state.df_todos, st.session_state.df_modelo, st.session_state.rutas, st.session_state.model, st.session_state.mappings

