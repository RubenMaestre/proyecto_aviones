import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import pickle
from datetime import time
from modules.ml.import_df import cargar_df_modelo
from modules.ml.rutas_unicas import obtener_rutas_unicas
from modules.ml.dic_estados import estados_en_espanol

def load_model(path):
    return load(path)

def load_mappings(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

def apply_target_encoding(value, mapping, default_value=np.nan):
    return mapping.get(value, default_value)

def display_ml_page():
    model = load_model('data/model.joblib')  
    mappings = load_mappings('data/target_encodings.pkl') 
    df_modelo = cargar_df_modelo()
    rutas = obtener_rutas_unicas()
    estados_dict = estados_en_espanol()

        # Agrega CSS para centrar el título
    st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold !important;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    # Usa el estilo para centrar el título
    st.markdown('<p class="big-font">✈️ JetSet Predictor (JSP): Tu pasaporte a la puntualidad ✈️</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns([5, 2, 5])  # Divide la interfaz en tres columnas

    with col1:
        st.write("Primero selecciona desde la ciudad donde vas a volar")  # Espacio en blanco para ajustar el diseño
        # Seleccionar estado de origen
        opciones_estado_origen = sorted(rutas['estado_origen'].map(estados_dict).unique())  # Mapea los estados a español
        estado_origen = st.selectbox('Selecciona el estado de origen:', options=opciones_estado_origen)
        opciones_ciudad_origen = sorted(rutas[rutas['estado_origen'].map(estados_dict) == estado_origen]['ciudad_origen'].unique())
        ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=opciones_ciudad_origen)

    with col2:
        st.image("sources/volando_voy.png")  # Mostrar imagen en la columna central

    with col3:
        st.write("Ahora selecciona a la ciudad a la que quieres llegar")  # Espacio en blanco para ajustar el diseño
        # Seleccionar destino basado en la ciudad de origen
        opciones_estado_destino = sorted(rutas[rutas['ciudad_origen'] == ciudad_origen]['estado_destino'].map(estados_dict).unique())  # Mapea los estados a español
        estado_destino = st.selectbox('Selecciona el estado destino:', options=opciones_estado_destino)
        ciudades_destino_validas = sorted(rutas[(rutas['estado_destino'].map(estados_dict) == estado_destino) & (rutas['ciudad_origen'] == ciudad_origen)]['ciudad_destino'].unique())
        ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=ciudades_destino_validas)

    st.markdown("---")

    st.write("Elige que día quieres volar...")
    dia_semana = st.selectbox('Selecciona el día de la semana:', options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
        
    col4, col5 = st.columns(2)
    with col4:
        st.write("Y ahora, ¿A qué hora sale tu vuelo...")
        hora = st.slider('Hora de salida programada (hora):', 0, 23, 12)
    with col5:
        st.write("... o a qué hora pretendes salir? 😎")
        minuto = st.slider('Minuto de salida programada (minutos):', 0, 59, 30)
    
    colizq, colcenter, colder = st.columns([1, 2, 1])
    with colcenter:
        if st.button('¿Quieres saber si tu vuelo llegará puntual? Ha llegado el momento de saberlo, pulsa aquí...'):
            dia_semana_map = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
            dia_semana_encoded = dia_semana_map[dia_semana]
            # Convertir hora y minutos a minutos desde medianoche
            hora_salida_programada_encoded = hora * 60 + minuto
            fecha_encoded = 12

            ciudad_origen_encoded = apply_target_encoding(ciudad_origen, mappings['ciudad_origen'])
            ciudad_destino_encoded = apply_target_encoding(ciudad_destino, mappings['ciudad_destino'])
            aerolinea_encoded = np.random.choice(list(mappings['aerolinea']))
            numero_cola_encoded = np.random.choice(list(mappings['numero_cola']))
            estado_origen_encoded = apply_target_encoding(estado_origen, mappings['estado_origen'])
            aeropuerto_origen_encoded = np.random.choice(list(mappings['aeropuerto_origen']))
            estado_destino_encoded = apply_target_encoding(estado_destino, mappings['estado_destino'])
            aeropuerto_destino_encoded = np.random.choice(list(mappings['aeropuerto_destino']))

            features = [
                aerolinea_encoded, fecha_encoded, numero_cola_encoded, hora_salida_programada_encoded,
                ciudad_origen_encoded, estado_origen_encoded, aeropuerto_origen_encoded,
                dia_semana_encoded, ciudad_destino_encoded, estado_destino_encoded, aeropuerto_destino_encoded
            ]
            features_df = pd.DataFrame([features], columns=df_modelo.columns.drop('llega_tarde'))  # Asumimos 'llega_tarde' como target.
            prediction = model.predict(features_df)
            
            if prediction[0] == 1:
                st.error('🚩 Ups, parece que tu vuelo podría sufrir un retraso. 😢 De todas formas, a ver, somos un poco tikismikis y queremos informarte que consideramos en nuestro modelo de predicción como retraso la llegada posterior a 15 minutos de la hora programada a priori... 😬 igual tampoco es para dramatizar 🙈.')  # Uso de st.error para retrasos
            else:
                st.success('✈️ ¡El vuelo probablemente llegará a tiempo! ¿No te hemos dicho ya que nuestro modelo era increíble? 🎉 🍾 Siiiiiiiiiiiiiiiiiuuuuuuuuuuuuuuuuuuuuuuuu!!!! 😎')  # Uso de st.success para llegadas a tiempo
                st.balloons() 
