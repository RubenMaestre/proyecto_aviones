import pandas as pd
import joblib
import pickle
import streamlit as st

# Cargar el modelo y el dataframe
modelo = joblib.load('data/joblib/model.joblib')
df_modelo = joblib.load('data/joblib/df_modelo.joblib')

# Cargar el diccionario de target encoding
with open('data/target_encoding.pkl', 'rb') as f:
    target_encoding = pickle.load(f)

# Importar la función para obtener rutas únicas
from modules.ml.rutas_unicas import obtener_rutas_unicas

# Definir los días de la semana como una lista global
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

def display_ml_page():
    st.subheader('Predicción de Retraso de Vuelos')

    # Obtener rutas únicas para el selector de ciudades
    rutas_unicas = obtener_rutas_unicas()
    ciudades_origen = sorted(rutas_unicas['ciudad_origen'].unique())
    ciudad_origen_seleccionada = st.selectbox('Elige la ciudad de origen:', ciudades_origen)

    # Filtrar ciudades de destino en base a la ciudad de origen seleccionada
    ciudades_destino = sorted(rutas_unicas[rutas_unicas['ciudad_origen'] == ciudad_origen_seleccionada]['ciudad_destino'].unique())
    ciudad_destino_seleccionada = st.selectbox('Elige la ciudad de destino:', ciudades_destino)

    # Seleccionar día de la semana
    dia_semana_seleccionado = st.selectbox('Selecciona el día de la semana:', dias_semana)

    # Seleccionar hora de salida programada
    hora_salida = st.slider('Selecciona la hora de salida programada:', 0, 23, 12)

    # Botón para realizar predicción
    if st.button('Predecir Retraso'):
        pred = predecir_retraso(ciudad_origen_seleccionada, ciudad_destino_seleccionada, dia_semana_seleccionado, hora_salida)
        st.write(f'Predicción de retraso: {"Sí" if pred else "No"}')

def predecir_retraso(ciudad_origen, ciudad_destino, dia_semana, hora_salida):
    # Convertir entradas usando el target encoding y la lista global de días de la semana
    inputs = {
        'ciudad_origen': target_encoding['ciudad_origen'].get(ciudad_origen, -1),
        'ciudad_destino': target_encoding['ciudad_destino'].get(ciudad_destino, -1),
        'dia_semana': dias_semana.index(dia_semana),
        'hora_salida_programada': hora_salida
    }

    # Convertir diccionario a DataFrame
    input_df = pd.DataFrame([inputs])

    # Hacer predicción
    resultado_prediccion = modelo.predict(input_df)[0]
    return resultado_prediccion