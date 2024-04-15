import pandas as pd
import streamlit as st

def muestra_aerolineas_medias():
    st.markdown("### Datos curiosos de las aerolíneas de Estados Unidos que debes saber")

    # Cargar los datos de aerolíneas
    df_aerolineas_unicas = pd.read_pickle('data/aerolineas_unicos.pkl')

    # Preparación de los datos
    df_aerolineas_unicas['founded'] = pd.to_numeric(df_aerolineas_unicas['founded'], errors='coerce')
    df_aerolineas_unicas['started_operations'] = pd.to_numeric(df_aerolineas_unicas['started_operations'], errors='coerce')
    df_aerolineas_unicas['fleet_size'] = pd.to_numeric(df_aerolineas_unicas['fleet_size'], errors='coerce')
    df_aerolineas_unicas['average_fleet_Age'] = pd.to_numeric(df_aerolineas_unicas['average_fleet_Age'], errors='coerce')

    # Cálculos
    df_aerolineas_unicas['oldest'] = df_aerolineas_unicas[['founded', 'started_operations']].min(axis=1)
    oldest_idx = df_aerolineas_unicas['oldest'].idxmin()
    largest_fleet_idx = df_aerolineas_unicas['fleet_size'].idxmax()
    smallest_fleet_idx = df_aerolineas_unicas['fleet_size'].idxmin()
    oldest_fleet_idx = df_aerolineas_unicas['average_fleet_Age'].idxmax()
    youngest_fleet_idx = df_aerolineas_unicas['average_fleet_Age'].idxmin()

    # Datos para la tabla
    datos = {
        'Dato': [
            'Compañía aérea más antigua',
            'Flota más grande',
            'Flota más pequeña',
            'Flota de mayor edad promedio',
            'Flota de menor edad promedio',
            'Media del tamaño de la flota',
            'Edad media de la flota',
            'Compañías con menos de 150 aviones',
            'Compañías con 150-500 aviones',
            'Compañías con más de 500 aviones'
        ],
        
        'Descripción': [
            f"{df_aerolineas_unicas.loc[oldest_idx, 'aerolinea']} (Fundada en {int(df_aerolineas_unicas.loc[oldest_idx, 'oldest'])})",
            f"{df_aerolineas_unicas.loc[largest_fleet_idx, 'aerolinea']} ({int(df_aerolineas_unicas.loc[largest_fleet_idx, 'fleet_size'])} aviones)",
            f"{df_aerolineas_unicas.loc[smallest_fleet_idx, 'aerolinea']} ({int(df_aerolineas_unicas.loc[smallest_fleet_idx, 'fleet_size'])} aviones)",
            f"{df_aerolineas_unicas.loc[oldest_fleet_idx, 'aerolinea']} ({df_aerolineas_unicas.loc[oldest_fleet_idx, 'average_fleet_Age']:.2f} años)",
            f"{df_aerolineas_unicas.loc[youngest_fleet_idx, 'aerolinea']} ({df_aerolineas_unicas.loc[youngest_fleet_idx, 'average_fleet_Age']:.2f} años)",
            f"{df_aerolineas_unicas['fleet_size'].mean():.2f}",
            f"{df_aerolineas_unicas['average_fleet_Age'].mean():.2f} años",
            f"{(df_aerolineas_unicas['fleet_size'] < 150).sum()} compañías " +
            f"({', '.join(df_aerolineas_unicas[df_aerolineas_unicas['fleet_size'] < 150]['aerolinea'].tolist())})",
            f"{((df_aerolineas_unicas['fleet_size'] >= 150) & (df_aerolineas_unicas['fleet_size'] <= 500)).sum()} compañías " +
            f"({', '.join(df_aerolineas_unicas[(df_aerolineas_unicas['fleet_size'] >= 150) & (df_aerolineas_unicas['fleet_size'] <= 500)]['aerolinea'].tolist())})",
            f"{(df_aerolineas_unicas['fleet_size'] > 500).sum()} compañías " +
            f"({', '.join(df_aerolineas_unicas[df_aerolineas_unicas['fleet_size'] > 500]['aerolinea'].tolist())})"
        ]
    }
    # Crear los cuadrados con la información
    for i in range(0, len(datos), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(datos):
                with cols[j]:
                    dato, descripcion = datos[i + j]
                    st.markdown(f"#### {dato}")
                    st.write(descripcion)
                    st.markdown("---")  # Agregar una línea horizontal para separar visualmente los bloques

# Llamar a la función fuera de su definición
muestra_aerolineas_medias()