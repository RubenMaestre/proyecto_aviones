import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from modules.data_preparation import prepare_aeropuertos_unicos
from modules.load_data import cargar_y_combinar_df


# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')


def display():
    st.title('Vuelos en USA')

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[48.8566, 2.3522], zoom_start=2)  

    # Añadir marcadores para cada aeropuerto (este es solo un ejemplo, ajusta según tu DataFrame)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    st_folium(mapa, width=1280, height=720)

    # Llamar a display() para mostrar el primer mapa
    display()
