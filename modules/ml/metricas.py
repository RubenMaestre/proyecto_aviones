import streamlit as st
import json
import pandas as pd

def mostrar_metricas():
    st.markdown("### Métricas del modelo de clasificación")

    # Botón para mostrar métricas
    if st.button('Ver métricas modelo DecisionTreeClassifier de scikit-learn'):
        # Cargar métricas
        with open('data/model_metrics.json', 'r') as f:
            metrics = json.load(f)

        # Diccionario con descripciones de las métricas
        descriptions = {
            "jaccard_index": "Medida de la similitud entre los conjuntos de predicciones y las etiquetas verdaderas.",
            "accuracy": "Proporción de predicciones correctas sobre el total.",
            "precision": "Proporción de predicciones positivas correctas respecto al total de predicciones positivas.",
            "recall": "Capacidad del modelo para encontrar todas las instancias positivas relevantes.",
            "f1_score": "Media armónica de la precisión y el recall.",
            "roc_auc": "Mide la habilidad del modelo para discriminar entre clases.",
            "confusion_matrix": "Tabla que describe el rendimiento del modelo de clasificación.",
            "confusion_matrix_percent": "Porcentajes sobre el total de casos en cada fila de la matriz de confusión.",
            "specificity": "Capacidad del modelo de identificar correctamente los negativos verdaderos."
        }

        datos = [(key.replace('_', ' ').title(), metrics.get(key, "No disponible"), descriptions[key]) for key in descriptions.keys()]

        # Estilo CSS para los cuadros
        st.markdown("""
            <style>
                .metric-box {
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                    text-align: center;
                }
            </style>
        """, unsafe_allow_html=True)

        # Mostrar los datos en cuadros organizados en 2 columnas y 5 filas
        for i in range(0, len(datos), 2):
            cols = st.columns(2)
            with cols[0]:
                titulo, valor, descripcion = datos[i]
                st.markdown(f"<div class='metric-box'><h6>{titulo}</h6><p>{valor}</p><p><small>{descripcion}</small></p></div>", unsafe_allow_html=True)
            if i + 1 < len(datos):
                with cols[1]:
                    titulo, valor, descripcion = datos[i+1]
                    st.markdown(f"<div class='metric-box'><h6>{titulo}</h6><p>{valor}</p><p><small>{descripcion}</small></p></div>", unsafe_allow_html=True)
        
        st.markdown("---")
        # Mostrar classification_report al final
        report = metrics.get('classification_report', "No disponible")
        st.markdown("### Reporte de clasificación")
        st.text(report)

# Llamar a la función en alguna parte del código principal
mostrar_metricas()

