# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    # Usamos st.columns para crear un diseño con espacios alrededor de los botones para centrarlos
    espacio_izq, col1, col2, col3, col4, espacio_der = st.columns([1,2,2,2,2,1])

    with col1:
        if st.button("Información vuelos en USA", key="vuelos_usa_btn"):
            st.session_state.subpagina = "vuelos_usa"

    with col2:
        if st.button("Ver aeropuertos de USA", key="aeropuertos_btn"):
            st.session_state.subpagina = "aeropuertos"

    with col3:
        if st.button("Ver aerolíneas de USA", key="aerolineas_btn"):
            st.session_state.subpagina = "aerolineas"

    with col4:
        if st.button("Ver datos de vuelos USA", key="datos_btn"):
            st.session_state.subpagina = "datos"
