import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Extracción de datos y explicación')
    # Aquí iría el resto de tu contenido de la página de inicio


    # Mostrar el mapa base con Folium (esto siempre se muestra, independientemente de la subpágina)
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)
    st_folium(mapa, width=1280, height=720, key="unique_map_key")