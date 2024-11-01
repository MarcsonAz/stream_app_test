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

st.divider()

if uploaded_file is not None:
    df = helper.carregar_dados(uploaded_file.name)
    # Criar uma lista com os nomes das colunas
    column_list = df.columns.tolist()

   # Criar caixas de seleção para coluna, valor e operador
    col1, col2, col3 = st.columns(3)
    
    #home_value = col1.number_input("Home Value", min_value=0, value=500000)
    
    selected_column = col1.selectbox('Selecione a coluna', df.columns)
    
    if selected_column in ["nome_candidato"]:
        st.write("O nome do candidato é sensível a letra maiúscula e minúscula, olhe a tabela acima!")
    
    value = col2.text_input('Digite o valor')
    if selected_column in ["NOTA FINAL","#","valor","ano"]:
        value = float(value)
        
        
    operator = col3.selectbox('Selecione o operador', ['==', '>', '<', '>=', '<=', '!=','Conter'])
    
    # Filtrar o DataFrame com base nas colunas selecionadas
    filtered_df = helper.filter_dataframe(df, selected_column, value, operator)

    st.divider()
    
    st.text('Tabela Filtrada')
    
    #st.dataframe(filtered_df)
    st.dataframe(
        filtered_df,
        column_config={
            "ano": st.column_config.NumberColumn("Ano",format="%d"),
            "valor": st.column_config.NumberColumn("Valor",format="%d")
            },
        hide_index=True,
    )
