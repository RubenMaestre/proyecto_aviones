# modules/botones_aviones.py
import streamlit as st

# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    # Funciones que se llamarán cuando se haga clic en las imágenes
    def on_click_vuelos_usa():
        st.session_state.subpagina = 'vuelos_usa'

    def on_click_aeropuertos():
        st.session_state.subpagina = 'aeropuertos'

    def on_click_aerolineas():
        st.session_state.subpagina = 'aerolineas'

    def on_click_datos():
        st.session_state.subpagina = 'datos'

    with col1:
        st.image("sources/aviones.jpg", width=200, on_click=on_click_vuelos_usa, caption="Ver vuelos en USA")

    with col2:
        st.image("sources/aeropuertos.jpg", width=200, on_click=on_click_aeropuertos, caption="Ver aeropuertos de USA")

    with col3:
        st.image("sources/aerolineas.jpg", width=200, on_click=on_click_aerolineas, caption="Ver aerolíneas de USA")

    with col4:
        st.image("sources/datos.jpg", width=200, on_click=on_click_datos, caption="Ver datos de vuelos USA")
