import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def cargar_unir_2023():
    clave = 'df_dec_2023'  # Definir la clave que se utilizará en el estado de sesión
    
    # Verificar si la clave ya está en el estado de sesión
    if clave not in st.session_state:
        archivo = 'data/pickles/df_2023.parquet'
        # Cargar el DataFrame desde el archivo Parquet y guardarlo en el estado de sesión
        st.session_state[clave] = pd.read_parquet(archivo)
    
    # Devolver el DataFrame desde el estado de sesión
    return st.session_state[clave]
