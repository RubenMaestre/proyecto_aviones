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

    # Botón de imagen para volver a la página de aviones (vuelos en USA)
    with col1:
        if st.image("sources/aviones.jpg", width=250, on_click=aviones.display):
            pass  # La función aviones.display se llama cuando se hace clic en la imagen

    # Botón de imagen para ir a la página de aeropuertos
    with col2:
        if st.image("sources/aeropuertos.jpg", width=250, on_click=aeropuertos.display):
            pass  # La función aeropuertos.display se llama cuando se hace clic en la imagen

    # Botón de imagen para ir a la página de aerolíneas
    with col3:
        if st.image("sources/aerolineas.jpg", width=250, on_click=aerolineas.display):
            pass  # La función aerolineas.display se llama cuando se hace clic en la imagen

    # Botón de imagen para ir a la página de datos
    with col4:
        if st.image("sources/datos.jpg", width=250, on_click=datos.display):
            pass  # La función datos.display se llama cuando se hace clic en la imagen

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)

    # Añadir marcadores para cada aeropuerto
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    # Mostrar el mapa
    st_folium(mapa, width=1280, height=720, key="unique_map_key")