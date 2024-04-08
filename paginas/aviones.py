# paginas/aviones.py
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from paginas.vuelos import aerolineas, aeropuertos, datos

# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_pickle('data/aeropuertos_unicos.pkl')

def display():
    st.title('Vuelos en USA')

    # Define las columnas para las imágenes/botones
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("sources/aviones.jpg", width=250)
        if st.button('Ver Aviones', key='btn_aviones'):
            st.session_state.subpagina = 'aviones'

    with col2:
        st.image("sources/aeropuertos.jpg", width=250)
        if st.button('Ver Aeropuertos', key='btn_aeropuertos'):
            st.session_state.subpagina = 'aeropuertos'

    with col3:
        st.image("sources/aerolineas.jpg", width=250)
        if st.button('Ver Aerolíneas', key='btn_aerolineas'):
            st.session_state.subpagina = 'aerolineas'

    with col4:
        st.image("sources/datos.jpg", width=250)
        if st.button('Ver Datos', key='btn_datos'):
            st.session_state.subpagina = 'datos'

    # Navegación interna basada en el estado de la sesión
    if 'subpagina' in st.session_state:
        if st.session_state.subpagina == 'aviones':
            # Contenido específico de 'aviones'
            pass  # Aquí puedes colocar contenido o llamadas a funciones específicas para 'aviones'
        elif st.session_state.subpagina == 'aeropuertos':
            aeropuertos.display()
        elif st.session_state.subpagina == 'aerolineas':
            aerolineas.display()
        elif st.session_state.subpagina == 'datos':
            datos.display()

    # Mostrar el mapa base con Folium (esto siempre se muestra, independientemente de la subpágina)
    mapa = folium.Map(location=[38.2699, 30.7126], zoom_start=2)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)
    st_folium(mapa, width=1280, height=720, key="unique_map_key")
