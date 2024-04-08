import pandas as pd
import os

def unir_pickles(carpeta_pickles='data/pickles/', num_partes=10, nombre_base='vuelos_limpio_parte_', extension='.pkl'):
    df_total = pd.DataFrame()

    for i in range(num_partes):
        nombre_archivo = f"{carpeta_pickles}{nombre_base}{i+1}{extension}"
        if os.path.exists(nombre_archivo):
            df_parte = pd.read_pickle(nombre_archivo)
            df_total = pd.concat([df_total, df_parte], ignore_index=True)
            yield df_total  # Rinde el DataFrame acumulado hasta el momento
        else:
            print(f"Advertencia: El archivo {nombre_archivo} no existe y será omitido.")

# No ejecutes la función aquí; será llamada desde el botón en la app de Streamlit.
