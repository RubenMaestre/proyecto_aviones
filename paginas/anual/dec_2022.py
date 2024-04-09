import streamlit as st
from modules.carga_dec_2022 import cargar_unir_2022  # Asegúrate de que la ruta y el nombre de la función sean correctos

def display():
    st.title('Datos diciembre 2022')
    
    # Llama a la función para cargar el DataFrame de 2022
    df_dec_2022 = cargar_unir_2022()

    # Ahora puedes usar df_dec_2022 para cualquier operación subsiguiente, como visualización, análisis, etc.
    # Por ejemplo:
    st.write(df_dec_2022.head())  # Muestra las primeras filas del DataFrame para confirmar que se ha cargado correctamente