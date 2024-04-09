import streamlit as st
from modules.carga_todos_df import cargar_todos_df
from modules.datos_df_cargados import mostrar_estadisticas_df
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.correlacion_variables import graficar_correlacion_variables
from modules.graph.correlacion_lineal import graficar_correlacion_lineal
from modules.graph.retrasos_mas_15 import graficar_retrasos_mas_15


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
