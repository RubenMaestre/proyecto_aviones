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
        # Asegurarse de que los tipos de datos son correctos para la comparación
        year = str(year)  # Convertir el año a string si es necesario
        df_descripciones['year'] = df_descripciones['year'].astype(str)

        descripcion = df_descripciones[
            (df_descripciones['year'] == year) & (df_descripciones['nombre'] == nombre_grafica)
        ]['descripcion'].values

        if descripcion.size > 0:
            print("Descripción encontrada:", descripcion[0])  # Diagnóstico
            return descripcion[0]
        else:
            print("Esta sección no contiene comentarios adicionales o está pendiente de comentar.")  # Diagnóstico
            return "Esta sección no contiene comentarios adicionales o está pendiente de comentar."
    except Exception as e:
        print(f"Error al obtener la descripción: {e}")
        return "Esta sección no contiene comentarios adicionales o está pendiente de comentar."

