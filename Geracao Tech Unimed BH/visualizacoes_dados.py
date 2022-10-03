import pandas as pd
import matplotlib.pyplot as plt


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

# Quantidade vendas por ID
imprime_jogo_da_velha()
print(data_frame['LojaID'].value_counts(ascending=False))

# Comando para criar uma nova coluna 
imprime_jogo_da_velha()
data_frame['Receita'] = data_frame['Vendas'].mul(data_frame['Qtde'])
print(data_frame.head())

# Grafico impressos em tipos
imprime_jogo_da_velha()
# data_frame['LojaID'].value_counts(ascending=False).plot.bar() - Barra vertical
# data_frame['LojaID'].value_counts(ascending=True).plot.barh(); - Barra horizontal ignorando a primeira, utilizado ponto e virgula
# data_frame.groupby(data_frame['Data'].dt.year)['Receita'].sum().plot.pie() - Grafico de pizza
# plt.show()

# Total de vendas por cidade
imprime_jogo_da_velha()
print(data_frame['Cidade'].value_counts())

imprime_jogo_da_velha()
data_frame['Cidade'].value_counts().plot.bar(title='Total de vendas por Cidade', color='red')
plt.xlabel('Cidade')
plt.ylabel('Total Vendas')
plt.show()
