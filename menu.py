# menu.py
import streamlit as st
from paginas import inicio, eda, modelo, sobre_nosotros

def create_sidebar():
    # Aplicar estilos CSS directamente
    st.markdown("""
        <style>
            /* Estilo del título en el sidebar */
            .titulo {
                font-weight: bold;
                color: white; /* Texto en blanco */
                font-size: 18px;
                padding-top: 20px;
                text-align: center;
            }
            /* Estilo de la barra del sidebar */
            .css-18e3th9 {
                background-color: black; /* Fondo negro */
                color: white; /* Texto en blanco */
            }
            /* Centrar el título del menú y añadir separación */
            .css-1xdhyk6 {
                text-align: center;
                padding-top: 50px;
            }
            /* Estilo de los botones del menú */
            .css-1v3fvcr {
                display: block;
                margin: 0 auto;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

    # Nombre del equipo en la parte superior del sidebar
    st.sidebar.markdown('<div class="titulo">José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez</div>', unsafe_allow_html=True)

    # Configuración de los elementos del menú
    menu_items = {
        "🏠 Inicio": inicio.display,
        "📊 EDA": eda.display,
        "👥 Modelo machine learning": modelo.display,
        "🏟 Sobre nosotros": sobre_nosotros.display,
    }

    # Título del menú
    st.sidebar.title("Menú")

    # Determinar la página activa
    if 'active_page' not in st.session_state:
        st.session_state['active_page'] = "🏠 Inicio"

    # Crear botones del menú
    for title, page_func in menu_items.items():
        if st.sidebar.button(title):
            st.session_state['active_page'] = title

    # Llama a la función de la página actual
    menu_items[st.session_state['active_page']]()
