import streamlit as st
from modules.carga_dec_2021 import cargar_unir_2021
from modules.datos_df_cargados import mostrar_estadisticas_df

def display():
    st.title('Datos diciembre 2021')
    
    # Llama a la función para cargar el DataFrame de 2021
    df_dec_2021 = cargar_unir_2021()

    mostrar_estadisticas_df(df_dec_2021, 'fecha')