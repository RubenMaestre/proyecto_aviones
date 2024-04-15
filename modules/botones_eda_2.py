import streamlit as st
import pandas as pd

# Suponiendo que las funciones de carga están en sus respectivos módulos
from modules.carga_todos_df import cargar_todos_df
from modules.carga_dec_2023 import cargar_unir_2023
from modules.carga_dec_2022 import cargar_unir_2022
from modules.carga_dec_2021 import cargar_unir_2021

def seleccionar_datos():
    opcion_año = st.selectbox("Selecciona el año:", ["2023", "2022", "2021", "Todos los años"])
    st.session_state.selected_year = opcion_año  # Guarda el año seleccionado en el estado de sesión
    
    # Carga los datos correspondientes
    if opcion_año == "2023":
        df = cargar_unir_2023()
    elif opcion_año == "2022":
        df = cargar_unir_2022()
    elif opcion_año == "2021":
        df = cargar_unir_2021()
    elif opcion_año == "Todos los años":
        df = cargar_todos_df()
    
    return df

df_seleccionado = seleccionar_datos()
