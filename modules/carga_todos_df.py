import pandas as pd
import streamlit as st
from .carga_dec_2021 import cargar_unir_2021
from .carga_dec_2022 import cargar_unir_2022
from .carga_dec_2023 import cargar_unir_2023

def cargar_todos_df():
    if 'df_todos' not in st.session_state:
        df_dec_2021 = cargar_unir_2021()
        df_dec_2022 = cargar_unir_2022()
        df_dec_2023 = cargar_unir_2023()

        # Unir todos los DataFrames en uno solo
        st.session_state.df_todos = pd.concat([df_dec_2021, df_dec_2022, df_dec_2023], ignore_index=True)
    
    df_todos = st.session_state.df_todos
    return df_todos