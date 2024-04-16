# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from modules.carga_todos_df import cargar_todos_df
from modules.ml.carga_mod_df import unir_df_modelo
from modules.ml.rutas_unicas import obtener_rutas_unicas

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

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')
    model = load_model('data/model_nuevo.joblib')
    mappings = load_mappings('data/target_encodings.pkl')

    df_todos = cargar_todos_df()
    df_modelo = unir_df_modelo()
    df_todos = alinear_columnas_df_todos(df_todos, df_modelo)
    
    # Cargar rutas únicas
    rutas = obtener_rutas_unicas()

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df_todos['ciudad_origen'].unique())
    
    # Filtrar las ciudades destino basadas en la ciudad de origen seleccionada
    ciudades_destino_validas = rutas[rutas['ciudad_origen'] == ciudad_origen]['ciudad_destino'].unique()
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=ciudades_destino_validas)
    
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    hora_salida = st.slider('Hora de salida programada', 0, 23, 12)

    dia_semana_map = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}

    if st.button('Predecir Retraso'):
        # Convertir entradas de usuario en valores codificados usando los mapeos
        ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
        ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
        dia_semana_encoded = dia_semana_map[dia_semana]

        # Generar valores aleatorios para las demás columnas
        aerolinea_encoded = np.random.choice(list(mappings['aerolinea']))
        numero_cola_encoded = np.random.choice(list(mappings['numero_cola']))
        estado_origen_encoded = np.random.choice(list(mappings['estado_origen']))
        aeropuerto_origen_encoded = np.random.choice(list(mappings['aeropuerto_origen']))
        estado_destino_encoded = np.random.choice(list(mappings['estado_destino']))
        aeropuerto_destino_encoded = np.random.choice(list(mappings['aeropuerto_destino']))
        fecha_encoded = np.random.choice(range(1, 13))  # Meses del año
        hora_salida_programada_encoded = np.random.choice(range(24))  # Hora del día

        features = [
            aerolinea_encoded, fecha_encoded, numero_cola_encoded,
            hora_salida_programada_encoded, ciudad_origen_encoded,
            estado_origen_encoded, aeropuerto_origen_encoded, dia_semana_encoded,
            ciudad_destino_encoded, estado_destino_encoded, aeropuerto_destino_encoded
        ]

        # Convertir a DataFrame
        features_df = pd.DataFrame([features], columns=[
            'aerolinea', 'fecha', 'numero_cola', 'hora_salida_programada',
            'ciudad_origen', 'estado_origen', 'aeropuerto_origen', 'dia_semana',
            'ciudad_destino', 'estado_destino', 'aeropuerto_destino'
        ])

        # Usar el DataFrame para hacer la predicción
        prediction = model.predict(features_df)

        # Mostrar resultados
        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')