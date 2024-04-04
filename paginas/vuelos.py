import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_csv('df/aeropuertos_unicos.csv')

def display():
    st.title('Vuelos en USA')

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[40, -95], zoom_start=4)  # Ajusta según tus necesidades

    # Añadir marcadores para cada aeropuerto (este es solo un ejemplo, ajusta según tu DataFrame)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

     # Centrar el mapa usando st.columns
    col1= st.columns([1])

    with col1:  # Usar la columna central para el mapa, haciendo que esté centrado
        st_folium(mapa, width=1280, height=720)
