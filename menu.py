# menu.py
import streamlit as st
from paginas import inicio, eda, modelo, sobre_nosotros

def create_sidebar():
    # Aplicar estilos CSS para usar una imagen de fondo en el sidebar
    st.markdown("""
        <style>
            /* Establecer la imagen de fondo para el sidebar */
            .css-1d391kg {
                background-image: url('sources/fondo_menu.jpg');
                background-size: cover;  /* Cubrir todo el sidebar */
            }
            /* Estilos adicionales para el texto y otros elementos en el sidebar para asegurar legibilidad */
            .css-1d391kg, .css-1d391kg .st-bb, .css-1d391kg .st-cx, .css-1d391kg .st-dv, .css-1d391kg .st-ij {
                color: white;  /* Texto en blanco */
            }
            /* Ajustes para el título y botones del sidebar */
            .css-1v3fvcr, .css-1n2mvz5 {
                margin: 0 auto;
                text-align: center;
                width: 100%;  /* Ajustar el ancho de los botones y el título */
            }
            .css-1xdhyk6 {
                padding-top: 50px;  /* Añadir separación después del título del menú */
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
