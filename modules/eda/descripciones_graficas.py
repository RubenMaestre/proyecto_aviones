# modules/eda/descripciones_graficas.py
import pandas as pd

def cargar_descripciones():
    """Carga las descripciones de las gráficas desde un archivo Excel."""
    try:
        df_descripciones = pd.read_excel('ruta/a/tu/archivo.xlsx')
        return df_descripciones
    except Exception as e:
        print(f"Error al cargar las descripciones: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío si hay error

def obtener_descripcion(año, nombre_grafica, df_descripciones):
    """Busca y retorna la descripción para una gráfica específica dada por año y nombre."""
    descripcion = df_descripciones[
        (df_descripciones['Año'] == año) & (df_descripciones['Nombre'] == nombre_grafica)
    ]['Descripción'].values

    if descripcion.size > 0:
        return descripcion[0]
    else:
        return "Descripción no disponible."