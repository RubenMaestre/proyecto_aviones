import streamlit as st
from modules.graph.a_vuelos_totales_por_year import graficar_vuelos_totales_por_year
from modules.graph.b_evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.c_vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.d_diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.ee_mapa_calor import graficar_mapa_calor_correlacion
from modules.graph.f_correlaciones_especificas import mostrar_correlaciones_significativas

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


def get_graficas_por_categoria():
    year = st.session_state.get('selected_year', 'Todos los años')  # Usar el valor guardado

    # Categoría de Aerolíneas
    aerolineas_category = {}
    if year == "Todos los años":
        aerolineas_category = {
            "Vuelos totales por año": graficar_vuelos_totales_por_year,
            "Evolución del número de vuelos por compañía aérea": graficar_evolucion_vuelos_por_aerolinea,
            "Vuelos por aerolínea": graficar_vuelos_por_aerolinea
        }
    else:
        aerolineas_category = {
            "Vuelos por aerolínea": graficar_vuelos_por_aerolinea
        }

    # Categoría de Horarios
    horarios_category = {
        "Diagrama de salidas y llegadas": graficar_horas_vuelos
    }

    # Combinar todas las categorías en un solo diccionario
    common_categories = {
        "Aerolíneas": aerolineas_category,
        "Horarios": horarios_category
    }

    # Categoría de Correlaciones, solo para 'Todos los años'
    if year == "Todos los años":
        correlaciones_category = {
            "Mapa de calor de correlación": graficar_mapa_calor_correlacion,
            "Correlaciones específicas significativas": mostrar_correlaciones_significativas
        }
        common_categories["Correlaciones"] = correlaciones_category

    return common_categories