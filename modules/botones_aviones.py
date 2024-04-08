# modules/botones_aviones.py
from paginas import aviones
from paginas.vuelos import aeropuertos, aerolineas, datos

import streamlit as st

def crear_botones(aviones, aeropuertos, aerolineas, datos):
    boton_html_template = """
    <style>
    .boton {{
        margin: 10px;
        width: 240px;
        height: 50px;
        background-color: #FFFFFF;
        color: #000000;
        border: 3px solid #ADD8E6;
        border-radius: 5px;
        cursor: pointer;
        outline: none;
    }}
    .boton:hover {{
        border-color: #0000FF;
    }}
    </style>
    <center><button class="boton" title="{}" onclick="handleClick('{}')">{}</button></center>
    <script>
    function handleClick(key) {{
        window.parent.postMessage({{func: 'keyPress', key: key}}, '*');
    }}
    </script>
    """

    # Crear columnas para los botones
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("sources/aviones.jpg", width=250)
        st.markdown(boton_html_template.format("Haz clic para ver Vuelos en USA", "aviones", "Vuelos en USA"), unsafe_allow_html=True)

    with col2:
        st.image("sources/aeropuertos.jpg", width=250)
        st.markdown(boton_html_template.format("Haz clic para ver Aeropuertos", "aeropuertos", "Aeropuertos"), unsafe_allow_html=True)

    with col3:
        st.image("sources/aerolineas.jpg", width=250)
        st.markdown(boton_html_template.format("Haz clic para ver Aerolíneas", "aerolineas", "Aerolíneas"), unsafe_allow_html=True)

    with col4:
        st.image("sources/datos.jpg", width=250)
        st.markdown(boton_html_template.format("Haz clic para ver Datos", "datos", "Datos"), unsafe_allow_html=True)