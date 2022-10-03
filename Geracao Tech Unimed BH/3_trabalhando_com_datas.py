import pandas as pd

def imprime_jogo_da_velha():
    return print('###############')

data_frame_1 = pd.read_excel('../datasets/Aracaju.xlsx')
data_frame_2 = pd.read_excel('../datasets/Fortaleza.xlsx')
data_frame_3 = pd.read_excel('../datasets/Natal.xlsx')
data_frame_4 = pd.read_excel('../datasets/Recife.xlsx')
data_frame_5 = pd.read_excel('../datasets/Salvador.xlsx')

data_frame = pd.concat([
    data_frame_1, data_frame_2, data_frame_3, data_frame_4, data_frame_5
])

# Converte a coluna data para inteiro e no formato date
imprime_jogo_da_velha()
print(data_frame.dtypes)
data_frame['Data'] = data_frame['Data'].astype('int64')
print(data_frame.dtypes)
data_frame['Data'] = pd.to_datetime(data_frame['Data'])
print(data_frame.dtypes)

# Comando para criar uma nova coluna 
imprime_jogo_da_velha()
data_frame['Receita'] = data_frame['Vendas'].mul(data_frame['Qtde'])
print(data_frame.head())

# Descobrir a receita por Ano
imprime_jogo_da_velha()
print(data_frame.groupby(data_frame['Data'].dt.year)['Receita'].sum())

# Criar uma nova coluna de Ano
imprime_jogo_da_velha()
data_frame['Ano_Venda'] = data_frame['Data'].dt.year
print(data_frame.sample(5))

# Criar uma nova de mês e dia
imprime_jogo_da_velha()
data_frame['mes_venda'], data_frame['dia_venda'] = data_frame['Data'].dt.month, data_frame['Data'].dt.day
print(data_frame.sample(5))

# Retorna a data mais antiga
imprime_jogo_da_velha()
print(data_frame['Data'].min())

# Calcular a diferença de dias
imprime_jogo_da_velha()
data_frame['diferenca_dias'] = data_frame['Data'] - data_frame['Data'].min()
print(data_frame.sample(5))

# Calcular a diferença de dias
imprime_jogo_da_velha()
data_frame['trimestre_venda'] = data_frame['Data'].dt.quarter
print(data_frame.sample(5))

# Filtrando as vendas de 2019 do mês de março
imprime_jogo_da_velha()
vendas_marco_2019 = data_frame.loc[(data_frame['Data'].dt.year == 2019) & (data_frame['Data'].dt.month == 3)]
print(vendas_marco_2019)
