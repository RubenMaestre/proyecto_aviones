import pandas as pd
import streamlit as st
from .carga_dec_2021 import cargar_unir_2021
from .carga_dec_2022 import cargar_unir_2022
from .carga_dec_2023 import cargar_unir_2023

def cargar_todos_df():
    # Intentar cargar cada DataFrame de año, ya sea desde el estado de la aplicación o directamente desde los archivos pickle
    try:
        # Suponiendo que puedes verificar si ya están cargados en el estado de la aplicación (ajusta según tu implementación)
        df_dec_2021 = st.session_state.df_dec_2021
    except AttributeError:
        df_dec_2021 = cargar_unir_2021()

    try:
        df_dec_2022 = st.session_state.df_dec_2022
    except AttributeError:
        df_dec_2022 = cargar_unir_2022()

    try:
        df_dec_2023 = st.session_state.df_dec_2023
    except AttributeError:
        df_dec_2023 = cargar_unir_2023()

    # Unir todos los DataFrames en uno solo
    df_todos = pd.concat([df_dec_2021, df_dec_2022, df_dec_2023], ignore_index=True)

    return df_todos

