import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.correlacion_variables import graficar_correlacion_variables
from modules.graph.correlacion_lineal import graficar_correlacion_lineal
from modules.graph.retrasos_mas_15 import graficar_retrasos_mas_15
from modules.graph.retrasos_mas_15_festivos import graficar_retrasos_mas_15_festivos
from modules.graph.numero_vuelos_dias_diciembre import graficar_numero_vuelos_dias_diciembre
from modules.graph.numero_vuelos_acumulados_diciembre import graficar_numero_vuelos_acumulados_diciembre
from modules.graph.cantidad_llegadas_salidas_hora import graficar_cantidad_llegadas_salidas_por_hora
from modules.graph.cantidad_retrasos_hora import graficar_cantidad_retrasos_por_hora
from modules.graph.dias_semana_con_sin_retrasos import graficar_dias_semana_con_sin_retrasos
from modules.graph.total_minutos_tipo_retraso import graficar_total_minutos_por_tipo_retraso
from modules.graph.analisis_retrasos_aereos import graficar_analisis_retrasos_aereos




def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Llama a la función para mostrar las estadísticas del DataFrame
    mostrar_estadisticas_df(df_todos, 'fecha')

    import streamlit as st
# Asegúrate de que los módulos siguientes estén correctamente importados
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea

def display():
    st.title('Todos los datos juntos')
    
    # Llama a la función para cargar y unir todos los DataFrames
    df_todos = cargar_todos_df()

    # Crear columnas para centrar el contenido
    col_izq, col_1, col_der = st.columns([1, 10, 1])

    with col_1:
        # Llama a la función para mostrar las estadísticas del DataFrame
        mostrar_estadisticas_df(df_todos, 'fecha')

        st.markdown("""
            ### Cantidad de vuelos nacionales por compañía aérea en Estados Unidos
            
            Esta gráfica muestra la distribución del número total de vuelos nacionales operados por diferentes compañías aéreas en Estados Unidos. Cada barra representa una aerolínea específica y la altura de la barra indica el número total de vuelos que esa aerolínea ha operado.
            
            Puedes utilizar esta información para identificar las aerolíneas con mayor y menor número de vuelos, lo que puede ser indicativo de su tamaño, alcance y actividad en el mercado de vuelos nacionales.
        """)

        # Llama a la función para mostrar la gráfica de vuelos por aerolínea
        graficar_vuelos_por_aerolinea(df_todos)

        st.markdown("---")

        st.markdown("""
            ### Evolución del número de vuelos por compañía aérea
            
            Esta visualización muestra cómo ha evolucionado el número de vuelos de cada compañía aérea a lo largo de los años 2021, 2022 y 2023. Cada línea representa una aerolínea diferente, y los puntos en la línea indican el número de vuelos operados en un año específico.
            
            Esta gráfica te permite observar tendencias a lo largo del tiempo, como el crecimiento o la disminución en el número de vuelos de una aerolínea, lo que puede reflejar cambios en su operativa, expansión del mercado o respuesta a la demanda de vuelos nacionales.
        """)

        # Todos años por aerolínea / evolución
        graficar_evolucion_vuelos_por_aerolinea(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Distribución de las horas de salida y llegada de los vuelos
        
        Estos diagramas de caja ilustran la distribución de las horas de salida y llegada de los vuelos, convertidas a minutos desde la medianoche, lo que ofrece una visión clara de los patrones típicos de operación de vuelo durante el día.
        
        En el diagrama de 'Salida', cada caja muestra el rango intercuartílico de la hora de salida de los vuelos, con la línea central representando la mediana. De manera similar, el diagrama de 'Llegada' refleja estas mismas estadísticas para las horas de llegada. Las 'antenas' que se extienden desde las cajas indican la variabilidad fuera del rango intercuartílico superior e inferior, y los puntos representan valores atípicos que se desvían significativamente de los demás.
        
        Este análisis puede ayudarte a comprender los horarios de mayor actividad en los aeropuertos, así como a identificar las horas en que los vuelos tienden a programarse con mayor o menor frecuencia.
    """)
        
        graficar_horas_vuelos(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Correlaciones Lineales de las Variables Numéricas
        
        Este mapa de calor muestra la correlación lineal entre diferentes variables numéricas relacionadas con los vuelos. Cada celda en el mapa de calor representa el coeficiente de correlación entre dos variables, donde el valor 1 indica una correlación positiva perfecta, -1 indica una correlación negativa perfecta, y 0 indica ninguna correlación.
        
        Los colores más cálidos (como el rojo) indican una correlación positiva más fuerte, mientras que los colores más fríos (como el azul) indican una correlación negativa. Las celdas de color más cercano al blanco representan una correlación cercana a cero.
        
        Este análisis es fundamental para identificar relaciones potenciales entre variables, lo que puede ser crucial para entender los factores que afectan a aspectos como los retrasos de vuelos, la duración de los vuelos y otros comportamientos operativos.
        
        Por ejemplo, una fuerte correlación positiva entre el 'retraso de salida' y el 'retraso de llegada' sugiere que los vuelos que se retrasan al despegar tienden a llegar también tarde a su destino. Identificar estas correlaciones puede ayudar a las aerolíneas y a los gestores de tráfico aéreo a mejorar la eficiencia y la puntualidad de los servicios de vuelo.
    """)

        graficar_correlacion_variables(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Correlación Lineal entre Retraso en la Salida y Llegada de Vuelos
        
        El siguiente gráfico de dispersión muestra la relación entre el retraso en la salida y el retraso en la llegada de los vuelos. Cada punto en el gráfico representa un vuelo, ubicado según su tiempo de retraso en la salida (eje X) y su tiempo de retraso en la llegada (eje Y).
        
        La línea de tendencia, calculada mediante el método de mínimos cuadrados ordinarios (OLS), indica la existencia de una correlación lineal entre estas dos variables. Una correlación positiva significativa entre estos indicadores sugiere que los vuelos que experimentan retrasos en la salida tienden a sufrir retrasos similares en la llegada.
        
        Esta correlación es crucial para la planificación operativa de las aerolíneas y la gestión del tráfico aéreo, ya que comprender la relación entre los retrasos en la salida y la llegada puede ayudar a minimizar los impactos negativos en los horarios de los vuelos y la satisfacción de los pasajeros.
    """)

        graficar_correlacion_lineal(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Análisis de Retrasos en Salidas y Llegadas de Vuelos

        Los siguientes gráficos de pastel representan la proporción de vuelos que experimentaron retrasos de más de 15 minutos en sus salidas y llegadas, respectivamente. Estos retrasos son indicativos de las eficiencias operativas y pueden estar influenciados por una variedad de factores, incluidos problemas técnicos, condiciones climáticas adversas y congestión del tráfico aéreo.

        Un 'retraso' se define como cualquier demora de más de 15 minutos en la salida o llegada programada del vuelo. La comparación entre los dos gráficos permite visualizar la relación entre los retrasos en la salida y los posibles impactos correspondientes en la llegada de los vuelos.

        Estos insights son cruciales para las aerolíneas y los aeropuertos para implementar estrategias destinadas a mejorar la puntualidad y la experiencia general del pasajero.
    """)

        # Asegúrate de tener la función graficar_retrasos_mas_15 importada y disponible para usar
        graficar_retrasos_mas_15(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en Días Festivos vs. Días Laborables
        
        Los gráficos de pastel presentados comparan el porcentaje de vuelos con retrasos menores o iguales a 15 minutos en salidas y llegadas, diferenciando entre días laborables y festivos. Esta distinción permite observar si los días festivos, que podrían conllevar un volumen diferente de tráfico aéreo, afectan la puntualidad de los vuelos de manera significativa.
        
        La visualización en cuatro partes ofrece una comparación directa, permitiendo evaluar de manera rápida si existe una variación notable en los porcentajes de retraso entre los tipos de días. Este análisis puede proporcionar insights valiosos para la planificación de operaciones y la gestión de expectativas de los pasajeros durante diferentes periodos.
    """)
        
        graficar_retrasos_mas_15_festivos(df_todos)

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

        st.markdown("""
        ### Cantidad de Retrasos en Llegadas y Salidas por Rangos Horarios
        
        El gráfico compara la cantidad de retrasos superiores a 15 minutos que ocurren en diferentes rangos horarios a lo largo del día tanto para salidas como para llegadas de vuelos. Cada par de barras representa un rango horario específico, con la primera barra mostrando la cantidad de retrasos en salidas y la segunda barra mostrando la cantidad de retrasos en llegadas durante ese período.
        
        Esta visualización ayuda a identificar las horas pico de retrasos en los aeropuertos, lo que puede ser crucial para la planificación operativa y la mejora de la puntualidad en los servicios de vuelo.
    """)
        
        graficar_cantidad_retrasos_por_hora(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Análisis de Retrasos por Día de la Semana
        
        Este gráfico de barras apiladas muestra la cantidad de vuelos con y sin retrasos (definidos como retrasos superiores a 15 minutos en la llegada) para cada día de la semana. Las barras apiladas permiten comparar visualmente la proporción de vuelos puntuales frente a los retrasados para cada día, ofreciendo insights sobre los patrones de puntualidad a lo largo de la semana.
        
        La visualización puede ayudar a identificar los días con mayor propensión a retrasos, lo cual es valioso tanto para las aerolíneas en la optimización de sus operaciones como para los pasajeros en la planificación de sus viajes.
    """)
        
        graficar_dias_semana_con_sin_retrasos(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Total de Minutos por Tipo de Retraso
        
        Este gráfico de barras muestra la suma total de minutos de retraso acumulados para diferentes categorías: retraso por aerolínea, retraso por clima, retraso por sistema de aviación y retraso por seguridad. Cada barra representa una categoría específica de retraso y la altura de la barra indica el total acumulado de minutos de retraso asociado a esa categoría.
        
        Esta visualización es útil para identificar los principales factores que contribuyen a los retrasos en los vuelos, lo que puede ayudar a las aerolíneas y autoridades aeronáuticas a implementar medidas dirigidas a mitigar los retrasos y mejorar la puntualidad.
    """)
        
        graficar_total_minutos_por_tipo_retraso(df_todos)

        st.markdown("---")

        st.markdown("""
        ### Análisis de Retrasos Aéreos

        Estos dos gráficos circulares presentan un análisis de los retrasos aéreos desde dos perspectivas: el tiempo de retraso acumulado y el porcentaje de ocurrencias de cada tipo de retraso.

        El primer gráfico muestra la distribución del tiempo total de retraso atribuido a cada categoría, proporcionando una visión de los tipos de retraso que tienen un mayor impacto en términos de tiempo perdido.

        El segundo gráfico refleja la frecuencia con la que ocurre cada tipo de retraso, ofreciendo insights sobre cuáles son más comunes, independientemente de la duración del tiempo de retraso asociado.
    """)
        
        graficar_analisis_retrasos_aereos(df_todos)

        st.markdown("---")


