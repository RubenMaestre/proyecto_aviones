import pandas as pd
import streamlit as st

@st.cache
def cargar_todos_df():
    # Ruta al archivo único Parquet
    archivo = 'data/pickles/vuelos_limpio.parquet'
    
    if 'df_todos' not in st.session_state:
        # Cargar el DataFrame desde el archivo Parquet
        st.session_state.df_todos = pd.read_parquet(archivo)

    # Devolver el DataFrame desde el estado de sesión
    return st.session_state.df_todos


