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

# Verificar e alterar o tipo de uma coluna
imprime_jogo_da_velha()
print(data_frame.dtypes)
data_frame['LojaID'] = data_frame['LojaID'].astype('object')
print(data_frame.dtypes)

# Somando números nulos
imprime_jogo_da_velha()
print(data_frame.isnull().sum())

# Alguns comandos para utilizar em valores nulos
imprime_jogo_da_velha()
# data_frame['Vendas'].fillna(data_frame['Vendas'].mean(), implace=True) - Substitui o valor nulo pela média
# data_frame['Vendas'].fillna(0, implace=True) - Substitui o valor nulo por zero
# data_frame.dropna(implace=True) - Apagando linhas com valor nulos
# data_frame.dropna(subset=['Vendas'], implace=True) - Apagando linhas com valor nulos com base apenas em 1 coluna
# data_frame.dropna(how='all', implace=True) - Removendo linhas com valores faltantes em todas as colunas

# Comando para criar uma nova coluna 
imprime_jogo_da_velha()
data_frame['Receita'] = data_frame['Vendas'].mul(data_frame['Qtde'])
print(data_frame.head())

# Retornando valor máximos e minimos
imprime_jogo_da_velha()
print(data_frame['Receita'].max())
print(data_frame['Receita'].min())

# Retornando as 3 melhores e piores receitas
imprime_jogo_da_velha()
print(data_frame.nlargest(3, 'Receita'))
print(data_frame.nsmallest(3, 'Receita'))

# Soma a receita agrupando por cidade
imprime_jogo_da_velha()
print(data_frame.groupby('Cidade')['Receita'].sum())

# Ordenando por receita
imprime_jogo_da_velha()
print(data_frame.sort_values('Receita', ascending=False).head(10))

# Comando para pegar uma amostra do conjunto
imprime_jogo_da_velha()
print(data_frame.sample(5))

imprime_jogo_da_velha()
print(data_frame.head())

imprime_jogo_da_velha()
print(data_frame.tail())