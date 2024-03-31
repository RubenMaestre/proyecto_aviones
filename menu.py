# menu.py
import streamlit as st
from paginas import inicio, eda, modelo, sobre_nosotros

def create_sidebar():
    #logo_path = 'sources/logo.png'

    with open('styles/custom_styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("""
        <style>
            .titulo {
                font-weight: bold;
                color: black;
                font-size: 18px;
                padding-top: 20px;
                padding-down: 100px;
                text-align: center;
            }
                .imagen-logo {
                display: block;
                margin-left: 100px;
                margin-right: 100px;
                width: 30%;
            }
        </style>
        """, unsafe_allow_html=True)

    # st.sidebar.image(logo_path, width=150)  # Ajusta el ancho si es necesario
    # Usamos un div con la clase 'titulo' para aplicar los estilos al título
    st.sidebar.markdown('<div class="titulo">José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez</div>', unsafe_allow_html=True)

    menu_items = {
        "🏠 Inicio": inicio.display,
        "📊 EDA": eda.display,
        "👥 Modelo machine learning": modelo.display,
        "🏟 Sobre nosotros": sobre_nosotros.display,
    }

    st.sidebar.title("Menú")

    if 'active_page' not in st.session_state:
        # Esto establecerá la página de inicio como predeterminada
        st.session_state['active_page'] = "🏠 Inicio"

    for title, page_func in menu_items.items():
        if st.sidebar.button(title):
            st.session_state['active_page'] = title

    # Llama a la función de la página actual
    menu_items[st.session_state['active_page']]()