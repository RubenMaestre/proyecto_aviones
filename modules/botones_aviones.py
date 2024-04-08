# modules/botones_aviones.py

import streamlit as st

def crear_botones():
    # Crear columnas para los botones
    col1, col2, col3, col4 = st.columns(4)

    # Botón para "Vuelos en USA"
    with col1:
        st.image("sources/aviones.jpg", width=250, caption="Vuelos en USA")
        if st.button("Ver", key="btn_aviones"):
            # La acción deseada cuando se hace clic en el botón
            pass

    # Botón para "Aeropuertos"
    with col2:
        st.image("sources/aeropuertos.jpg", width=250, caption="Aeropuertos")
        if st.button("Ver", key="btn_aeropuertos"):
            # La acción deseada cuando se hace clic en el botón
            pass

    # Botón para "Aerolíneas"
    with col3:
        st.image("sources/aerolineas.jpg", width=250, caption="Aerolíneas")
        if st.button("Ver", key="btn_aerolineas"):
            # La acción deseada cuando se hace clic en el botón
            pass

    # Botón para "Datos"
    with col4:
        st.image("sources/datos.jpg", width=250, caption="Datos")
        if st.button("Ver", key="btn_datos"):
            # La acción deseada cuando se hace clic en el botón
            pass
