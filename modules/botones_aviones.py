# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    # CSS para usar imágenes como fondo de botones
    button_style = """
    <style>
        .btn {
            border: none;
            color: transparent;
            background-color: transparent;
            padding: 0px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 200px;
            height: 200px;
        }
        .btn1 {background-image: url('sources/aviones.jpg'); background-size: cover;}
        .btn2 {background-image: url('sources/aeropuertos.jpg'); background-size: cover;}
        .btn3 {background-image: url('sources/aerolineas.jpg'); background-size: cover;}
        .btn4 {background-image: url('sources/datos.jpg'); background-size: cover;}
    </style>
    """

    # Aplica el estilo CSS
    st.markdown(button_style, unsafe_allow_html=True)

    # Botones de Streamlit para gestionar interacciones
    with col1:
        if st.button("", key="vuelos_usa_btn", **{"class": "btn btn1"}):
            st.session_state.subpagina = "vuelos_usa"

    with col2:
        if st.button("", key="aeropuertos_btn", **{"class": "btn btn2"}):
            st.session_state.subpagina = "aeropuertos"

    with col3:
        if st.button("", key="aerolineas_btn", **{"class": "btn btn3"}):
            st.session_state.subpagina = "aerolineas"

    with col4:
        if st.button("", key="datos_btn", **{"class": "btn btn4"}):
            st.session_state.subpagina = "datos"
