import pandas as pd
import streamlit as st

@st.cache_data
def cargar_unir_2021():
    clave = 'df_dec_2021'  # Definir la clave que se utilizará en el estado de sesión
    
    # Verificar si la clave ya está en el estado de sesión
    if clave not in st.session_state:
        archivo = 'data/pickles/df_2021.parquet'
        # Cargar el DataFrame desde el archivo Parquet y guardarlo en el estado de sesión
        st.session_state[clave] = pd.read_parquet(archivo)
    
    # Devolver el DataFrame desde el estado de sesión
    return st.session_state[clave]

