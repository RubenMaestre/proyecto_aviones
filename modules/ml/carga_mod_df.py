import pandas as pd
import streamlit as st

def unir_df_modelo():
    # Verifica si el DataFrame ya está en el estado de sesión
    if 'df_modelo' not in st.session_state:
        # Rutas a los archivos pickle
        archivo_1 = 'data/pickles/df_modelo_1.pkl'
        archivo_2 = 'data/pickles/df_modelo_2.pkl'

        # Cargar los DataFrames desde los archivos pickle
        df_modelo_1 = pd.read_pickle(archivo_1)
        df_modelo_2 = pd.read_pickle(archivo_2)

        # Unir los dos DataFrames en uno solo y almacenarlo en el estado de sesión
        st.session_state.df_modelo = pd.concat([df_modelo_1, df_modelo_2], ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión, asegurándote de que la variable sea la correcta
    df_modelo = st.session_state.df_modelo
    return df_modelo
