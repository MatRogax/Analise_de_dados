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




