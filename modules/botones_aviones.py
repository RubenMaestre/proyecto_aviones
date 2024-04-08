# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    # Función para generar el markdown de una imagen clicable
    def markdown_image(image_path, key, caption=""):
        # Usamos 'key' en el href para identificar qué enlace fue clickeado
        # El manejo real se hará en la app principal usando 'st.session_state'.
        return st.markdown(f"<a href='?{key}=True' style='display: inline-block; text-align: center;'><img src='{image_path}' class='img-fluid' width='200'><p>{caption}</p></a>", unsafe_allow_html=True)

    with col1:
        markdown_image("sources/aviones.jpg", 'vuelos_usa', "Ver vuelos en USA")

    with col2:
        markdown_image("sources/aeropuertos.jpg", 'aeropuertos', "Ver aeropuertos de USA")

    with col3:
        markdown_image("sources/aerolineas.jpg", 'aerolineas', "Ver aerolíneas de USA")

    with col4:
        markdown_image("sources/datos.jpg", 'datos', "Ver datos de vuelos USA")
