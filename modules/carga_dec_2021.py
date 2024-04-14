import pandas as pd
import streamlit as st

@st.cache_data
def cargar_unir_2021():
    # Clave 'df_dec_2021' en el estado de sesión para verificar su existencia
    if 'df_dec_2021' not in st.session_state:
        archivo_1 = 'data/parquet/df_2021_1.parquet'
        archivo_2 = 'data/parquet/df_2021_2.parquet'

        # Cargar y unir los DataFrames solo si no existen en el estado de sesión
        df_2021_1 = pd.read_parquet(archivo_1)
        df_2021_2 = pd.read_parquet(archivo_2)

        # Guardar el DataFrame unido en el estado de sesión
        st.session_state.df_dec_2021 = pd.concat([df_2021_1, df_2021_2], ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión
    return st.session_state.df_dec_2021
