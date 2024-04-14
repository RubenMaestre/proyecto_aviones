import pandas as pd
import streamlit as st

@st.cache_data
def cargar_unir_2023():
    # Clave 'df_dec_2023' en el estado de sesión para verificar su existencia
    if 'df_dec_2023' not in st.session_state:
        archivo_1 = 'data/parquet/df_2023_1.parquet'
        archivo_2 = 'data/parquet/df_2023_2.parquet'

        # Cargar y unir los DataFrames solo si no existen en el estado de sesión
        df_2023_1 = pd.read_parquet(archivo_1)
        df_2023_2 = pd.read_parquet(archivo_2)

        # Guardar el DataFrame unido en el estado de sesión
        st.session_state.df_dec_2023 = pd.concat([df_2023_1, df_2023_2], ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión
    return st.session_state.df_dec_2023
