import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_por_estado(key_suffix=''):
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')
    geojson_usa = 'data/us-states.json'
    nombres_estados = df_aeropuertos_unicos['nombre_estado'].unique()

    nombre_estado_seleccionado = st.selectbox(
        'Selecciona un estado:',
        sorted(nombres_estados),
        key=f'estado_seleccionado{key_suffix}'
    )

    def actualizar_mapa(nombre_estado):
        df_aeropuertos_estado = df_aeropuertos_unicos[df_aeropuertos_unicos['nombre_estado'] == nombre_estado]
        centro_estado = [df_aeropuertos_estado['latitude'].mean(), df_aeropuertos_estado['longitude'].mean()]
        mapa_estado = folium.Map(location=centro_estado, zoom_start=5)

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
            }
        ).add_to(mapa_estado)

        for index, row in df_aeropuertos_estado.iterrows():
            folium.Marker(
                [row['latitude'], row['longitude']],
                popup=f"{row['nombre_aeropuerto']} ({row['codigo_aeropuerto']})",
                icon=folium.Icon(color='blue', icon='plane', prefix='fa')
            ).add_to(mapa_estado)

        st_folium(mapa_estado, width=1280, height=720, key=f'mapa_aeropuertos{key_suffix}')

    actualizar_mapa(nombre_estado_seleccionado)

mostrar_mapa_aeropuertos_por_estado(key_suffix='_pagina_principal')
