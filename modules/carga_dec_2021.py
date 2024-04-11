import pandas as pd
import streamlit as st

def cargar_unir_2021():
    # Verifica si el DataFrame ya está en el estado de sesión
    if 'df_dec_2021' not in st.session_state:
        # Rutas a los archivos pickle
        archivo_1 = 'data/pickles/df_2021_1.pkl'
        archivo_2 = 'data/pickles/df_2021_2.pkl'

        # Cargar los DataFrames desde los archivos pickle
        df_2021_1 = pd.read_pickle(archivo_1)
        df_2021_2 = pd.read_pickle(archivo_2)

        # Unir los dos DataFrames en uno solo y almacenarlo en el estado de sesión
        st.session_state.df_dec_2021 = pd.concat([df_2021_1, df_2021_2], ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión, puedes llamar a esta variable local como prefieras
    df_dec_2021 = st.session_state.df_dec_2021
    return df_dec_2021