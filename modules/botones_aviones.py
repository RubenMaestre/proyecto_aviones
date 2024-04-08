# modules/botones_aviones.py
import streamlit as st

def crear_botones(navegar_a):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.image("sources/aviones.jpg", width=250, on_click=lambda: navegar_a('aviones')):
            pass

    with col2:
        if st.image("sources/aeropuertos.jpg", width=250, on_click=lambda: navegar_a('aeropuertos')):
            pass

    with col3:
        if st.image("sources/aerolineas.jpg", width=250, on_click=lambda: navegar_a('aerolineas')):
            pass

    with col4:
        if st.image("sources/datos.jpg", width=250, on_click=lambda: navegar_a('datos')):
            pass
