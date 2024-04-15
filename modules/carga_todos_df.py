import pandas as pd
import streamlit as st

@st.cache_data
def cargar_todos_df():
    # Clave a verificar
    clave = 'df_todos'
    
    # Verificar si la clave ya está en el estado de sesión
    if clave not in st.session_state:
        # Ruta al archivo Parquet
        archivo = 'data/pickles/vuelos_limpio.parquet'
        # Cargar el DataFrame desde el archivo Parquet y guardarlo en el estado de sesión
        st.session_state[clave] = pd.read_parquet(archivo)
    
    # Devolver el DataFrame desde el estado de sesión
    return st.session_state[clave]
