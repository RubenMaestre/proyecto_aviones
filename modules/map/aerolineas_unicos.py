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

    # Mostrar tabla con información de la aerolínea
    col1, col2 = st.columns([3, 2])  # Ajusta la proporción de las columnas según necesites

    with col1:
        st.markdown(f"### {aerolinea_info['aerolinea']}")
        st.write(aerolinea_info['Resumen'])

    with col2:
        st.image(aerolinea_info['Imagen_URL'], width=400, caption=aerolinea_info['aerolinea'])
