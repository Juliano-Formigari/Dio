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

# Grafico de barras
imprime_jogo_da_velha()
data_frame['LojaID'].value_counts(ascending=False).plot.bar()
plt.show()