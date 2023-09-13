import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo csv
acao_MGLU3 = pd.read_csv('MGLU3.SA.csv')


# Transformação a coluna Date em datetime
acao_MGLU3['Date'] = pd.to_datetime(acao_MGLU3['Date'])


# Filtragem da data para os dias 04, 05, 06, 07 do mês de março de 2017
data_filtrada_MGLU3 = acao_MGLU3.loc[(acao_MGLU3['Date'].dt.year == 2017) & (acao_MGLU3['Date'].dt.month == 3) & (acao_MGLU3['Date'].dt.day >= 4) & (acao_MGLU3['Date'].dt.day <= 7)]


# Exibe a média do fechamento dos valores da ação MGLU3
print('média: ' + str(data_filtrada_MGLU3['Close'].mean()))
