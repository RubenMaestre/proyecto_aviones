# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        col1_1, col1_2, col1_3 = col1.columns([1,4,1])  # Ajusta las proporciones para centrar más
        with col1_2:  # Usa esta subcolumna para colocar tanto la imagen como el botón
            st.image("sources/aviones.jpg", width=200)
            if st.button('Ver vuelos en USA', key='btn_vuelos_usa'):
                st.session_state.subpagina = 'vuelos_usa'
  
    with col2:
        col2_1, col2_2, col2_3 = col2.columns([1,4,1])  # Mismas proporciones que col1 para consistencia
        with col2_2:
            st.image("sources/aeropuertos.jpg", width=200)
            if st.button('Ver aeropuertos de USA', key='btn_aeropuertos'):
                st.session_state.subpagina = 'aeropuertos'

    with col3:
        col3_1, col3_2, col3_3 = col3.columns([1,4,1])  # Mismas proporciones que col1 para consistencia
        with col3_2:
            st.image("sources/aerolineas.jpg", width=200)
            if st.button('Ver aerolíneas de USA', key='btn_aerolineas'):
                st.session_state.subpagina = 'aerolineas'

    with col4:
        col4_1, col4_2, col4_3 = col4.columns([1,4,1])  # Mismas proporciones que col1 para consistencia
        with col4_2:
            st.image("sources/datos.jpg", width=200)
            if st.button('Ver datos de vuelos USA', key='btn_datos'):
                st.session_state.subpagina = 'datos'
