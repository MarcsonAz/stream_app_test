import pandas as pd

def carregar_dados(nome_arquivo):
    """Carrega os dados de um arquivo Excel.

    Args:
        nome_arquivo (str): Nome do arquivo Excel.

    Returns:
        pandas.DataFrame: DataFrame com os dados carregados.
    """

    df = pd.read_excel(f"data/{nome_arquivo}")
    
    column_list = df.columns.tolist()
    
    if "ano" in column_list:
        df["ano"] = pd.to_numeric(df["ano"])
    
    if "valor" in column_list:
        df["valor"] = pd.to_numeric(df["valor"])
        
    if "NOTA FINAL" in column_list:
        df["NOTA FINAL"] = pd.to_numeric(df["NOTA FINAL"], errors='coerce') 
    
    return df

def criar_grafico_de_barras(df, coluna_x, coluna_y):
    """Cria um gráfico de barras simples.

    Args:
        df (pandas.DataFrame): DataFrame com os dados.
        coluna_x (str): Nome da coluna para o eixo x.
        coluna_y (str): Nome da coluna para o eixo y.
    """

    import plotly.express as px

    fig = px.bar(df, x=coluna_x, y=coluna_y)
    return fig

def filter_dataframe(df, selected_column, value, operator='=='):
    """Filtra um DataFrame com base em uma coluna, um valor e um operador.

    Args:
        df (pd.DataFrame): DataFrame a ser filtrado.
        selected_column (str): Nome da coluna para filtrar.
        value: Valor a ser usado para filtrar.
        operator (str, optional): Operador de comparação. Defaults to '=='.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """

    if selected_column not in df.columns:
        raise ValueError(f"A coluna '{selected_column}' não existe no DataFrame.")

    if operator == '==':
        return df[df[selected_column] == value]
    elif operator == '>':
        return df[df[selected_column] > value]
    elif operator == '<':
        return df[df[selected_column] < value]
    elif operator == '>=':
        return df[df[selected_column] >= value]
    elif operator == '<=':
        return df[df[selected_column] <= value]
    elif operator == '!=':
        return df[df[selected_column] != value]
    elif operator == 'Conter':
        return df[df[selected_column].str.contains(value)]
    
    
    else:
        raise ValueError(f"Operador '{operator}' inválido.")