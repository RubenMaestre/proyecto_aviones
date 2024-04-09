import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_dias_semana_con_sin_retrasos(df):
    df_modif = df.copy()
    df_modif["retraso"] = df_modif["retraso_llegada"].apply(lambda x: 1 if x > 15 else 0)
    df_modif["fecha"] = pd.to_datetime(df_modif["fecha"])
    df_modif["dia_semana"] = df_modif["fecha"].dt.dayofweek

    retrasos_por_dia = df_modif.groupby(["dia_semana", "retraso"])["retraso"].count().unstack(fill_value=0)
    retrasos_por_dia.reset_index(inplace=True)
    retrasos_por_dia.columns = ["Dia de la semana", "Sin retraso", "Con retraso"]

    fig = px.bar(retrasos_por_dia, 
                x="Dia de la semana", 
                y=["Sin retraso", "Con retraso"],
                barmode="stack", 
                labels={"value": "Cantidad de vuelos", "Dia de la semana": "Día de la semana"})

    fig.update_layout(
        title="Cantidad de vuelos con y sin retraso por día de la semana",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(7)),
            ticktext=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        ),
        title_x=0.5,
        width=1080
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
