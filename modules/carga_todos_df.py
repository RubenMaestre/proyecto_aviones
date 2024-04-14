import pandas as pd
import streamlit as st

@st.cache_data
def cargar_todos_df():
    # Define los años y la cantidad de archivos pickle por año
    anios = {
        '2023': 2,
        '2022': 2,
        '2021': 2
    }
    
    if 'df_todos' not in st.session_state:
        dataframes = []
        
        # Iterar sobre cada año y cargar cada pickle correspondiente
        for anio, num_archivos in anios.items():
            for i in range(1, num_archivos + 1):
                archivo = f'data/pickles/df_{anio}_{i}.pkl'
                df_temp = pd.read_pickle(archivo)
                dataframes.append(df_temp)
        
        # Concatenar todos los DataFrames en uno solo
        st.session_state.df_todos = pd.concat(dataframes, ignore_index=True)

    # Devolver el DataFrame desde el estado de sesión
    return st.session_state.df_todos
