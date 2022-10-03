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

# Criar uma nova coluna de Ano
imprime_jogo_da_velha()
data_frame['Ano_Venda'] = data_frame['Data'].dt.year

# Criar uma nova de mês e dia
imprime_jogo_da_velha()
data_frame['mes_venda'], data_frame['dia_venda'] = data_frame['Data'].dt.month, data_frame['Data'].dt.day

    # Grafico impressos em tipos
# imprime_jogo_da_velha()
# data_frame['LojaID'].value_counts(ascending=False).plot.bar() - Barra vertical
# data_frame['LojaID'].value_counts(ascending=True).plot.barh(); - Barra horizontal ignorando a primeira, utilizado ponto e virgula
# data_frame.groupby(data_frame['Data'].dt.year)['Receita'].sum().plot.pie() - Grafico de pizza

    # Total de vendas por cidade
# imprime_jogo_da_velha()
# print(data_frame['Cidade'].value_counts())

# imprime_jogo_da_velha()
# data_frame['Cidade'].value_counts().plot.bar(title='Total de vendas por Cidade', color='red')
# plt.xlabel('Cidade')
# plt.ylabel('Total Vendas')
   
    # Alterando estilo
# imprime_jogo_da_velha()
# plt.style.use('ggplot')

# data_frame.groupby(data_frame['mes_venda'])['Qtde'].sum().plot(title = 'Total produtos vendidos por mês')
# plt.xlabel('Mês')
# plt.ylabel('Total Produtos Vendidos')
# plt.legend()

    # Quantidade por mês de venda
imprime_jogo_da_velha()
print(data_frame.groupby(data_frame['mes_venda'])['Qtde'].sum())

    # Quantidade de vendas no ano de 2019
# imprime_jogo_da_velha()
data_frame_2019 = data_frame[data_frame['Ano_Venda'] == 2019]
# data_frame_2019.groupby(data_frame_2019['mes_venda'])['Qtde'].sum().plot(marker = 'v')
# plt.xlabel('Mês')
# plt.ylabel('Total Produtos Vendidos')
# plt.legend()

    # Quantidade no gráfico de histograma
# plt.hist(data_frame['Qtde'], color='magenta')

    # Exemplo de gráfico de dispersão
# plt.scatter(x = data_frame_2019['dia_venda'], y = data_frame_2019['Receita'])
# plt.show()

    # Quantidade de vendas no ano de 2019
imprime_jogo_da_velha()
data_frame_2019.groupby(data_frame_2019['mes_venda'])['Qtde'].sum().plot(marker = 'v')
plt.title('Quantidade de produtos vendidos x mês')
plt.xlabel('Mês')
plt.ylabel('Total Produtos Vendidos')
plt.legend()
plt.savefig('produtos Qtde X Mes.png')