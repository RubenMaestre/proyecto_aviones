import streamlit as st
import plotly.express as px

def graficar_correlacion_variables(df):
    # Seleccionar solo las columnas numéricas para la correlación
    columnas_numericas = df.select_dtypes(include=['int64', 'int32', 'float64']).columns.tolist()

    # Calcular la matriz de correlación y redondearla a 1 decimal
    matriz_correlacion = df[columnas_numericas].corr().round(1)

    # Crear el mapa de calor usando Plotly
    fig = px.imshow(
        img=matriz_correlacion,
        text_auto=True,
        title="Correlaciones Lineales de las Variables Numéricas",
        labels=dict(x="Variables", y="Variables", color="Correlación"),
        x=columnas_numericas,
        y=columnas_numericas
    )

    fig.update_layout(
        title_x=0.5,
        width=1080,
        height=800
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
