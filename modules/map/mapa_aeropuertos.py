import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_globales():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Inicializar el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)

    # Iterar sobre el DataFrame y agregar un marcador para cada aeropuerto
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=row['nombre_aeropuerto'],
            icon=folium.Icon(color='red', icon='plane', prefix='fa')
        ).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=1280, height=720, key="unique_map_key")
