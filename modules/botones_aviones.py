# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    # Define el enlace de cada imagen. En este caso, estamos simulando una acción de "navegación"
    # al establecer una clave en st.session_state. La clave debería manejarse en tu app principal.
    def markdown_image(image_path, key, caption=""):
        return st.markdown(f"<div style='text-align: center;'><a href='javascript:void(0);' onclick='localStorage.setItem(\"{key}\", \"true\");'><img src='{image_path}' class='img-fluid' width='200'><p>{caption}</p></a></div>", unsafe_allow_html=True)

    with col1:
        markdown_image("sources/aviones.jpg", 'vuelos_usa', "Ver vuelos en USA")

    with col2:
        markdown_image("sources/aeropuertos.jpg", 'aeropuertos', "Ver aeropuertos de USA")

    with col3:
        markdown_image("sources/aerolineas.jpg", 'aerolineas', "Ver aerolíneas de USA")

    with col4:
        markdown_image("sources/datos.jpg", 'datos', "Ver datos de vuelos USA")

