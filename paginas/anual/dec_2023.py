import streamlit as st
from modules.carga_dec_2023 import cargar_unir_2023
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea


def display():
    st.title('Datos diciembre 2023')
    
    # Llama a la función para cargar el DataFrame de 2023
    df_dec_2023 = cargar_unir_2023()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_dec_2023, 'fecha')

# Usamos st.columns para dividir la pantalla en dos columnas
    col1, col2 = st.columns(2)

    # En la primera columna, ponemos la gráfica de vuelos por aerolínea
    with col1:
        graficar_vuelos_por_aerolinea(df_dec_2023)

    # En la segunda columna, ponemos la gráfica de evolución de vuelos por aerolínea
    with col2:
        graficar_vuelos_por_aerolinea(df_dec_2023)
