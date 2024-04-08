# paginas/aviones.py
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from modules.botones_aviones import crear_botones  # Importa la función
from paginas.vuelos import vuelos_usa, aerolineas, aeropuertos, datos  # Asegúrate de que estas rutas sean correctas

def display():
    st.title('Vuelos en USA')

    # Llama a la función para mostrar los botones de navegación
    crear_botones()

    # Texto centrado después de los botones
    st.markdown("<h3 style='text-align: center;'>Pulse una opción para saber más</h3>", unsafe_allow_html=True)


    # Navegación interna basada en el estado de la sesión
    if 'subpagina' in st.session_state:
        if st.session_state.subpagina == 'vuelos_usa':
            vuelos_usa.display()
        elif st.session_state.subpagina == 'aeropuertos':
            aeropuertos.display()
        elif st.session_state.subpagina == 'aerolineas':
            aerolineas.display()
        elif st.session_state.subpagina == 'datos':
            datos.display()


