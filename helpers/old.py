import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import helpers.helper1 as helper

# Função para carregar os dados
def load_data(file):
    df = pd.read_excel(f"data/{file}")
    return df

# Título do aplicativo
st.title("Visualizador de Dados Interativo")

# Carregar o arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])


if uploaded_file is not None:
    df = helper.carregar_dados(uploaded_file.name)

    # Exibir opções de gráficos
    grafico = st.selectbox("Escolha um tipo de gráfico", ["Gráfico de Barras"])

    if grafico == "Gráfico de Barras":
        coluna_x = st.selectbox("Selecione a coluna para o eixo x", df.columns)
        coluna_y = st.selectbox("Selecione a coluna para o eixo y", df.columns)

        fig = helper.criar_grafico_de_barras(df, coluna_x, coluna_y)
        st.plotly_chart(fig)
    
    st.text('Tabela Completa')
    
    st.dataframe(df)
    
    fig = go.Figure(data=go.Table(header=dict(values=list(df.columns),
                                              #fill_color='paleturquoise',
                                              align='left'),
                                  cells=dict(values=[df[col] for col in df.columns],
                                             #fill_color='white',
                                             align='left')
                                  )
                    )

# Adicionar interatividade (opcional)
    fig.update_layout(
        autosize=False,
        width=1500,
        height=500,
        margin=dict(l=50, r=50, b=70, t=0))


    fig.update_layout(clickmode='event+select')

    # Callback para lidar com a seleção
    #@st.experimental_memo
    def filter_dataframe(df: pd.DataFrame, selected_rows: list):
        return df if selected_rows is None else df.loc[selected_rows]

    # Exibir a tabela no Streamlit
    selected_rows = st.plotly_chart(fig)
    filtered_df = filter_dataframe(df, selected_rows=None)