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
from modules.graph.k_top_aeropuertos_sin_retrasos import graficar_top_aeropuertos_con_sin_retrasos
from modules.graph.l_numero_vuelos_dias_diciembre import graficar_numero_vuelos_dias_diciembre
from modules.graph.m_numero_vuelos_acumulados_diciembre import graficar_numero_vuelos_acumulados_diciembre
from modules.graph.n_cantidad_llegadas_salidas_hora import graficar_cantidad_llegadas_salidas_por_hora
from modules.graph.o_cantidad_retrasos_hora import graficar_cantidad_retrasos_por_hora
from modules.graph.p_dias_semana_con_sin_retrasos import graficar_dias_semana_con_sin_retrasos
from modules.graph.q_total_minutos_tipo_retraso import graficar_total_minutos_por_tipo_retraso
from modules.graph.r_analisis_retrasos_aereos import graficar_analisis_retrasos_aereos
from modules.graph.s_top_estados_mas_retrasos import graficar_estados_mas_retrasos
from modules.graph.t_top_menos_retrasos import graficar_estados_menos_retrasos
from modules.graph.u_diagrama_distancia_millas import graficar_diagrama_distancia_millas
from modules.graph.v_histograma_distancias_millas import graficar_histograma_distancias_millas
from modules.graph.w_relacion_retrasos_millas import graficar_relacion_retrasos_millas
from modules.graph.x_numero_retrasos_intervalo import graficar_retrasos_por_intervalo
from modules.graph.y_costo_aerolinea import graficar_vuelos_por_costo_aerolinea
from modules.graph.yy_aerolinea_costo_retrasos import graficar_vuelos_retrasos_por_costo_aerolinea

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
            "Vuelos por aerolínea": graficar_vuelos_por_aerolinea,
            "Tipo de aerolínea": graficar_vuelos_por_costo_aerolinea
        }
    else:
        aerolineas_category = {
            "Vuelos por aerolínea": graficar_vuelos_por_aerolinea,
            "Tipo de aerolínea": graficar_vuelos_por_costo_aerolinea
        }
    common_categories["Aerolíneas"] = aerolineas_category

    # Categoría de Horarios
    horarios_category = {}
    if year == "Todos los años":
        horarios_category["Diagrama de salidas y llegadas"] = graficar_horas_vuelos
    horarios_category["Cantidad de llegadas y salidas por hora"] = graficar_cantidad_llegadas_salidas_por_hora
    common_categories["Horarios"] = horarios_category

    # Categoría de Correlaciones, solo para 'Todos los años'
    if year == "Todos los años":
        correlaciones_category = {
            "Mapa de calor de correlación": graficar_mapa_calor_correlacion,
            "Correlaciones específicas significativas": mostrar_correlaciones_significativas,
            "Correlación lineal": graficar_correlacion_lineal
        }
        common_categories["Correlaciones"] = correlaciones_category

    # Categoría de Puntualidad
    puntualidad_category = {
        "Retrasos mayores a 15 minutos": graficar_retrasos_mas_15,
        "Retrasos mayores a 15 minutos en días festivos": graficar_retrasos_mas_15_festivos,
        "Top aerolíneas con y sin retrasos": graficar_top_aerolineas_con_sin_retrasos,
        "Top aeropuertos con y sin retrasos": graficar_top_aeropuertos_con_sin_retrasos
    }
    common_categories["Puntualidad"] = puntualidad_category

    # Categoría de Vuelos, solo para 'Todos los años'
    if year == "Todos los años":
        vuelos_category = {
            "Número de vuelos por días en diciembre": graficar_numero_vuelos_dias_diciembre,
            "Número de vuelos acumulados por días en diciembre": graficar_numero_vuelos_acumulados_diciembre
        }
        common_categories["Vuelos"] = vuelos_category

    retrasos_category = {
        "Cantidad de retrasos por hora": graficar_cantidad_retrasos_por_hora,
        "Días de la semana con y sin retrasos": graficar_dias_semana_con_sin_retrasos,
        "Total de minutos por tipo de retraso": graficar_total_minutos_por_tipo_retraso,
        "Análisis de retrasos aéreos": graficar_analisis_retrasos_aereos,
        "Número de Retrasos por Intervalo (Hasta 200 Minutos)": graficar_retrasos_por_intervalo,
        "Tipo de aerolínea con y sin retraso": graficar_vuelos_retrasos_por_costo_aerolinea
    }
    common_categories["Retrasos"] = retrasos_category

    estados_category = {
        "Top estados con más retrasos": graficar_estados_mas_retrasos,
        "Top estados con menos retrasos": graficar_estados_menos_retrasos
    }
    common_categories["Estados"] = estados_category

    if year == "Todos los años":
        millas_analisis_category = {
            "Diagrama de distancia en millas": graficar_diagrama_distancia_millas,
            "Histograma de distancias en millas": graficar_histograma_distancias_millas,
            "Relación entre retrasos y millas": graficar_relacion_retrasos_millas
            }
        common_categories["Millas Análisis"] = millas_analisis_category

    return common_categories
