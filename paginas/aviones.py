# paginas/aviones.py
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from modules.botones_aviones import crear_botones  # Importa la función
from paginas.vuelos import aerolineas, aeropuertos, datos  # Asegúrate de que estas rutas sean correctas

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Vuelos en USA')

    # Llama a la función para mostrar los botones de navegación
    crear_botones()

    # Navegación interna basada en el estado de la sesión
    if 'subpagina' in st.session_state:
        if st.session_state.subpagina == 'aeropuertos':
            aeropuertos.display()
        elif st.session_state.subpagina == 'aerolineas':
            aerolineas.display()
        elif st.session_state.subpagina == 'datos':
            datos.display()

    # Mostrar el mapa base con Folium (esto siempre se muestra, independientemente de la subpágina)
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)
    st_folium(mapa, width=1280, height=720, key="unique_map_key")
