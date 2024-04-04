import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_csv('/data/aeropuertos_unicos.csv')

def display():
    st.title('Vuelos en USA')

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[40, -95], zoom_start=4)  # Ajusta según tus necesidades

    # Añadir marcadores para cada aeropuerto (este es solo un ejemplo, ajusta según tu DataFrame)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=725, height=500)  # Ajusta el tamaño según tus necesidades
