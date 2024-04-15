import streamlit as st
from modules.carga_dec_2022 import cargar_unir_2022 
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.correlacion_variables import graficar_correlacion_variables
from modules.graph.correlacion_lineal import graficar_correlacion_lineal
from modules.graph.retrasos_mas_15 import graficar_retrasos_mas_15
from modules.graph.retrasos_mas_15_festivos import graficar_retrasos_mas_15_festivos
from modules.graph.cantidad_llegadas_salidas_hora import graficar_cantidad_llegadas_salidas_por_hora
from modules.graph.cantidad_retrasos_hora import graficar_cantidad_retrasos_por_hora
from modules.graph.dias_semana_con_sin_retrasos import graficar_dias_semana_con_sin_retrasos
from modules.graph.total_minutos_tipo_retraso import graficar_total_minutos_por_tipo_retraso
from modules.graph.analisis_retrasos_aereos import graficar_analisis_retrasos_aereos



def display():
    st.title('Datos diciembre 2022')
    
    # Llama a la función para cargar el DataFrame de 2022
    df_dec_2022 = cargar_unir_2022()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_dec_2022, 'fecha')

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
        st.markdown("""
        ### Análisis de Retrasos en Salidas y Llegadas de Vuelos

        Los siguientes gráficos de pastel representan la proporción de vuelos que experimentaron retrasos de más de 15 minutos en sus salidas y llegadas, respectivamente. Estos retrasos son indicativos de las eficiencias operativas y pueden estar influenciados por una variedad de factores, incluidos problemas técnicos, condiciones climáticas adversas y congestión del tráfico aéreo.

        Un 'retraso' se define como cualquier demora de más de 15 minutos en la salida o llegada programada del vuelo. La comparación entre los dos gráficos permite visualizar la relación entre los retrasos en la salida y los posibles impactos correspondientes en la llegada de los vuelos.

        Estos insights son cruciales para las aerolíneas y los aeropuertos para implementar estrategias destinadas a mejorar la puntualidad y la experiencia general del pasajero.
    """)

        # Asegúrate de tener la función graficar_retrasos_mas_15 importada y disponible para usar
        graficar_retrasos_mas_15(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en Días Festivos vs. Días Laborables
        
        Los gráficos de pastel presentados comparan el porcentaje de vuelos con retrasos menores o iguales a 15 minutos en salidas y llegadas, diferenciando entre días laborables y festivos. Esta distinción permite observar si los días festivos, que podrían conllevar un volumen diferente de tráfico aéreo, afectan la puntualidad de los vuelos de manera significativa.
        
        La visualización en cuatro partes ofrece una comparación directa, permitiendo evaluar de manera rápida si existe una variación notable en los porcentajes de retraso entre los tipos de días. Este análisis puede proporcionar insights valiosos para la planificación de operaciones y la gestión de expectativas de los pasajeros durante diferentes periodos.
    """)
        
        graficar_retrasos_mas_15_festivos(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Cantidad de Llegadas y Salidas por Rangos Horarios
        
        El gráfico compara la cantidad de vuelos que salen y llegan en diferentes rangos horarios a lo largo del día. Cada par de barras representa un rango horario específico, con la primera barra mostrando la cantidad de salidas y la segunda barra mostrando la cantidad de llegadas durante ese período.
        
        Esta visualización ayuda a entender los patrones de tráfico aéreo, identificando las horas pico de actividad en los aeropuertos y permitiendo evaluar cómo la distribución de las llegadas y salidas se compara a lo largo del día.
    """)
        
        graficar_cantidad_llegadas_salidas_por_hora(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Cantidad de Retrasos en Llegadas y Salidas por Rangos Horarios
        
        El gráfico compara la cantidad de retrasos superiores a 15 minutos que ocurren en diferentes rangos horarios a lo largo del día tanto para salidas como para llegadas de vuelos. Cada par de barras representa un rango horario específico, con la primera barra mostrando la cantidad de retrasos en salidas y la segunda barra mostrando la cantidad de retrasos en llegadas durante ese período.
        
        Esta visualización ayuda a identificar las horas pico de retrasos en los aeropuertos, lo que puede ser crucial para la planificación operativa y la mejora de la puntualidad en los servicios de vuelo.
    """)
        
        graficar_cantidad_retrasos_por_hora(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Análisis de Retrasos por Día de la Semana
        
        Este gráfico de barras apiladas muestra la cantidad de vuelos con y sin retrasos (definidos como retrasos superiores a 15 minutos en la llegada) para cada día de la semana. Las barras apiladas permiten comparar visualmente la proporción de vuelos puntuales frente a los retrasados para cada día, ofreciendo insights sobre los patrones de puntualidad a lo largo de la semana.
        
        La visualización puede ayudar a identificar los días con mayor propensión a retrasos, lo cual es valioso tanto para las aerolíneas en la optimización de sus operaciones como para los pasajeros en la planificación de sus viajes.
    """)
        
        graficar_dias_semana_con_sin_retrasos(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Total de Minutos por Tipo de Retraso
        
        Este gráfico de barras muestra la suma total de minutos de retraso acumulados para diferentes categorías: retraso por aerolínea, retraso por clima, retraso por sistema de aviación y retraso por seguridad. Cada barra representa una categoría específica de retraso y la altura de la barra indica el total acumulado de minutos de retraso asociado a esa categoría.
        
        Esta visualización es útil para identificar los principales factores que contribuyen a los retrasos en los vuelos, lo que puede ayudar a las aerolíneas y autoridades aeronáuticas a implementar medidas dirigidas a mitigar los retrasos y mejorar la puntualidad.
    """)
        
        graficar_total_minutos_por_tipo_retraso(df_dec_2022)

        st.markdown("---")

        st.markdown("""
        ### Análisis de Retrasos Aéreos

        Estos dos gráficos circulares presentan un análisis de los retrasos aéreos desde dos perspectivas: el tiempo de retraso acumulado y el porcentaje de ocurrencias de cada tipo de retraso.

        El primer gráfico muestra la distribución del tiempo total de retraso atribuido a cada categoría, proporcionando una visión de los tipos de retraso que tienen un mayor impacto en términos de tiempo perdido.

        El segundo gráfico refleja la frecuencia con la que ocurre cada tipo de retraso, ofreciendo insights sobre cuáles son más comunes, independientemente de la duración del tiempo de retraso asociado.
    """)
        
        graficar_analisis_retrasos_aereos(df_dec_2022)

        st.markdown("---")

