import streamlit as st
from modules.map.aeropuertos_unicos import mostrar_aeropuertos_unicos


def display():
    st.title('Aeropuertos')
    # Aquí iría el resto de tu contenido de la página de inicio

    mostrar_aeropuertos_unicos()