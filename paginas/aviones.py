import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from paginas import aviones
from paginas.vuelos import aerolineas, aeropuertos, datos

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Vuelos en USA')

    # Crear columnas para los botones
    col1, col2, col3, col4 = st.columns(4)

    # Botón para volver a la página de aviones (vuelos en USA)
    with col1:
        if st.button("", image="sources/aviones.jpg"):
            aviones.display()  # Asumiendo que tienes una función display en aviones.py

    # Botón para ir a la página de aeropuertos
    with col2:
        if st.button("", image="sources/aeropuertos.jpg"):
            aeropuertos.display()  # Asumiendo que tienes una función display en aeropuertos.py dentro de paginas/vuelos/

    # Botón para ir a la página de aerolíneas
    with col3:
        if st.button("", image="sources/aerolineas.jpg"):
            aerolineas.display()  # Asumiendo que tienes una función display en aerolineas.py dentro de paginas/vuelos/

    # Botón para ir a la página de datos
    with col4:
        if st.button("", image="sources/datos.jpg"):
            datos.display()  # Asumiendo que tienes una función display en datos.py

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)  # Punto centrado en Elche, la idea es que se vea todo el mundo desde punto vista Europa

    # Añadir marcadores para cada aeropuerto
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    # Mostrar el mapa
    st_folium(mapa, width=1280, height=720, key="unique_map_key")

