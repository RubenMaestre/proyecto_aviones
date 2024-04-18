#modules/eda/botones_eda.py
import streamlit as st
import pandas as pd
import time

# Suponiendo que las funciones de carga están en sus respectivos módulos
from modules.carga_todos_df import cargar_todos_df
from modules.carga_dec_2023 import cargar_unir_2023
from modules.carga_dec_2022 import cargar_unir_2022
from modules.carga_dec_2021 import cargar_unir_2021

def seleccionar_datos(key_suffix):
    unique_key = f"seleccion_año_vuelos_{key_suffix}_{int(time.time())}"
    opcion_año = st.selectbox(
        "Selecciona el año:",
        ["Todos los años", "2023", "2022", "2021"],
        key=unique_key
    )
    st.session_state['selected_year'] = opcion_año  # Guarda la selección en el estado de sesión

    if opcion_año == "Todos los años":
        df = cargar_todos_df()
    elif opcion_año == "2023":
        df = cargar_unir_2023()
    elif opcion_año == "2022":
        df = cargar_unir_2022()
    elif opcion_año == "2021":
        df = cargar_unir_2021()
    return df

