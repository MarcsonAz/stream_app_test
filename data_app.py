import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import helpers.helper1 as helper

# Título do aplicativo
st.title("Visualizador de Dados Interativo")

# Carregar o arquivo
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = helper.carregar_dados(uploaded_file.name)
    
    st.text('Tabela Completa')
    
    st.dataframe(df)

if uploaded_file is not None:
    df = helper.carregar_dados(uploaded_file.name)
    # Criar uma lista com os nomes das colunas
    column_list = df.columns.tolist()

   # Criar caixas de seleção para coluna, valor e operador
    selected_column = st.selectbox('Selecione a coluna', df.columns)
    value = st.text_input('Digite o valor')
    if selected_column in ["NOTA FINAL","#"]:
        value = float(value)
    operator = st.selectbox('Selecione o operador', ['==', '>', '<', '>=', '<=', '!=','Conter'])
    
    # Filtrar o DataFrame com base nas colunas selecionadas
    filtered_df = helper.filter_dataframe(df, selected_column, value, operator)

    st.text('Tabela Filtrada')
    
    #st.dataframe(filtered_df)
    st.dataframe(
        filtered_df,
        column_config={
            "ano": "App name",
            "valor": st.column_config.NumberColumn(
                "Github Stars",
                format="%d",
                )
            },
        hide_index=True,
    )
