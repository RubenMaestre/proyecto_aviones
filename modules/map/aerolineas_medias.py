import pandas as pd
import streamlit as st

def muestra_aerolineas_medias():
    st.markdown("### Datos curiosos de las aerolíneas de Estados Unidos que debes saber")

    # Cargar los datos de aerolíneas
    df_aerolineas_unicas = pd.read_pickle('data/aerolineas_unicos.pkl')

    # Limpiar y preparar los datos
    df_aerolineas_unicas['founded'] = pd.to_numeric(df_aerolineas_unicas['founded'], errors='coerce')
    df_aerolineas_unicas['started_operations'] = pd.to_numeric(df_aerolineas_unicas['started_operations'], errors='coerce')
    df_aerolineas_unicas['fleet_size'] = pd.to_numeric(df_aerolineas_unicas['fleet_size'], errors='coerce')
    df_aerolineas_unicas['average_fleet_Age'] = pd.to_numeric(df_aerolineas_unicas['average_fleet_Age'], errors='coerce')

    # Encuentra la compañía más antigua
    df_aerolineas_unicas['oldest'] = df_aerolineas_unicas[['founded', 'started_operations']].min(axis=1)
    oldest_company = df_aerolineas_unicas.loc[df_aerolineas_unicas['oldest'].idxmin()]['aerolinea']

    # Encuentra la aerolínea con el mayor/menor fleet_size y average_fleet_Age
    largest_fleet = df_aerolineas_unicas.loc[df_aerolineas_unicas['fleet_size'].idxmax()]['aerolinea']
    smallest_fleet = df_aerolineas_unicas.loc[df_aerolineas_unicas['fleet_size'].idxmin()]['aerolinea']
    oldest_fleet = df_aerolineas_unicas.loc[df_aerolineas_unicas['average_fleet_Age'].idxmax()]['aerolinea']
    youngest_fleet = df_aerolineas_unicas.loc[df_aerolineas_unicas['average_fleet_Age'].idxmin()]['aerolinea']

    # Calcula la media de fleet_size y average_fleet_Age
    mean_fleet_size = df_aerolineas_unicas['fleet_size'].mean()
    mean_fleet_age = df_aerolineas_unicas['average_fleet_Age'].mean()

    # Calcula el número de compañías por rango de tamaño de flota
    small_fleets = df_aerolineas_unicas[df_aerolineas_unicas['fleet_size'] < 150].shape[0]
    medium_fleets = df_aerolineas_unicas[(df_aerolineas_unicas['fleet_size'] >= 150) & (df_aerolineas_unicas['fleet_size'] <= 500)].shape[0]
    large_fleets = df_aerolineas_unicas[df_aerolineas_unicas['fleet_size'] > 500].shape[0]

    # Mostrar los resultados
    st.write(f"La compañía aérea más antigua es: {oldest_company}")
    st.write(f"La aerolínea con la flota más grande es: {largest_fleet}")
    st.write(f"La aerolínea con la flota más pequeña es: {smallest_fleet}")
    st.write(f"La aerolínea con la flota de mayor edad es: {oldest_fleet}")
    st.write(f"La aerolínea con la flota más joven es: {youngest_fleet}")
    st.write(f"La media del tamaño de la flota es: {mean_fleet_size:.2f} aviones")
    st.write(f"La edad media de la flota es: {mean_fleet_age:.2f} años")
    st.write(f"{small_fleets} compañías tienen menos de 150 aviones")
    st.write(f"{medium_fleets} compañías tienen entre 150 y 500 aviones")
    st.write(f"{large_fleets} compañías tienen más de 500 aviones")
