import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df

def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_todos, 'fecha')
