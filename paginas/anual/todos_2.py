import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.correlacion_variables import graficar_correlacion_variables
from modules.graph.correlacion_lineal import graficar_correlacion_lineal
from modules.graph.numero_vuelos_dias_diciembre import graficar_numero_vuelos_dias_diciembre
from modules.graph.numero_vuelos_acumulados_diciembre import graficar_numero_vuelos_acumulados_diciembre
from modules.graph.cantidad_llegadas_salidas_hora import graficar_cantidad_llegadas_salidas_por_hora


def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_todos, 'fecha')

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
        st.markdown("""
        ### Correlación Lineal entre Retraso en la Salida y Llegada de Vuelos
        
        El siguiente gráfico de dispersión muestra la relación entre el retraso en la salida y el retraso en la llegada de los vuelos. Cada punto en el gráfico representa un vuelo, ubicado según su tiempo de retraso en la salida (eje X) y su tiempo de retraso en la llegada (eje Y).
        
        La línea de tendencia, calculada mediante el método de mínimos cuadrados ordinarios (OLS), indica la existencia de una correlación lineal entre estas dos variables. Una correlación positiva significativa entre estos indicadores sugiere que los vuelos que experimentan retrasos en la salida tienden a sufrir retrasos similares en la llegada.
        
        Esta correlación es crucial para la planificación operativa de las aerolíneas y la gestión del tráfico aéreo, ya que comprender la relación entre los retrasos en la salida y la llegada puede ayudar a minimizar los impactos negativos en los horarios de los vuelos y la satisfacción de los pasajeros.
    """)

        graficar_correlacion_lineal(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Número de Vuelos por Días en Diciembre por Año
        
        Los gráficos muestran la cantidad de vuelos diarios durante el mes de diciembre para los años 2021, 2022 y 2023. Cada gráfico proporciona una visualización detallada del número de vuelos para un año específico, permitiendo observar tendencias, picos y variaciones diarias en la cantidad de vuelos.
        
        El gráfico 'Todos los Años' combina la información de los tres años, facilitando la comparación directa entre ellos y permitiendo identificar patrones recurrentes o cambios significativos en el número de vuelos durante el mismo periodo en años diferentes.
    """)
        
        graficar_numero_vuelos_dias_diciembre(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Número Acumulado de Vuelos por Días en Diciembre por Año
        
        Los gráficos presentan la evolución acumulativa del número de vuelos diarios durante el mes de diciembre para los años 2021, 2022 y 2023. Cada gráfico traza la suma acumulativa de vuelos desde el comienzo del mes, proporcionando una perspectiva de cómo la actividad de vuelo se incrementa a lo largo de diciembre.
        
        Estas visualizaciones permiten apreciar no solo los picos de actividad diaria sino también la tendencia general en la acumulación de vuelos a lo largo del mes, lo cual es particularmente útil para evaluar el volumen de tráfico aéreo y la planificación de recursos.
    """)
        
        graficar_numero_vuelos_acumulados_diciembre(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Cantidad de Llegadas y Salidas por Rangos Horarios
        
        El gráfico compara la cantidad de vuelos que salen y llegan en diferentes rangos horarios a lo largo del día. Cada par de barras representa un rango horario específico, con la primera barra mostrando la cantidad de salidas y la segunda barra mostrando la cantidad de llegadas durante ese período.
        
        Esta visualización ayuda a entender los patrones de tráfico aéreo, identificando las horas pico de actividad en los aeropuertos y permitiendo evaluar cómo la distribución de las llegadas y salidas se compara a lo largo del día.
    """)
        
        graficar_cantidad_llegadas_salidas_por_hora(df_todos)

        st.markdown("---")


