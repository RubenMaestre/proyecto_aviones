# modules/botones_aviones.py
from paginas import aviones
from paginas.vuelos import aeropuertos, aerolineas, datos

import streamlit as st

def crear_botones():
    # Definición de las acciones al hacer clic en cada imagen
    def navegar_a_aviones():
        st.session_state.pagina_actual = 'aviones'
    
    def navegar_a_aeropuertos():
        st.session_state.pagina_actual = 'aeropuertos'
    
    def navegar_a_aerolineas():
        st.session_state.pagina_actual = 'aerolineas'
    
    def navegar_a_datos():
        st.session_state.pagina_actual = 'datos'
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("sources/aviones.jpg", width=250, on_click=navegar_a_aviones)

    with col2:
        st.image("sources/aeropuertos.jpg", width=250, on_click=navegar_a_aeropuertos)

    with col3:
        st.image("sources/aerolineas.jpg", width=250, on_click=navegar_a_aerolineas)

    with col4:
        st.image("sources/datos.jpg", width=250, on_click=navegar_a_datos)
