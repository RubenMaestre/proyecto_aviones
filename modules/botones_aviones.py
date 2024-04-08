# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("sources/aviones.jpg", width=250)
        if st.button('Ver Aviones', key='btn_aviones'):
            st.session_state.subpagina = 'aviones'

    with col2:
        st.image("sources/aeropuertos.jpg", width=250)
        if st.button('Ver Aeropuertos', key='btn_aeropuertos'):
            st.session_state.subpagina = 'aeropuertos'

    with col3:
        st.image("sources/aerolineas.jpg", width=250)
        if st.button('Ver Aerolíneas', key='btn_aerolineas'):
            st.session_state.subpagina = 'aerolineas'

    with col4:
        st.image("sources/datos.jpg", width=250)
        if st.button('Ver Datos', key='btn_datos'):
            st.session_state.subpagina = 'datos'
