import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_por_estado_interactivo():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Crear una lista de estados
    estados = df_aeropuertos_unicos['estado'].unique()
    estados = sorted(estados)  # Ordenar alfabéticamente si se desea

    # Usar st.radio para que el usuario seleccione un estado
    estado_seleccionado = st.radio('Selecciona un estado:', estados)

    # Actualizar el mapa basado en la selección
    actualizar_mapa(estado_seleccionado)

def actualizar_mapa(estado_seleccionado):
    # Filtrar los datos para el estado seleccionado
    df_aeropuertos_estado = df_aeropuertos_unicos[df_aeropuertos_unicos['estado'] == estado_seleccionado]

    # Centrar el mapa en el estado seleccionado
    centro_estado = [df_aeropuertos_estado['latitude'].mean(), df_aeropuertos_estado['longitude'].mean()]

    # Crear el mapa centrado en el estado seleccionado
    mapa_estado = folium.Map(location=centro_estado, zoom_start=7)

    # Agregar marcadores para cada aeropuerto en el estado
    for _, row in df_aeropuertos_estado.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=f"{row['nombre_aeropuerto']} ({row['codigo_aeropuerto']})",
            icon=folium.Icon(color='blue', icon='plane', prefix='fa')
        ).add_to(mapa_estado)

    # Mostrar el mapa actualizado en Streamlit
    st_folium(mapa_estado, width=1280, height=720)