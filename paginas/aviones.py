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

    # Mostrar imagen y botón para volver a la página de aviones (vuelos en USA)
    with col1:
        st.image("sources/aviones.jpg", width=250)
        if st.button("Vuelos en USA", key="btn_aviones"):
            aviones.display()  # Asumiendo que tienes una función display en aviones.py

    # Mostrar imagen y botón para ir a la página de aeropuertos
    with col2:
        st.image("sources/aeropuertos.jpg", width=250)
        if st.button("Aeropuertos", key="btn_aeropuertos"):
            aeropuertos.display()  # Asumiendo que tienes una función display en aeropuertos.py

    # Mostrar imagen y botón para ir a la página de aerolíneas
    with col3:
        st.image("sources/aerolineas.jpg", width=250)
        if st.button("Aerolíneas", key="btn_aerolineas"):
            aerolineas.display()  # Asumiendo que tienes una función display en aerolineas.py

    # Mostrar imagen y botón para ir a la página de datos
    with col4:
        st.image("sources/datos.jpg", width=250)
        if st.button("Datos", key="btn_datos"):
            datos.display()  # Asumiendo que tienes una función display en datos.py

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)

    # Añadir marcadores para cada aeropuerto
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    # Mostrar el mapa
    st_folium(mapa, width=1280, height=720, key="unique_map_key")