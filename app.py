import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle

with open('GPA.pickle', 'rb') as m:
    modelo = pickle.load(m)
df = pd.read_csv('colGPA_data.csv')
st.title('Modelo de Predicción Promedio Universidad')

tab1,tab2,tab3 = st.tabs(['TAB 1','TAB 2','TAB 3'])

with tab1:


    frec_male = df["Male"].value_counts().reset_index()
    colores_male = ["#636EFA", "#19D3F3"]

    colores_male = ["#BCC4DB", "#CA054D"]
    colores_hist = ["#0B3C49"]  # Un color rojo/naranja para los histogramas
    colores_hist2 = ["#7880B5"]  # Un color verde para variar
    colores_hist3 = ["#6BBAEC"]  # Otro color para el tercero

    fig1 = px.histogram(df, x='College GPA', title='College GPA', color_discrete_sequence=colores_hist)
    fig1.update_traces(marker_line_color='white', marker_line_width=1)
    fig2 = px.histogram(df, x='High School GPA', title='High School GPA', color_discrete_sequence=colores_hist2)
    fig2.update_traces(marker_line_color='white', marker_line_width=1)
    fig3 = px.histogram(df, x='Achievement Score', title='Achievement Score', color_discrete_sequence=colores_hist3)
    fig3.update_traces(marker_line_color='white', marker_line_width=1)
    fig4 = px.bar(frec_male, x="Male", y="count", title="Gender", color="Male", color_discrete_sequence=colores_male)
    fig4.update_traces(marker_line_color='black', marker_line_width=1)

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
  

with tab2:

    fig = make_subplots(rows=2,cols=2,
    subplot_titles=("High School VS ColGPA",
    'ACT VS ColGPA', "Male VS ColGPA"))

    color1 = "#00A7E1"  
    color2 = "#00171F"  
    color3 = "#003459" 

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=("High School VS ColGPA", "ACT VS ColGPA", "Male VS ColGPA")
    )

    # Scatter 1
    fig.add_trace(
        go.Scatter(
            x=df["High School GPA"],
            y=df["College GPA"],
            mode='markers',
            name="High School VS ColGPA",
            marker=dict(color=color1)
        ),
        row=1, col=1
    )

    # Scatter 2
    fig.add_trace(
        go.Scatter(
            x=df["Achievement Score"],
            y=df["College GPA"],
            mode='markers',
            name="ACT VS ColGPA",
            marker=dict(color=color2)
        ),
        row=1, col=2
    )

    # Box plot
    fig.add_trace(
        go.Box(
            x=df["Male"],
            y=df["College GPA"],
            name="Gender VS ColGPA",
            marker_color=color3
        ),
        row=2, col=1
    )

    fig.update_layout(height=700, width=900, title_text="Comparative GPA Analysis")

    st.plotly_chart(fig)

with tab3:
    hsGPA = st.slider('hsGPA',0.0,4.0)
    ACT = st.slider('ACT',1,36)
    sexo = st.selectbox('Gender',['Male','Female'])
    if sexo == 'Female':
        sexo = 0
    else:
        sexo = 1
    if st.button('PREDICCIÓN'):
        pred = modelo.predict(np.array([[hsGPA, ACT, sexo]]))
        st.write(pred[0])