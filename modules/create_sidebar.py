# modules/create_sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu
from paginas import inicio, eda, modelo, sobre_nosotros

def create_sidebar():
    # Crear el menú de opciones en el sidebar con option_menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Inicio", "EDA", "Modelo machine learning", "Sobre nosotros"],
            icons=["house", "bar-chart-line", "cpu", "people"],
            menu_icon="cast", default_index=0, orientation="vertical")

    # Llama a la función de la página correspondiente en función de la selección
    if selected == "Inicio":
        inicio.display()
    elif selected == "EDA":
        eda.display()
    elif selected == "Modelo machine learning":
        modelo.display()
    elif selected == "Sobre nosotros":
        sobre_nosotros.display()

# No olvides llamar a la función create_sidebar en tu app
create_sidebar()
