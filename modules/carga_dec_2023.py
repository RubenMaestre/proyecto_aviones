import pandas as pd
import streamlit as st

@st.cache
def cargar_unir_2023():
    if 'df_dec_2023' not in st.session_state:
        archivo = 'data/pickles/df_2023.parquet'
        # Cargar el DataFrame desde el archivo Parquet
        st.session_state.df_dec_2023 = pd.read_parquet(archivo)

    return st.session_state.df_dec_2023
