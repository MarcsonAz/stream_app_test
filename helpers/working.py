import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título do aplicativo
st.title("Visualizador de Dados Interativo")

# Carregar o arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = helper.carregar_dados(uploaded_file.name)
    
    st.text('Tabela Completa')
    
    st.dataframe(df)

if uploaded_file is not None:
    # Criar uma lista com os nomes das colunas
    column_list = df.columns.tolist()

    # Criar caixas de seleção para cada coluna
    selected_columns = st.multiselect('Selecione as colunas', column_list)

    # Função para filtrar o DataFrame
    def filter_dataframe(df, selected_columns):
        return df[selected_columns]

    # Filtrar o DataFrame com base nas colunas selecionadas
    filtered_df = filter_dataframe(df, selected_columns)

    # Criar a figura do Plotly
    fig = go.Figure(data=go.Table(
        header=dict(values=list(filtered_df.columns),
                fill_color='paleturquoise',
                align='left'),
        cells=dict(values=[filtered_df[col] for col in filtered_df.columns],
                fill_color='white',
                align='left')))

    # Adicionar interatividade (opcional)
    fig.update_layout(
        autosize=False,
        width=1500,
        height=500,
        margin=dict(l=50, r=50, b=70, t=0))

    # Exibir a tabela no Streamlit
    st.plotly_chart(fig)



##
##
##
##
##

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
    
    st.text('Tabela Completa')
    
    st.dataframe(df)
    
