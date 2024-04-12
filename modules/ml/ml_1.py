# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
import random
from modules.carga_todos_df import cargar_todos_df
from modules.ml.carga_mod_df import unir_df_modelo

def load_model(path):
    model = load(path)
    return model

def alinear_columnas_df_todos(df_todos, df_modelo):
    # Obtener las columnas que están en ambos DataFrames, excluyendo la columna 'llega_tarde'
    columnas_comunes = [col for col in df_modelo.columns if col in df_todos.columns and col != 'llega_tarde']
    return df_todos[columnas_comunes]

def apply_target_encoding(value, mapping, default_value=np.nan):
    """
    Aplica el mapeo de codificación a un valor dado.
    
    Args:
    - value: El valor a codificar.
    - mapping: Un diccionario que contiene el mapeo de codificación.
    - default_value: El valor a retornar si `value` no está en `mapping`.
    
    Returns:
    - El valor codificado si `value` está en `mapping`, de lo contrario `default_value`.
    """
    return mapping.get(value, default_value)

def load_mappings(path):
    with open(path, 'rb') as file:
        mappings = pickle.load(file)
    return mappings

def generate_random_feature_value(column_name, df_modelo, mappings):
    """Genera un valor aleatorio para una columna, utilizando mapeos si están disponibles."""
    if column_name in mappings:
        # Si hay un mapeo, utiliza los valores del mapeo
        return np.random.choice(list(mappings[column_name]))
    else:
        # Si no hay mapeo, utiliza valores del DataFrame directamente
        column_data = df_modelo[column_name].dropna()
        if column_data.dtype == 'object':
            return np.random.choice(column_data.unique())
        else:
            return np.random.choice(column_data)

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/modelo_entrenado.joblib')
    mappings = load_mappings('data/target_encodings.pkl')

    df_todos = cargar_todos_df()
    df_modelo = unir_df_modelo()
    df_todos = alinear_columnas_df_todos(df_todos, df_modelo)  # Asegúrate de que df_todos y df_modelo están alineados

    # Permitir al usuario seleccionar usando nombres legibles
    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df_todos['ciudad_origen'].unique())
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df_todos['ciudad_destino'].unique())
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    dia_semana_map = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
    dia_semana_encoded = dia_semana_map[dia_semana]

    if st.button('Predecir Retraso'):
    # Convertir entradas de usuario en valores codificados usando los mapeos
    ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
    ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
    dia_semana_encoded = dia_semana_map[dia_semana]

    # Generar características aleatorias para las demás necesarias
    features = []
    for col in df_modelo.columns:
        if col == 'ciudad_origen':
            features.append(ciudad_origen_encoded)
        elif col == 'ciudad_destino':
            features.append(ciudad_destino_encoded)
        elif col == 'dia_semana':
            features.append(dia_semana_encoded)
        elif col == 'hora_salida_programada':
            features.append(hora_salida)  # Asumiendo que 'hora_salida_programada' es la 'hora_salida'
        else:
            # Para todas las demás características, genera un valor aleatorio
            features.append(generate_random_feature_value(col, df_modelo, mappings))

    # Realizar predicción
    prediction = model.predict([features])
    if prediction[0] == 1:
        st.success('El vuelo probablemente llegará con retraso.')
    else:
        st.success('El vuelo probablemente llegará a tiempo.')
