# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    def on_click(key):
        st.session_state['navegar_a'] = key

    with col1:
        if st.image("sources/aviones.jpg", width=200, caption="Ver vuelos en USA", on_click=lambda: on_click('vuelos_usa')):
            pass

    with col2:
        if st.image("sources/aeropuertos.jpg", width=200, caption="Ver aeropuertos de USA", on_click=lambda: on_click('aeropuertos')):
            pass

    with col3:
        if st.image("sources/aerolineas.jpg", width=200, caption="Ver aerolíneas de USA", on_click=lambda: on_click('aerolineas')):
            pass

    with col4:
        if st.image("sources/datos.jpg", width=200, caption="Ver datos de vuelos USA", on_click=lambda: on_click('datos')):
            pass

