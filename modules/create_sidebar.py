# modules/create_sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu
from paginas import inicio, eda, modelo, sobre_nosotros

def create_sidebar():
    # Aplicar estilos CSS personalizados para el sidebar
    st.markdown("""
        <style>
            /* Estilos para el fondo y el texto del sidebar */
            .css-1lcbmhc {
                background-color: black;
                color: white;
            }
            /* Añadir estilos adicionales aquí si es necesario */
        </style>
        """, unsafe_allow_html=True)

    # Añadir texto personalizado en el sidebar con markdown y HTML
    st.sidebar.markdown(
        f'<div style="text-align: center; color: white; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez'
        f'</div>',
        unsafe_allow_html=True
    )

    # Crear el menú de opciones en el sidebar con option_menu
    with st.sidebar:
        selected = option_menu("Menú del proyecto", ["Inicio", "EDA", "Modelo machine learning", "Sobre nosotros"],
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

