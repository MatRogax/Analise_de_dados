import pandas as pd
import matplotlib.pyplot as plt
from time import sleep
import os

print('Gerando gráficos...')
sleep(1)
os.system('cls')

# Leitura dos arquivos csv

acao_LREN3 = pd.read_csv('LREN3.SA.csv')
acao_MGLU3 = pd.read_csv('MGLU3.SA.csv')

# Transformando a coluna Date em datetime para servir de referência para o eixo x

acao_LREN3['Date'] = pd.to_datetime(acao_LREN3['Date'])
acao_MGLU3['Date'] = pd.to_datetime(acao_MGLU3['Date'])


data_filtrada_LREN3 = acao_LREN3.loc[(acao_LREN3['Date'].dt.year >= 2017) & (acao_LREN3['Date'].dt.year <= 2019)]
data_filtrada_MGLU3 = acao_MGLU3.loc[(acao_MGLU3['Date'].dt.year >= 2017) & (acao_MGLU3['Date'].dt.year <= 2019)]


# Gráfico de fechamento das ações

plt.plot(data_filtrada_LREN3['Date'], data_filtrada_LREN3['Close'], linestyle= '-', linewidth= 1, color= 'yellow', label= 'Fechamento LREN3')
plt.plot(data_filtrada_MGLU3['Date'], data_filtrada_MGLU3['Close'], linestyle= '-', linewidth= 1, color= 'cyan', label= 'Fechamento MGLU3')


# Gráfico de abertura das ações

plt.plot(data_filtrada_LREN3['Date'], data_filtrada_LREN3['Open'], linestyle= ':', linewidth= 3, color= 'red', label= 'Abertura LREN3')
plt.plot(data_filtrada_MGLU3['Date'], data_filtrada_MGLU3['Open'], linestyle= ':', linewidth= 3, color= 'blue', label= 'Abertura MGLU3')


plt.title('Evolução dos preços das ações LREN3 e MGLU3')
plt.legend(loc = 4)
plt.xlabel('Anos')
plt.ylabel('Preço')
plt.show()

# Transformar a coluna Date em datetime
acao_LREN3['Date'] = pd.to_datetime(acao_LREN3['Date'])
acao_MGLU3['Date'] = pd.to_datetime(acao_MGLU3['Date'])

# Filtrar os dados para o dia 8 de fevereiro de 2017
data_filtrada_LREN3 = acao_LREN3.loc[(acao_LREN3['Date'].dt.year == 2017) & (acao_LREN3['Date'].dt.month == 2) & (acao_LREN3['Date'].dt.day == 8)]
data_filtrada_MGLU3 = acao_MGLU3.loc[(acao_MGLU3['Date'].dt.year == 2017) & (acao_MGLU3['Date'].dt.month == 2) & (acao_MGLU3['Date'].dt.day == 8)]

data_filtrada_LREN3['Prices'] = data_filtrada_LREN3[['Open', 'High', 'Low', 'Close']].values.tolist()
data_filtrada_MGLU3['Prices'] = data_filtrada_MGLU3[['Open', 'High', 'Low', 'Close']].values.tolist()

# Criar um subplot com duas caixas de box lado a lado
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plotar a caixa de box para LREN3
axes[0].boxplot(data_filtrada_LREN3["Prices"], labels=['LREN3'], vert=True)
axes[0].set_title('Distribuição dos Preços de Fechamento e Abertura em 08/02/2017 (LREN3)')
axes[0].set_ylabel('Preços')
axes[0].set_xlabel('Ação')

# Plotar a caixa de box para MGLU3
axes[1].boxplot(data_filtrada_MGLU3["Prices"], labels=['MGLU3'], vert=True)
axes[1].set_title('Distribuição dos Preços de Fechamento e Abertura em 08/02/2017 (MGLU3)')
axes[1].set_ylabel('Preços')
axes[1].set_xlabel('Ação')

plt.tight_layout()  # Garante que as caixas de box não se sobreponham
plt.show()

#análise da ação da LRNE3 ( lojas renner )

"""
A caixa representa o intervalo interquartil (IQR), ou seja, a diferença entre o terceiro quartil (Q3)
e o primeiro quartil (Q1) dos preços de fechamento da ação LREN3 em 08/02/2017. O limite superior da 
caixa é Q3, e o limite inferior é Q1. O traço no meio da caixa representa a mediana (Q2),representando
com um candle de força um  aumento forte e contínuo da ação LREN3.
"""

#análise da ação da MGLU3 ( Magazine Luisa )

"""
A caixa representa o intervalo interquartil (IQR), ou seja, a diferença entre o terceiro quartil (Q3)
e o primeiro quartil (Q1) dos preços de fechamento da ação LREN3 em 08/02/2017. O limite superior da 
caixa é Q3, e o limite inferior é Q1,representando graficamente com um candle de médio que não indica força
mas indica uma constante ou uma força no dia 08/02/2017.

"""

# Transformação a coluna Date em datetime
acao_MGLU3['Date'] = pd.to_datetime(acao_MGLU3['Date'])

# Filtragem da data para os dias 04, 05, 06, 07 do mês de março de 2017
data_filtrada_MGLU3 = acao_MGLU3.loc[(acao_MGLU3['Date'].dt.year == 2017) & (acao_MGLU3['Date'].dt.month == 3) & (acao_MGLU3['Date'].dt.day >= 4) & (acao_MGLU3['Date'].dt.day <= 7)]

# Exibe a média do fechamento dos valores da ação MGLU3
print(data_filtrada_MGLU3['Close'].mean())



