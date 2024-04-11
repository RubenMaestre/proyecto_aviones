import folium
from folium import plugins
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_usa():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Inicializar el mapa centrado en los Estados Unidos
    mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=5)

    # Cargar el GeoJSON de los estados de EE.UU.
    geojson_usa = 'modules/map/us-states.json'

    # Función para agregar aeropuertos a un estado específico
    def add_airports_to_state(map_obj, state_code):
        # Filtrar aeropuertos por estado
        state_airports = df_aeropuertos_unicos[df_aeropuertos_unicos['estado'] == state_code]
        for index, row in state_airports.iterrows():
            folium.Marker(
                [row['latitude'], row['longitude']],
                popup=f"{row['nombre_aeropuerto']} ({row['codigo_aeropuerto']})",
                icon=folium.Icon(color='blue', icon='plane', prefix='fa')
            ).add_to(map_obj)

    # Función para manejar el clic en un estado
    def on_click(feature):
        # Extraer el código del estado del feature del GeoJSON
        state_code = feature['properties']['abbreviation']

        # Crear un nuevo mapa centrado en el estado
        state_map = folium.Map(
            location=[feature['properties']['lat'], feature['properties']['long']],
            zoom_start=6
        )

        # Agregar aeropuertos a este mapa
        add_airports_to_state(state_map, state_code)

        # Mostrar el mapa con aeropuertos en Streamlit
        st_folium(state_map, width=700, height=500)

    # Agregar capas de estados al mapa con un evento de clic
    folium.GeoJson(
        geojson_usa,
        name='USA States',
        style_function=lambda feature: {
            'fillColor': '#aaffaa',
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        },
        highlight_function=lambda feature: {
            'fillColor': '#ffafaa',
            'color': 'red',
            'weight': 3,
        },
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['State:']),
    ).add_to(mapa)

    # Mostrar el mapa base en Streamlit
    st_folium(mapa, width=700, height=500, key="main_map")
