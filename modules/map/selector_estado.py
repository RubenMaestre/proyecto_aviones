import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_por_estado():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

    # Crear un selector de estados
    estados = df_aeropuertos_unicos['estado'].unique()
    estado_seleccionado = st.selectbox('Selecciona un estado:', estados)

    # Función para actualizar el mapa con los aeropuertos del estado seleccionado
    def actualizar_mapa(estado):
        # Filtrar aeropuertos por el estado seleccionado
        df_aeropuertos_estado = df_aeropuertos_unicos[df_aeropuertos_unicos['estado'] == estado]
        
        # Encuentra el centro del estado para centrar el mapa (esto es un ejemplo, podrías necesitar una mejor lógica)
        centro_estado = [df_aeropuertos_estado['latitude'].mean(), df_aeropuertos_estado['longitude'].mean()]
        
        # Crea un nuevo mapa centrado en el estado seleccionado
        mapa_estado = folium.Map(location=centro_estado, zoom_start=7)
        
        # Agrega marcadores para cada aeropuerto en el estado
        for index, row in df_aeropuertos_estado.iterrows():
            folium.Marker(
                [row['latitude'], row['longitude']],
                popup=f"{row['nombre_aeropuerto']} ({row['codigo_aeropuerto']})",
                icon=folium.Icon(color='blue', icon='plane', prefix='fa')
            ).add_to(mapa_estado)
        
        # Muestra el mapa actualizado en Streamlit
        st_folium(mapa_estado, width=1280, height=720)

    # Actualizar el mapa cuando se selecciona un estado
    actualizar_mapa(estado_seleccionado)
