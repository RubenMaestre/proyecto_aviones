# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        col1_1, col1_2, col1_3 = col1.columns([1,2,1])  # Ajusta las proporciones según sea necesario
        st.image("sources/aviones.jpg", width=200)
        with col1_2:
            if st.button('Ver vuelos en USA', key='btn_vuelos_usa'):
                st.session_state.subpagina = 'vuelos_usa'

    with col2:
        st.image("sources/aeropuertos.jpg", width=200)
        col2_1, col2_2, col2_3 = col2.columns([1,2,1])  # Ajusta las proporciones según sea necesario
        with col2_2:
            if st.button('Ver aeropuertos de USA', key='btn_aeropuertos'):
                st.session_state.subpagina = 'aeropuertos'

    with col3:
        st.image("sources/aerolineas.jpg", width=200)
        col3_1, col3_2, col3_3 = col3.columns([1,2,1])  # Ajusta las proporciones según sea necesario
        with col3_2:
            if st.button('Ver aerolíneas de USA', key='btn_aerolineas'):
                st.session_state.subpagina = 'aerolineas'

    with col4:
        st.image("sources/datos.jpg", width=200)
        col4_1, col4_2, col4_3 = col4.columns([1,2,1])  # Ajusta las proporciones según sea necesario
        with col4_2:
            if st.button('Ver datos de vuelos USA', key='btn_datos'):
                st.session_state.subpagina = 'datos'
