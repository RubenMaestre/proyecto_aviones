import streamlit as st
from modules.carga_dec_2021 import cargar_unir_2021  # Asegúrate de que la ruta y el nombre de la función sean correctos

def display():
    st.title('Datos diciembre 2021')
    
    # Llama a la función para cargar el DataFrame de 2021
    df_dec_2021 = cargar_unir_2021()

    # Ahora puedes usar df_dec_2021 para cualquier operación subsiguiente, como visualización, análisis, etc.
    # Por ejemplo:
    st.write(df_dec_2021.head())  # Muestra las primeras filas del DataFrame para confirmar que se ha cargado correctamente