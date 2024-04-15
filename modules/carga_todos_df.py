import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def cargar_todos_df():
    # Verifica si 'df_todos' ya está en el estado de sesión
    if 'df_todos' not in st.session_state:
        # Aquí, ajusta la ruta y el archivo según tus necesidades
        archivo = 'data/pickles/vuelos_limpio.parquet'
        # Cargar el DataFrame desde el archivo Parquet
        st.session_state.df_todos = pd.read_parquet(archivo)

    return st.session_state.df_todos

