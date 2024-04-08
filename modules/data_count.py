import pandas as pd

def cargar_y_contar_datos():
    # Ajusta las rutas de los archivos según donde tengas guardados los pickles
    ruta_aerolineas = 'data/aerolineas_unicos.pkl'
    ruta_aeropuertos = 'data/aeropuertos_unicos.pkl'

    # Cargar los DataFrames desde los archivos pickle
    aerolineas_df = pd.read_pickle(ruta_aerolineas)
    aeropuertos_df = pd.read_pickle(ruta_aeropuertos)

    # Calcular los datos requeridos
    numero_total_estados = aeropuertos_df['estado'].nunique()
    numero_total_ciudades = aeropuertos_df['ciudad'].nunique()
    numero_total_aeropuertos = aeropuertos_df['nombre_aeropuerto'].nunique()
    numero_total_aerolineas = aerolineas_df['aerolinea'].nunique()

    return numero_total_estados, numero_total_ciudades, numero_total_aeropuertos, numero_total_aerolineas
