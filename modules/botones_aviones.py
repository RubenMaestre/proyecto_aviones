# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    # CSS para usar imágenes como fondo de botones
    button_style = """
    <style>
        .btn {
            border: none;
            color: white;
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

     # Botones invisibles de Streamlit para gestionar interacciones
    with col1:
        button_style("btn1", "vuelos_usa")
        if st.button("", key="vuelos_usa_btn", help="Haz clic en la imagen para ver vuelos en USA", **{"style": "visibility: hidden;"}):
            st.session_state.subpagina = "vuelos_usa"

    with col2:
        button_style("btn2", "aeropuertos")
        if st.button("", key="aeropuertos_btn", help="Haz clic en la imagen para ver aeropuertos", **{"style": "visibility: hidden;"}):
            st.session_state.subpagina = "aeropuertos"

    with col3:
        button_style("btn3", "aerolineas")
        if st.button("", key="aerolineas_btn", help="Haz clic en la imagen para ver aerolíneas", **{"style": "visibility: hidden;"}):
            st.session_state.subpagina = "aerolineas"

    with col4:
        button_style("btn4", "datos")
        if st.button("", key="datos_btn", help="Haz clic en la imagen para ver datos", **{"style": "visibility: hidden;"}):
            st.session_state.subpagina = "datos"

    # Aplica el estilo CSS
    st.markdown(button_style, unsafe_allow_html=True)
