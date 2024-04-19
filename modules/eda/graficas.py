# modules/eda/graficas.py

# Importar funciones de visualización
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

graficas_por_nombre = {
    "Vuelos totales por año": graficar_vuelos_totales_por_year,
    "Evolución de vuelos por aerolínea": graficar_evolucion_vuelos_por_aerolinea,
    "Vuelos por aerolínea": graficar_vuelos_por_aerolinea,
    "Diagrama de salidas y llegadas": graficar_horas_vuelos,
    "Mapa de calor de correlación": graficar_mapa_calor_correlacion,
    "Correlaciones específicas significativas": mostrar_correlaciones_significativas,
    "Correlación lineal entre retrasos": graficar_correlacion_lineal,
    "Retrasos mayores a 15 minutos": graficar_retrasos_mas_15,
    "Retrasos mayores a 15 minutos en festivos": graficar_retrasos_mas_15_festivos,
    "Top aerolíneas con y sin retrasos": graficar_top_aerolineas_con_sin_retrasos,
    "Top aeropuertos con y sin retrasos": graficar_top_aeropuertos_con_sin_retrasos,
    "Número de vuelos por días en diciembre": graficar_numero_vuelos_dias_diciembre,
    "Número de vuelos acumulados en diciembre": graficar_numero_vuelos_acumulados_diciembre,
    "Cantidad de llegadas y salidas por hora": graficar_cantidad_llegadas_salidas_por_hora,
    "Cantidad de retrasos por hora": graficar_cantidad_retrasos_por_hora,
    "Días de la semana con y sin retrasos": graficar_dias_semana_con_sin_retrasos,
    "Total de minutos por tipo de retraso": graficar_total_minutos_por_tipo_retraso,
    "Análisis de retrasos aéreos": graficar_analisis_retrasos_aereos,
    "Estados con más retrasos": graficar_estados_mas_retrasos,
    "Estados con menos retrasos": graficar_estados_menos_retrasos,
    "Diagrama de distancia en millas": graficar_diagrama_distancia_millas,
    "Histograma de distancias en millas": graficar_histograma_distancias_millas,
    "Relación entre retrasos y millas": graficar_relacion_retrasos_millas,
    "Número de retrasos por intervalo": graficar_retrasos_por_intervalo,
    "Vuelos por costo de aerolínea": graficar_vuelos_por_costo_aerolinea,
    "Retrasos y costos de aerolíneas": graficar_vuelos_retrasos_por_costo_aerolinea
}
