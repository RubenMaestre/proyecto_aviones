import streamlit as st
import json
import pandas as pd

def mostrar_metricas():
    # Cargar métricas
    with open('data/model_metrics.json', 'r') as f:
        metrics = json.load(f)
    
    # Imprimir las métricas cargadas para depuración
    print("Métricas cargadas:", metrics)

    # Diccionario con descripciones de las métricas
    descriptions = {
        "jaccard_index": "Medida de la similitud entre los conjuntos de predicciones y las etiquetas verdaderas. Varía de 0 a 1, donde 1 es la mejor puntuación.",
        "accuracy": "Proporción de predicciones correctas sobre el total. Es una medida general de cómo el modelo predice correctamente.",
        "precision": "Proporción de predicciones positivas correctas respecto al total de predicciones positivas hechas.",
        "recall": "Capacidad del modelo para encontrar todas las instancias positivas relevantes.",
        "f1_score": "Media armónica de la precisión y el recall. Combina ambos en una sola métrica.",
        "roc_auc": "Mide la habilidad del modelo para discriminar entre clases. Un área de 1 representa un modelo perfecto.",
        "confusion_matrix": "Tabla que describe el rendimiento del modelo de clasificación.",
        "confusion_matrix_percent": "Similar a la matriz de confusión, pero mostrando los porcentajes sobre el total de casos en cada fila.",
        "specificity": "Capacidad del modelo de identificar correctamente los negativos verdaderos.",
        "classification_report": "Resumen de la precisión, recall y F1-score para cada clase."
}


    # Crear DataFrame para las métricas
    data = []
    for key, desc in descriptions.items():
        value = metrics.get(key, "No disponible")  # Obtener el valor de cada métrica del JSON
        data.append({"Métrica": key, "Valor": value, "Descripción": desc})

    df_metrics = pd.DataFrame(data)

    # Botón para mostrar métricas
    if st.button('VER MÉTRICAS DEL MODELO'):
        st.subheader("Métricas del Modelo")
        st.table(df_metrics)

