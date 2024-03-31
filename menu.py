"""# menu.py
import streamlit as st
from paginas import inicio, eda, modelo, sobre_nosotros
from streamlit_option_menu import option_menu

def create_sidebar():
    # Estilos CSS para aplicar imagen de fondo y estilos de texto al sidebar
    st.markdown("""
        <style>
            /* Aplicar la imagen de fondo a todos los elementos dentro del sidebar */
            [data-testid="stSidebar"] .css-1e5imcs {
                background-image: url('sources/fondo_menu.jpg');
                background-size: cover;
            }
            /* Ajustar el color de texto de todos los elementos dentro del sidebar */
            [data-testid="stSidebar"] .css-1e5imcs, 
            [data-testid="stSidebar"] .css-1e5imcs button,
            [data-testid="stSidebar"] .css-1e5imcs .st-bq,
            [data-testid="stSidebar"] .css-1e5imcs .st-cx {
                color: white;
            }
            /* Estilos específicos para el título y botones del sidebar */
            .sidebar .block-container {
                text-align: center;
            }
            .sidebar .block-container button {
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
            .sidebar .block-container h1 {
                padding-top: 50px;
                padding-bottom: 20px;
            }
        </style>
        """, unsafe_allow_html=True)

    # Título del equipo en el sidebar
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
"""