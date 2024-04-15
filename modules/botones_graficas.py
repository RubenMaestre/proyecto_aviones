import streamlit as st
from modules.graph.vuelos_total_aerolineas import graficar_vuelos_por_aerolinea
from modules.graph.evolucion_vuelos_aerolineas import graficar_evolucion_vuelos_por_aerolinea
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
from modules.graph.diagrama_distancia_millas import graficar_diagrama_distancia_millas
from modules.graph.histograma_distancias_millas import graficar_histograma_distancias_millas
from modules.graph.relacion_retrasos_millas import graficar_relacion_retrasos_millas
from modules.graph.maxima_distancia_millas import graficar_maxima_distancia_millas


def seleccionar_grafica():
    graficas_disponibles = {
        "Vuelos por aerolínea": graficar_vuelos_por_aerolinea,
        "Evolución de vuelos por aerolínea": graficar_evolucion_vuelos_por_aerolinea,
        "Diagrama de salidas y llegadas": graficar_horas_vuelos,
        "Correlación de variables": graficar_correlacion_variables,
        "Correlación lineal": graficar_correlacion_lineal,
        "Retrasos mayores a 15 minutos": graficar_retrasos_mas_15,
        "Retrasos mayores a 15 minutos en días festivos": graficar_retrasos_mas_15_festivos,
        "Cantidad de llegadas y salidas por hora": graficar_cantidad_llegadas_salidas_por_hora,
        "Cantidad de retrasos por hora": graficar_cantidad_retrasos_por_hora,
        "Días de la semana con y sin retrasos": graficar_dias_semana_con_sin_retrasos,
        "Total de minutos por tipo de retraso": graficar_total_minutos_por_tipo_retraso,
        "Análisis de retrasos aéreos": graficar_analisis_retrasos_aereos,
        "Diagrama de distancias en millas": graficar_diagrama_distancia_millas,
        "Histograma de distancias en millas": graficar_histograma_distancias_millas,
        "Relación entre retrasos y millas": graficar_relacion_retrasos_millas,
        "Distancia máxima en millas": graficar_maxima_distancia_millas
    }
    grafica_seleccionada = st.selectbox("Selecciona una gráfica para visualizar:", list(graficas_disponibles.keys()))
    return graficas_disponibles[grafica_seleccionada]


