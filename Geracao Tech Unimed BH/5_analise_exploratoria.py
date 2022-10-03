import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

def imprime_jogo_da_velha():
    return print('###############')

data_frame = pd.read_excel('../datasets/AdventureWorks.xlsx')

# Receita total
imprime_jogo_da_velha()
print(data_frame['Valor Venda'].sum())

# Custo total por venda
imprime_jogo_da_velha()
custo_total = data_frame['custo'] = data_frame['Custo Unitário'].mul(data_frame['Quantidade'])
print(custo_total)

# Custo total
imprime_jogo_da_velha()
print(round(data_frame['custo'].sum(), 2))

# Lucro total por venda
imprime_jogo_da_velha()
lucro_total = data_frame['lucro'] = data_frame['Valor Venda'] - data_frame['custo']
print(lucro_total)

# Lucro total
imprime_jogo_da_velha()
print(round(data_frame['lucro'].sum(), 2))

# Criando uma coluna com total de dias para enviar o produto por venda
imprime_jogo_da_velha()
tempo_envio =  data_frame['Tempo_envio'] = (data_frame['Data Envio'] - data_frame['Data Venda']).dt.days # Trazendo somente os dias
print(tempo_envio)

# Média do tempo de envio por Marca
imprime_jogo_da_velha()
print(data_frame.groupby('Marca')['Tempo_envio'].mean())

# Agrupamento por ANO e Marca
imprime_jogo_da_velha()
pd.options.display.float_format = '{:20,.2f}'.format
print(data_frame.groupby([data_frame['Data Venda'].dt.year, 'Marca'])['lucro'].sum())

# Resetando index
imprime_jogo_da_velha()
lucro_ano = data_frame.groupby([data_frame['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()
print(lucro_ano)

# Qual o total de produtos vendidos
imprime_jogo_da_velha()
print(data_frame.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False))
