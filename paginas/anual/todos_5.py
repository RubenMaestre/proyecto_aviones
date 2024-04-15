import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.graph.diagrama_distancia_millas import graficar_diagrama_distancia_millas
from modules.graph.histograma_distancias_millas import graficar_histograma_distancias_millas
from modules.graph.relacion_retrasos_millas import graficar_relacion_retrasos_millas
from modules.graph.maxima_distancia_millas import graficar_maxima_distancia_millas



def display():
    st.title('Datos y curiosidades sobre distancias')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
        st.markdown("""
        ### Top 20 de Máximas Distancias entre Aeropuertos Únicos

        Este gráfico muestra el top 20 de las mayores distancias registradas entre pares de aeropuertos únicos. Cada barra representa un par de aeropuertos y la altura de la barra indica la máxima distancia en millas que ha sido registrada entre ellos.

        Este análisis puede ofrecer insights sobre las rutas más largas operadas y cómo estas distancias extremas son gestionadas por las aerolíneas, además de los desafíos logísticos y operativos que representan.
    """)
        
        graficar_maxima_distancia_millas(df_todos)

        st.markdown("---")
