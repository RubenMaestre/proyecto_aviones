import streamlit as st
from modules.map.aerolineas_unicos import mostrar_aerolineas_unicos
from modules.map.aerolineas_medias import aerolineas_medias

def display():
    st.title('Aerolineas')
    # Aquí iría el resto de tu contenido de la página de inicio

    aerolineas_medias
    
    st.markdown("---")

    mostrar_aerolineas_unicos()