import os
import pandas as pd
import streamlit as st

def mostrar_aerolineas_unicos():
    # Cargar los datos de aerolíneas
    df_aerolineas_unicas = pd.read_pickle('data/aerolineas_unicos.pkl')

    # Selector de Aerolínea
    aerolineas = df_aerolineas_unicas['aerolinea'].tolist()
    aerolinea_seleccionada = st.selectbox('Selecciona una aerolínea:', aerolineas)

    # Información de la Aerolínea seleccionada
    aerolinea_info = df_aerolineas_unicas[df_aerolineas_unicas['aerolinea'] == aerolinea_seleccionada].iloc[0]

    # Mostrar la tabla con la información de la aerolínea
    tabla_data = [
        ['Nombre:', aerolinea_info['aerolinea']],
        ['IATA:', aerolinea_info['IATA'], 'ICAO:', aerolinea_info['ICAO']],
        ['País de la aerolínea:', aerolinea_info['country']],
        ['Grupo:', aerolinea_info['Group'], 'Aeropuerto Base:', aerolinea_info['Base']],
        ['Tamaño Flota:', aerolinea_info['fleet_size'], 'Edad de la Flota:', aerolinea_info['average_fleet_Age'], 'Web:', aerolinea_info['official_site']]
    ]
    for fila in tabla_data:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.write(fila[0])
        with col2:
            st.write(fila[1])
        if len(fila) > 2:
            with col3:
                st.write(fila[2])
        if len(fila) > 3:
            with col4:
                st.write(fila[3])
        if len(fila) > 4:
            with col5:
                st.write(fila[4])

    # Mostrar el título "Sobre la compañía"
    st.markdown("### Sobre la compañía:")

    # Intenta cargar la imagen desde el directorio local, considerando diferentes extensiones
    imagen_path = None
    for ext in ['svg', 'jpg', 'png']:
        path = f'sources/aerolineas/{aerolinea_seleccionada}.{ext}'
        if os.path.exists(path):
            imagen_path = path
            break

    # Si se encuentra una imagen, mostrarla centrada
    if imagen_path:
        st.image(imagen_path, width=600, caption=aerolinea_info['aerolinea'])

    # Mostrar el Resumen de la aerolínea seleccionada
    st.write(aerolinea_info['Resumen'])