import pandas as pd
import streamlit as st

@st.cache
def cargar_unir_2022():
    if 'df_dec_2022' not in st.session_state:
        archivo = 'data/pickles/df_2022.parquet'
        # Cargar el DataFrame desde el archivo Parquet
        st.session_state.df_dec_2022 = pd.read_parquet(archivo)

    return st.session_state.df_dec_2022

