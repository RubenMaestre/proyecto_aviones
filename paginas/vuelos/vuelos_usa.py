import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

from modules.map.mapa_aeropuertos import mostrar_mapa_aeropuertos_globales
from modules.map.estados_usa import mostrar_mapa_aeropuertos_usa
from modules.map.selector_estado import mostrar_mapa_aeropuertos_por_estado


# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Datos de vuelos sobre Estados Unidos')
    # Aquí iría el resto de tu contenido de la página de inicio
    
    st.markdown("""
            ### Mapa donde graficamos todos los Aeropuertos de Estados Unidos""")
    
    mostrar_mapa_aeropuertos_globales()

    st.markdown("---")

    st.markdown("""
            ### Mapa de estados de los Estados Unidos""")

    mostrar_mapa_aeropuertos_usa()

    st.markdown("---")

    st.markdown("""
                ### Selecciona un estado para ver los aeropuertos que contiene""")

    mostrar_mapa_aeropuertos_por_estado()

    st.markdown("---")

