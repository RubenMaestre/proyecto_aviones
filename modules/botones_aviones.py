# modules/botones_aviones.py
import streamlit as st

def crear_botones():
    col1, col2, col3, col4 = st.columns(4)

    button_style = """
    <style>
        .button {
            display: inline-block;
            padding: 0.5em 3em;
            margin: 0 0.3em 0.3em 0;
            border-radius: 0.15em;
            box-sizing: border-box;
            text-decoration: none;
            font-family: 'Roboto',sans-serif;
            font-weight: 300;
            color: #FFFFFF;
            background-color: #4eb5f1;
            text-align: center;
            transition: all 0.2s;
        }
        .button:hover {
            background-color: #4095c6;
        }
    </style>
    """

    def markdown_button(text, key):
        return st.markdown(f"<a class='button' href='javascript:void(0);' onclick='if(typeof(Storage) !== \"undefined\") {{localStorage.setItem(\"{key}\", \"true\"); location.reload(); }}'>{text}</a>", unsafe_allow_html=True)

    with col1:
        col1_1, col1_2, col1_3 = col1.columns([1,4,1])
        with col1_2:
            st.image("sources/aviones.jpg", width=200, use_column_width=True)
            markdown_button('Ver vuelos en USA', 'btn_vuelos_usa')

    with col2:
        col2_1, col2_2, col2_3 = col2.columns([1,4,1])
        with col2_2:
            st.image("sources/aeropuertos.jpg", width=200, use_column_width=True)
            markdown_button('Ver aeropuertos de USA', 'btn_aeropuertos')

    with col3:
        col3_1, col3_2, col3_3 = col3.columns([1,4,1])
        with col3_2:
            st.image("sources/aerolineas.jpg", width=200, use_column_width=True)
            markdown_button('Ver aerolíneas de USA', 'btn_aerolineas')

    with col4:
        col4_1, col4_2, col4_3 = col4.columns([1,4,1])
        with col4_2:
            st.image("sources/datos.jpg", width=200, use_column_width=True)
            markdown_button('Ver datos de vuelos USA', 'btn_datos')

    st.markdown(button_style, unsafe_allow_html=True)