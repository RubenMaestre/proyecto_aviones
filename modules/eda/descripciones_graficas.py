# modules/eda/descripciones_graficas.py
import pandas as pd

def cargar_descripciones():
    try:
        df_descripciones = pd.read_parquet('data/graficas/descripciones.parquet')
        return df_descripciones
    except Exception as e:
        print(f"Error al cargar las descripciones: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío si hay error

def obtener_descripcion(year, nombre_grafica, df_descripciones):
    """Busca y retorna la descripción para una gráfica específica dada por año y nombre."""
    try:
        print(f"Buscando descripción para el año: {year}, gráfica: {nombre_grafica}")  # Diagnóstico
        descripcion = df_descripciones[
            (df_descripciones['year'].astype(str) == str(year)) & (df_descripciones['nombre'] == nombre_grafica)
        ]['descripcion'].values

        if descripcion.size > 0:
            print("Descripción encontrada:", descripcion[0])  # Diagnóstico
            return descripcion[0]
        else:
            print("Descripción no encontrada.")  # Diagnóstico
            return "Descripción no disponible."
    except Exception as e:
        print(f"Error al obtener la descripción: {e}")
        return "Descripción no disponible."
