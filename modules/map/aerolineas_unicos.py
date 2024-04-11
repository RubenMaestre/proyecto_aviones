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

    # Intenta cargar la imagen desde el directorio local, considerando diferentes extensiones
    imagen_path = None
    for ext in ['svg', 'jpg', 'png']:
        path = f'sources/aerolineas/{aerolinea_seleccionada}.{ext}'
        if os.path.exists(path):
            imagen_path = path
            break

    # Si se encuentra una imagen, mostrarla centrada
    if imagen_path:
        st.image(imagen_path, width=600, align='center', caption=aerolinea_info['aerolinea'])

    # Mostrar la tabla con la información de la aerolínea
        tabla_html = f"""
    <table style='border: 3px solid; border-collapse: collapse;'>
        <tr>
            <td style='border: 3px solid;'><b>Nombre:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['aerolinea']}</td>
        </tr>
        <tr>
            <td style='border: 3px solid;'><b>IATA:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['IATA']}</td>
            <td style='border: 3px solid;'><b>ICAO:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['ICAO']}</td>
        </tr>
        <tr>
            <td style='border: 3px solid;'><b>País de la aerolínea:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['country']}</td>
        </tr>
        <tr>
            <td style='border: 3px solid;'><b>Grupo:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['Group']}</td>
            <td style='border: 3px solid;'><b>Aeropuerto Base:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['Base']}</td>
        </tr>
        <tr>
            <td style='border: 3px solid;'><b>Tamaño Flota:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['fleet_size']}</td>
            <td style='border: 3px solid;'><b>Edad de la Flota:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['average_fleet_Age']}</td>
            <td style='border: 3px solid;'><b>Web:</b></td>
            <td style='border: 3px solid;'>{aerolinea_info['official_site']}</td>
        </tr>
    </table>
    """
    st.markdown(tabla_html, unsafe_allow_html=True)

    # Mostrar el título "Sobre la compañía"
    st.markdown("### Sobre la compañía:")

    # Mostrar el Resumen de la aerolínea seleccionada
    st.write(aerolinea_info['Resumen'])