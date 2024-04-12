# modules/ml/ml_1.py
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from modules.carga_todos_df import cargar_todos_df

# Importaciones de Scikit-learn y Imbalanced-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import jaccard_score, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline


def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def display_ml_page():
    st.title('Predicción de Retrasos de Vuelos')

    # Cargar modelo
    model = load_model('data/modelo_entrenado.pkl')

    # Cargar datos y asegurar transformación adecuada
    df = cargar_todos_df()

    ciudad_origen = st.selectbox('Selecciona la ciudad de origen:', options=df['ciudad_origen'].unique())
    aeropuertos_disponibles = df[df['ciudad_origen'] == ciudad_origen]['aeropuerto_origen'].unique()
    aeropuerto_origen = st.selectbox('Selecciona el aeropuerto de origen:', options=aeropuertos_disponibles)
    ciudad_destino = st.selectbox('Selecciona la ciudad destino:', options=df['ciudad_destino'].unique())
    aerolineas_disponibles = df[(df['ciudad_destino'] == ciudad_destino) & (df['ciudad_origen'] == ciudad_origen)]['aerolinea'].unique()
    aerolinea = st.selectbox('Selecciona la aerolínea:', options=aerolineas_disponibles)

    if st.button('Predecir Retraso'):
        # Aquí necesitas asegurarte de que las entradas estén en el formato adecuado
        features = np.array([[ciudad_origen, aeropuerto_origen, ciudad_destino, aerolinea]])
        # Transformar las características aquí si es necesario antes de la predicción, por ejemplo con un encoder
        # Si usaste un encoder durante el entrenamiento, deberías cargarlo y usarlo aquí para transformar 'features'
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success('El vuelo probablemente llegará con retraso.')
        else:
            st.success('El vuelo probablemente llegará a tiempo.')