import streamlit as st
from modules.carga_dec_2023 import cargar_unir_2023  # Asegúrate de que la ruta y el nombre de la función sean correctos

def display():
    st.title('Datos diciembre 2023')
    
    # Llama a la función para cargar el DataFrame de 2023
    df_dec_2023 = cargar_unir_2023()

