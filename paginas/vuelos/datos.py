# paginas/vuelos/datos.py
import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.graph.diagrama_distancia_millas import graficar_diagrama_distancia_millas
from modules.graph.histograma_distancias_millas import graficar_histograma_distancias_millas
from modules.graph.relacion_retrasos_millas import graficar_relacion_retrasos_millas
from modules.graph.maxima_distancia_millas import graficar_maxima_distancia_millas



def display():
    st.title('Datoys y curiosidades sobre distancias')
    
    # Llama a la función para cargar y unir todos los DataFrames
    #df_todos = cargar_todos_df()

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
    
        st.markdown("""
        ### Diagrama de Caja de la Distancia en Millas

        Este diagrama de caja muestra la distribución de las distancias de vuelo en millas. La caja central representa el rango intercuartílico (IQR) que abarca desde el primer cuartil (Q1) hasta el tercer cuartil (Q3). La línea dentro de la caja marca la mediana. Los 'bigotes' se extienden hasta los puntos más distantes que todavía se consideran no ser valores atípicos, y los puntos individuales representan los valores atípicos en los datos.

        Este tipo de visualización es útil para comprender la variabilidad de las distancias de vuelo, identificar posibles valores atípicos y obtener una idea general sobre la centralidad y la dispersión de los datos.
    """)

        #graficar_diagrama_distancia_millas(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Histograma de Distancia en Millas

        Este histograma muestra la distribución de las distancias de vuelo en millas. Cada barra representa el número de vuelos que caen dentro de un rango específico de distancias.

        Las líneas verticales representan la media (en rojo) y la mediana (en verde) de las distancias. La media proporciona el promedio de la distancia de los vuelos, mientras que la mediana indica el valor medio, dividiendo el conjunto de datos en dos mitades iguales.

        Este análisis permite visualizar la distribución general de las distancias de vuelo y entender mejor las tendencias centrales de los datos.
    """)
        
        #graficar_histograma_distancias_millas(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Relación entre Distancia en Millas y Retrasos

        Este gráfico de barras compara la cantidad de vuelos con y sin retrasos (definidos como retrasos superiores a 15 minutos en la llegada) para diferentes rangos de distancia de vuelo en millas. Esto permite visualizar cómo la distancia recorrida por el vuelo podría influir en la incidencia de retrasos.

        La visualización puede ser útil para entender si los vuelos más largos son más susceptibles a retrasos en comparación con los vuelos más cortos, y podría ayudar a las aerolíneas a optimizar sus operaciones y estrategias de manejo de retrasos.
    """)
        
        #graficar_relacion_retrasos_millas(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Top 20 de Máximas Distancias entre Aeropuertos Únicos

        Este gráfico muestra el top 20 de las mayores distancias registradas entre pares de aeropuertos únicos. Cada barra representa un par de aeropuertos y la altura de la barra indica la máxima distancia en millas que ha sido registrada entre ellos.

        Este análisis puede ofrecer insights sobre las rutas más largas operadas y cómo estas distancias extremas son gestionadas por las aerolíneas, además de los desafíos logísticos y operativos que representan.
    """)
        
        #graficar_maxima_distancia_millas(df_todos)

        st.markdown("---")
