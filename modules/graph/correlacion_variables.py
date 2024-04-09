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
        y=columnas_numericas,
        color_continuous_scale='RdYlBu_r'  # Cambiar la paleta de colores a rojos y azules (invertida)
    )

    fig.update_layout(
        title_x=0.5,
        width=1080,
        height=800
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

    # Calcular y mostrar la correlación específica entre retraso de salida y llegada
    corr_salida_llegada = df["retraso_salida"].corr(df["retraso_llegada"])
    st.markdown(f"**Nota:** Hay una relación positiva moderadamente fuerte entre el retraso de salida y el retraso de llegada, con un coeficiente de correlación de {corr_salida_llegada:.2f}. Esto sugiere que cuando un vuelo se retrasa en la salida, tiende a experimentar un retraso similar en la llegada.")
