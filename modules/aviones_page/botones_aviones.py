# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    # Crear botones que ocupen todo el ancho de la columna
    if st.button("✈️ Información vuelos en USA", key="vuelos_usa_btn"):
        st.session_state.subpagina = "vuelos_usa"

    if st.button("🛫 Ver aeropuertos de USA", key="aeropuertos_btn"):
        st.session_state.subpagina = "aeropuertos"

    if st.button("🏢 Ver aerolíneas de USA", key="aerolineas_btn"):
        st.session_state.subpagina = "aerolineas"

    if st.button("📊 Ver datos de vuelos USA", key="datos_btn"):
        st.session_state.subpagina = "datos"
