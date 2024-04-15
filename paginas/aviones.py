# paginas/aviones.py
import streamlit as st
from modules.aviones_page.botones_aviones import crear_botones
from paginas.vuelos import vuelos_usa, aerolineas, aeropuertos, datos

def display():
    st.markdown("<h2 style='text-align: center;'>Información sobre los vuelos en USA</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Dividir la interfaz en dos columnas: una para la navegación y otra para el contenido
    col_navegacion, col_contenido = st.columns([1, 7])

    with col_navegacion:
        st.markdown("<h4 style='text-align: center;'>Pulse una opción para saber más</h4>", unsafe_allow_html=True)

        # Llama a la función para mostrar los botones de navegación
        crear_botones()

    with col_contenido:
        # Muestra el contenido de la subpágina seleccionada
        if 'subpagina' in st.session_state:
            if st.session_state.subpagina == 'vuelos_usa':
                vuelos_usa.display()
            elif st.session_state.subpagina == 'aeropuertos':
                aeropuertos.display()
            elif st.session_state.subpagina == 'aerolineas':
                aerolineas.display()
            elif st.session_state.subpagina == 'datos':
                datos.display()

display()
