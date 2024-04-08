# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    image_style = """
    <style>
        .clickable-image {
            cursor: pointer;
            transition: transform 0.2s;
        }
        .clickable-image:hover {
            transform: scale(1.1);
        }
    </style>
    """

    def markdown_image(image_path, key):
        # La función JavaScript aquí intenta establecer un valor en localStorage y recargar la página.
        # Sin embargo, esta acción puede no funcionar como se espera en el entorno de Streamlit Sharing.
        return st.markdown(f"""
        <a href='javascript:void(0);'>
            <img class='clickable-image' src='{image_path}' onclick='if(typeof(Storage) !== "undefined") {{localStorage.setItem("{key}", "true"); location.reload(); }}' width='200'/>
        </a>
        """, unsafe_allow_html=True)

    with col1:
        col1_1, col1_2, col1_3 = col1.columns([1,4,1])
        with col1_2:
            markdown_image("sources/aviones.jpg", 'btn_vuelos_usa')

    with col2:
        col2_1, col2_2, col2_3 = col2.columns([1,4,1])  # Corregido para usar col2
        with col2_2:
            markdown_image("sources/aeropuertos.jpg", 'btn_aeropuertos')  # Asegúrate de que la imagen exista

    with col3:
        col3_1, col3_2, col3_3 = col3.columns([1,4,1])  # Corregido para usar col3
        with col3_2:
            markdown_image("sources/aerolineas.jpg", 'btn_aerolineas')

    with col4:
        col4_1, col4_2, col4_3 = col4.columns([1,4,1])  # Corregido para usar col4
        with col4_2:
            markdown_image("sources/datos.jpg", 'btn_datos')

    st.markdown(image_style, unsafe_allow_html=True)