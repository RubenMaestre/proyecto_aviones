import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')


def display():
    st.title('Vuelos en USA')

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)  #Punto centrado en Elche, la idea es que se vea todo el mundo desde punto vista Europa

    # Añadir marcadores para cada aeropuerto (este es solo un ejemplo, ajusta según tu DataFrame)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    st_folium(mapa, width=1280, height=720)

    # Llamar a display() para mostrar el primer mapa
    display()
