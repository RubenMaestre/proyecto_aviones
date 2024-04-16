import pandas as pd
import streamlit as st
import pickle
from joblib import load
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
        st.session_state.model = load('data/joblib/model.joblib')

    if 'mappings' not in st.session_state:
        with open('data/target_encodings.pkl', 'rb') as file:
            st.session_state.mappings = pickle.load(file)

    return st.session_state.df_todos, st.session_state.df_modelo, st.session_state.rutas, st.session_state.model, st.session_state.mappings
