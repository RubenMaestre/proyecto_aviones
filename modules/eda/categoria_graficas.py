import streamlit as st
from modules.graph.a_vuelos_totales_por_year import graficar_vuelos_totales_por_year
from modules.graph.b_evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
from modules.graph.c_vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.d_diagrama_salidas_llegadas import graficar_horas_vuelos
from modules.graph.e_mapa_calor import graficar_mapa_calor_correlacion
from modules.graph.f_correlaciones_especificas import mostrar_correlaciones_significativas
from modules.graph.g_correlacion_lineal import graficar_correlacion_lineal
from modules.graph.h_retrasos_mas_15 import graficar_retrasos_mas_15
from modules.graph.i_retrasos_mas_15_festivos import graficar_retrasos_mas_15_festivos
from modules.graph.j_top_aerolineas_con_sin_retrasos import graficar_top_aerolineas_con_sin_retrasos

#from modules.graph.correlacion_variables import graficar_correlacion_variables

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

    # Inicializa common_categories al inicio para asegurar que está disponible en todos los flujos del código
    common_categories = {}

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
    common_categories["Aerolíneas"] = aerolineas_category

    # Categoría de Horarios
    horarios_category = {
        "Diagrama de salidas y llegadas": graficar_horas_vuelos
    }
    common_categories["Horarios"] = horarios_category

    # Categoría de Correlaciones, solo para 'Todos los años'
    if year == "Todos los años":
        correlaciones_category = {
            "Mapa de calor de correlación": graficar_mapa_calor_correlacion,
            "Correlaciones específicas significativas": mostrar_correlaciones_significativas,
            "Correlación lineal": graficar_correlacion_lineal
        }
        common_categories["Correlaciones"] = correlaciones_category

    # Nueva Categoría de Puntualidad
    puntualidad_category = {
        "Retrasos mayores a 15 minutos": graficar_retrasos_mas_15,
        "Retrasos mayores a 15 minutos en días festivos": graficar_retrasos_mas_15_festivos,
        "Top de aerolíneas sin retrasos": graficar_top_aerolineas_con_sin_retrasos
    }
    common_categories["Puntualidad"] = puntualidad_category

    return common_categories
