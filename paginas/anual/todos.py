import streamlit as st
from modules.carga_todos_df import cargar_todos_df  # Asegúrate de que la ruta y el nombre de la función sean correctos

def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Ahora puedes usar df_todos para cualquier operación subsiguiente, como visualización, análisis, etc.
    # Por ejemplo:
    st.write(df_todos.head())  # Muestra las primeras filas del DataFrame para confirmar que se ha cargado correctamente

    # Aquí puedes añadir más lógica para trabajar con df_todos, como visualizaciones o análisis adicionales
