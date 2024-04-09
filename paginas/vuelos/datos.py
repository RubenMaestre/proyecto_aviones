import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.graph.diagrama_distancia_millas import graficar_diagrama_distancia_millas


def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
    
        st.markdown("""
        ### Diagrama de Caja de la Distancia en Millas

        Este diagrama de caja muestra la distribución de las distancias de vuelo en millas. La caja central representa el rango intercuartílico (IQR) que abarca desde el primer cuartil (Q1) hasta el tercer cuartil (Q3). La línea dentro de la caja marca la mediana. Los 'bigotes' se extienden hasta los puntos más distantes que todavía se consideran no ser valores atípicos, y los puntos individuales representan los valores atípicos en los datos.

        Este tipo de visualización es útil para comprender la variabilidad de las distancias de vuelo, identificar posibles valores atípicos y obtener una idea general sobre la centralidad y la dispersión de los datos.
    """)

        graficar_diagrama_distancia_millas(df_todos)

        st.markdown("---")
