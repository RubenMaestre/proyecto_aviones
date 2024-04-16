import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_aeropuertos_unicos():
    # Cargar los datos de aeropuertos
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')
    df_aeropuertos_unicos['latitude'] = pd.to_numeric(df_aeropuertos_unicos['latitude'], errors='coerce')
    df_aeropuertos_unicos['longitude'] = pd.to_numeric(df_aeropuertos_unicos['longitude'], errors='coerce')

    # Selector de Estado
    nombres_estados = sorted(df_aeropuertos_unicos['nombre_estado'].unique())
    nombre_estado_seleccionado = st.selectbox('Selecciona un estado:', nombres_estados)

    # Filtrar por Estado seleccionado
    df_estado = df_aeropuertos_unicos[df_aeropuertos_unicos['nombre_estado'] == nombre_estado_seleccionado]

    # Selector de Ciudad
    ciudades = sorted(df_estado['ciudad'].unique())
    ciudad_seleccionada = st.selectbox('Selecciona una ciudad:', ciudades)

    # Filtrar por Ciudad seleccionada
    df_ciudad = df_estado[df_estado['ciudad'] == ciudad_seleccionada]

    # Selector de Aeropuerto
    aeropuertos = df_ciudad['nombre_aeropuerto'].tolist()
    aeropuerto_seleccionado = st.selectbox('Selecciona un aeropuerto:', aeropuertos)

    # Información del Aeropuerto seleccionado
    aeropuerto_info = df_ciudad[df_ciudad['nombre_aeropuerto'] == aeropuerto_seleccionado].iloc[0]

    # Mostrar detalles del aeropuerto
    st.markdown(f"### {aeropuerto_info['nombre_aeropuerto']} Airport")

    # Tabla con información del aeropuerto
    info = aeropuerto_info[['ciudad', 'nombre_estado', 'latitude', 'longitude']].copy()
    info['latitude'] = info['latitude'].astype(str)
    info['longitude'] = info['longitude'].astype(str)
    info.columns = ['Ciudad', 'Estado', 'Latitud', 'Longitud']
    st.table(info)

    # Mostrar dirección en una nueva fila
    st.write(f"**Dirección:** {aeropuerto_info['direccion']}")

    # Mostrar el mapa
    location = [float(aeropuerto_info['latitude']), float(aeropuerto_info['longitude'])]
    mapa = folium.Map(location=location, zoom_start=12)
    folium.Marker(
        location,
        popup=f"{aeropuerto_info['nombre_aeropuerto']} Airport",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa)
    st_folium(mapa, width=1280, height=480)

    # Información de Wiki
    st.write(f"**Información:** {aeropuerto_info['wiki_info']}")
