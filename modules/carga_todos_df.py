import pandas as pd
import streamlit as st
from .carga_dec_2021 import cargar_unir_2021
from .carga_dec_2022 import cargar_unir_2022
from .carga_dec_2023 import cargar_unir_2023

@st.cache(allow_output_mutation=True)
def cargar_todos_df():
    # Verificar si el DataFrame combinado ya está en el estado de sesión
    if 'df_todos' not in st.session_state:
        # Cargar cada uno de los DataFrames anuales usando las funciones respectivas
        df_dec_2021 = cargar_unir_2021()
        df_dec_2022 = cargar_unir_2022()
        df_dec_2023 = cargar_unir_2023()

        # Concatenar los DataFrames cargados en uno solo
        st.session_state.df_todos = pd.concat([df_dec_2021, df_dec_2022, df_dec_2023], ignore_index=True)

    # Devolver el DataFrame combinado desde el estado de sesión
    return st.session_state.df_todos
