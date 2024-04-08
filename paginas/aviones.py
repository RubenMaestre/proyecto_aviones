# paginas/aviones.py
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from paginas import aviones
from paginas.vuelos import aerolineas, aeropuertos, datos
from modules.botones_aviones import crear_botones

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Vuelos en USA')

    # Inicialización de la variable de estado si aún no existe
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'

    # Llamada a crear_botones en cada página o en un sidebar común
    crear_botones()

    # Lógica para determinar qué página mostrar
    if st.session_state.pagina_actual == 'aviones':
        aviones.display()
    elif st.session_state.pagina_actual == 'aeropuertos':
        aeropuertos.display()
    elif st.session_state.pagina_actual == 'aerolineas':
        aerolineas.display()
    elif st.session_state.pagina_actual == 'datos':
        datos.display()

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)

    # Añadir marcadores para cada aeropuerto
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    # Mostrar el mapa
    st_folium(mapa, width=1280, height=720, key="unique_map_key")