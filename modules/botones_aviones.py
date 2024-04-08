# modules/botones_aviones.py
from paginas import aviones
from paginas.vuelos import aeropuertos, aerolineas, datos

import streamlit as st

def crear_botones(aviones, aeropuertos, aerolineas, datos):
    st.title('Vuelos en USA')

    # Crear columnas para los botones
    col1, col2, col3, col4 = st.columns(4)

    # Mostrar imagen y botón personalizado para volver a la página de aviones (vuelos en USA)
    with col1:
        st.image("sources/aviones.jpg", width=250)
        if st.button("Vuelos en USA", key="btn_aviones", help="Haz clic para ver Vuelos en USA"):
            aviones.display()

    # Mostrar imagen y botón personalizado para ir a la página de aeropuertos
    with col2:
        st.image("sources/aeropuertos.jpg", width=250)
        if st.button("Aeropuertos", key="btn_aeropuertos", help="Haz clic para ver Aeropuertos"):
            aeropuertos.display()

    # Mostrar imagen y botón personalizado para ir a la página de aerolíneas
    with col3:
        st.image("sources/aerolineas.jpg", width=250)
        if st.button("Aerolíneas", key="btn_aerolineas", help="Haz clic para ver Aerolíneas"):
            aerolineas.display()

    # Mostrar imagen y botón personalizado para ir a la página de datos
    with col4:
        st.image("sources/datos.jpg", width=250)
        if st.button("Datos", key="btn_datos", help="Haz clic para ver Datos"):
            datos.display()
