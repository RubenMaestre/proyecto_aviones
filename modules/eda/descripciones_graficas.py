# modules/eda/descripciones_graficas.py
import pandas as pd

def obtener_descripcion(año, nombre_grafica, df_descripciones):
    """Busca y retorna la descripción para una gráfica específica dada por año y nombre."""
    try:
        print(f"Buscando descripción para el año: {año}, gráfica: {nombre_grafica}")  # Diagnóstico
        descripcion = df_descripciones[
            (df_descripciones['Año'] == año) & (df_descripciones['Nombre'] == nombre_grafica)
        ]['Descripción'].values

        if descripcion.size > 0:
            print("Descripción encontrada:", descripcion[0])  # Diagnóstico
            return descripcion[0]
        else:
            print("Descripción no encontrada.")  # Diagnóstico
            return "Descripción no disponible."
    except Exception as e:
        print(f"Error al obtener la descripción: {e}")
        return "Descripción no disponible."