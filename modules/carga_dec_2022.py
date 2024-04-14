import pandas as pd
import streamlit as st

@st.cache_data
def cargar_unir_2022():
    # Clave 'df_dec_2023' en el estado de sesión para verificar su existencia
    if 'df_dec_2022' not in st.session_state:
        archivo_1 = 'data/pickles/df_2022_1.pkl'
        archivo_2 = 'data/pickles/df_2022_2.pkl'

        # Cargar y unir los DataFrames solo si no existen en el estado de sesión
        df_2022_1 = pd.read_pickle(archivo_1)
        df_2022_2 = pd.read_pickle(archivo_2)

        # Guardar el DataFrame unido en el estado de sesión
        st.session_state.df_dec_2022 = pd.concat([df_2022_1, df_2022_2], ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión
    return st.session_state.df_dec_2022
