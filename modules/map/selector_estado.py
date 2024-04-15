import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

def mostrar_mapa_aeropuertos_por_estado():
    df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')
    geojson_usa = 'data/us-states.json'
    
    estado_seleccionado = st.session_state.get('estado_seleccionado', None)
    
    nombres_estados = df_aeropuertos_unicos['nombre_estado'].unique()
    nombre_estado_seleccionado = st.selectbox('Selecciona un estado:', sorted(nombres_estados), key='estado_selectbox', index=sorted(nombres_estados).index(estado_seleccionado) if estado_seleccionado else 0)

    mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    
    folium.GeoJson(
        geojson_usa,
        name='USA States',
        style_function=lambda feature: {'fillColor': '#aaffaa', 'color': 'black', 'weight': 2, 'dashArray': '5, 5'},
        highlight_function=lambda feature: {'fillColor': '#ffafaa', 'color': 'red', 'weight': 3},
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['State:']),
        # Imaginative part: capturing clicks to update session state (not directly possible)
    ).add_to(mapa)
    
    st_folium(mapa, width=1280, height=720, key="map")

    if st.session_state.get('update_selectbox_from_map_click', False):
        st.session_state['estado_selectbox'] = st.session_state['estado_seleccionado']
        st.session_state['update_selectbox_from_map_click'] = False

mostrar_mapa_aeropuertos_por_estado()