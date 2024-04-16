import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_por_estado():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')
    geojson_usa = 'data/us-states.json'  # Asegúrate de que la ruta al archivo GeoJSON es correcta

    # Crear un selector de nombres de estados en español
    nombres_estados = df_aeropuertos_unicos['nombre_estado'].unique()
    nombre_estado_seleccionado = st.selectbox('Selecciona un estado:', sorted(nombres_estados), key='estado_seleccionado')

    # Función para actualizar el mapa con los aeropuertos del nombre del estado seleccionado
    def actualizar_mapa(nombre_estado):
        # Filtrar aeropuertos por el nombre del estado seleccionado
        df_aeropuertos_estado = df_aeropuertos_unicos[df_aeropuertos_unicos['nombre_estado'] == nombre_estado]

        # Encuentra el centro del estado para centrar el mapa
        centro_estado = [df_aeropuertos_estado['latitude'].mean(), df_aeropuertos_estado['longitude'].mean()]

        # Crea un nuevo mapa centrado en el estado seleccionado
        mapa_estado = folium.Map(location=centro_estado, zoom_start=5)

        # Agregar GeoJSON para marcar los estados
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

        # Agrega marcadores para cada aeropuerto en el estado
        for index, row in df_aeropuertos_estado.iterrows():
            folium.Marker(
                [row['latitude'], row['longitude']],
                popup=f"{row['nombre_aeropuerto']} ({row['codigo_aeropuerto']})",
                icon=folium.Icon(color='blue', icon='plane', prefix='fa')
            ).add_to(mapa_estado)

        # Muestra el mapa actualizado en Streamlit
        st_folium(mapa_estado, width=1280, height=720)

    # Actualizar el mapa cuando se selecciona un nombre de estado
    actualizar_mapa(nombre_estado_seleccionado)

# Llamar a la función para mostrar el mapa
mostrar_mapa_aeropuertos_por_estado()
