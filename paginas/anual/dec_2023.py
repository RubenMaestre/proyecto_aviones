import streamlit as st
from modules.carga_dec_2023 import cargar_unir_2023
from modules.datos_df_cargados import mostrar_estadisticas_df

def display():
    st.title('Datos diciembre 2023')
    
    # Llama a la función para cargar el DataFrame de 2023
    df_dec_2023 = cargar_unir_2023()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_dec_2023, 'fecha')
