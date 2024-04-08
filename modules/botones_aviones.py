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

    # Asegúrate de que las URLs de las imágenes sean accesibles públicamente
    def markdown_button(button_class, key):
        # Al hacer clic en el botón, se actualizará st.session_state.subpagina
        return st.markdown(f"<button class='btn {button_class}' onclick='if(typeof(Storage) !== \"undefined\") {{localStorage.setItem(\"{key}\", \"true\"); location.reload(); }}'></button>", unsafe_allow_html=True)

    with col1:
        markdown_button("btn1", "vuelos_usa")

    with col2:
        markdown_button("btn2", "aeropuertos")

    with col3:
        markdown_button("btn3", "aerolineas")

    with col4:
        markdown_button("btn4", "datos")

    # Aplica el estilo CSS
    st.markdown(button_style, unsafe_allow_html=True)

