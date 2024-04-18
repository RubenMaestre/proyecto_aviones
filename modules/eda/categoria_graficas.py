import streamlit as st
from modules.graph.a_vuelos_totales_por_year import graficar_vuelos_totales_por_year
from modules.graph.b_evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea

#from modules.graph.diagrama_salidas_llegadas import graficar_horas_vuelos
#from modules.graph.correlacion_variables import graficar_correlacion_variables
#from modules.graph.correlacion_lineal import graficar_correlacion_lineal
#from modules.graph.retrasos_mas_15 import graficar_retrasos_mas_15
#from modules.graph.retrasos_mas_15_festivos import graficar_retrasos_mas_15_festivos
#from modules.graph.cantidad_llegadas_salidas_hora import graficar_cantidad_llegadas_salidas_por_hora
#from modules.graph.cantidad_retrasos_hora import graficar_cantidad_retrasos_por_hora
#from modules.graph.dias_semana_con_sin_retrasos import graficar_dias_semana_con_sin_retrasos
#from modules.graph.total_minutos_tipo_retraso import graficar_total_minutos_por_tipo_retraso
#from modules.graph.analisis_retrasos_aereos import graficar_analisis_retrasos_aereos
#from modules.graph.diagrama_distancia_millas import graficar_diagrama_distancia_millas
#from modules.graph.histograma_distancias_millas import graficar_histograma_distancias_millas
#from modules.graph.relacion_retrasos_millas import graficar_relacion_retrasos_millas
#from modules.graph.maxima_distancia_millas import graficar_maxima_distancia_millas

import streamlit as st
from modules.graph.a_vuelos_totales_por_year import graficar_vuelos_totales_por_year
from modules.graph.b_evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea

def get_graficas_por_categoria():
    year = st.session_state.get('selected_year', 'Todos los años')  # Obtén el año seleccionado

    # Categorías y gráficas comunes a todos los años específicos
    common_categories = {
        "Aerolíneas": {}
    }

    # Añadir gráficas específicas para "Todos los años"
    if year == "Todos los años":
        common_categories["Aerolíneas"].update({
            "Vuelos totales por año": graficar_vuelos_totales_por_year,
            "Evolución del número de vuelos por compañía aérea": graficar_evolucion_vuelos_por_aerolinea,
            "Vuelos por aerolínea": graficar_vuelos_por_aerolinea
        })
    else:
        common_categories["Aerolíneas"].update({
            "Evolución del número de vuelos por compañía aérea": graficar_evolucion_vuelos_por_aerolinea
        })

    return common_categories

