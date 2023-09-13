import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos arquivos csv
acao_LREN3 = pd.read_csv('LREN3.SA.csv')
acao_MGLU3 = pd.read_csv('MGLU3.SA.csv')

# Transformação da coluna Date em datetime
acao_LREN3['Date'] = pd.to_datetime(acao_LREN3['Date'])
acao_MGLU3['Date'] = pd.to_datetime(acao_MGLU3['Date'])

# Filtragem dos dados para o dia 8 de fevereiro de 2017
data_filtrada_LREN3 = acao_LREN3.loc[(acao_LREN3['Date'].dt.year == 2017) & (acao_LREN3['Date'].dt.month == 2) & (acao_LREN3['Date'].dt.day == 8)]
data_filtrada_MGLU3 = acao_MGLU3.loc[(acao_MGLU3['Date'].dt.year == 2017) & (acao_MGLU3['Date'].dt.month == 2) & (acao_MGLU3['Date'].dt.day == 8)]

data_filtrada_LREN3['Prices'] = data_filtrada_LREN3[['Open', 'High', 'Low', 'Close']].values.tolist()
data_filtrada_MGLU3['Prices'] = data_filtrada_MGLU3[['Open', 'High', 'Low', 'Close']].values.tolist()

# Criação de um subplot com duas caixas de box lado a lado
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plotagem do gráfico de caixa para LREN3
axes[0].boxplot(data_filtrada_LREN3["Prices"], labels=['LREN3'], vert=True)
axes[0].set_title('Distribuição dos Preços de Fechamento e Abertura em 08/02/2017 (LREN3)')
axes[0].set_ylabel('Preços')
axes[0].set_xlabel('Ação')

# Plotagem do gráfico de caixa para MGLU3
axes[1].boxplot(data_filtrada_MGLU3["Prices"], labels=['MGLU3'], vert=True)
axes[1].set_title('Distribuição dos Preços de Fechamento e Abertura em 08/02/2017 (MGLU3)')
axes[1].set_ylabel('Preços')
axes[1].set_xlabel('Ação')

plt.tight_layout()  # Garante que as caixas de box não se sobreponham
plt.show()

# Análise da ação da LRNE3 ( lojas renner )

"""
A caixa representa o intervalo interquartil (IQR), ou seja, a diferença entre o terceiro quartil (Q3)
e o primeiro quartil (Q1) dos preços de fechamento da ação LREN3 em 08/02/2017. O limite superior da 
caixa é Q3, e o limite inferior é Q1. O traço no meio da caixa representa a mediana (Q2),representando
com um candle de força um  aumento forte e contínuo da ação LREN3.
"""

# Análise da ação da MGLU3 ( Magazine Luisa )

"""
A caixa representa o intervalo interquartil (IQR), ou seja, a diferença entre o terceiro quartil (Q3)
e o primeiro quartil (Q1) dos preços de fechamento da ação LREN3 em 08/02/2017. O limite superior da 
caixa é Q3, e o limite inferior é Q1,representando graficamente com um candle de médio que não indica força
mas indica uma constante ou uma força no dia 08/02/2017.

"""