import pandas as pd

def imprime_jogo_da_velha():
    return print('###############')
    
# Lendo dados do csv
data_frame = pd.read_csv('../datasets/Gapminder.csv', on_bad_lines='skip', sep=';')

# Renomeando o cabeçalho
d_f_r = data_frame.rename(
        columns={'country': 'País', 'continent': 'Continente', 'year': 'Ano', 'lifeExp': 'Expec. de vida', 'pop': 'Total pop.', 'gdpPercap': 'PIB'}
    )


    # Total de linhas e colunas
imprime_jogo_da_velha()
print(d_f_r.shape)

    # Exibe as colunas
imprime_jogo_da_velha()
print(d_f_r.columns)

    # Exibe o tipo de dado das colunas
imprime_jogo_da_velha()
print(d_f_r.dtypes)

    # Exibe as primeiras linhas
imprime_jogo_da_velha()
print(d_f_r.head())

    # Exibe as últimas linhas
imprime_jogo_da_velha()
print(d_f_r.tail())

    # Retorna informações estatisticas do conjunto de dados
imprime_jogo_da_velha()
print(d_f_r.describe())

    # Retorna os valores unicos de continente
imprime_jogo_da_velha()
print(d_f_r['Continente'].unique())

    # Utilizando filtros
imprime_jogo_da_velha()
oceania = d_f_r.loc[d_f_r['Continente'] == 'Oceania']
print(oceania.head())

    # Agrupamento
imprime_jogo_da_velha()
print(d_f_r.groupby('Continente')['País'].nunique())

    # Espectativa media para cada pais
imprime_jogo_da_velha()
print(d_f_r.groupby('Ano')['Expec. de vida'].mean())
    
    # Média PIB
imprime_jogo_da_velha()
print(d_f_r['PIB'].mean())
    
    # Soma PIB
imprime_jogo_da_velha()
print(d_f_r['PIB'].sum())
