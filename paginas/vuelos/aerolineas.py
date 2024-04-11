import streamlit as st
from modules.map.aerolineas_unicos import mostrar_aerolineas_unicos

def display():
    st.title('Aerolineas')
    # Aquí iría el resto de tu contenido de la página de inicio

    mostrar_aerolineas_unicos()