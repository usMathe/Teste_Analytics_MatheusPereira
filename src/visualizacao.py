import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'data\data_clean.csv')

# Garantir que vai estar datetime e extrair mês-ano
df['DATA'] = pd.to_datetime(df['DATA'])
df['mes_ano'] = df['DATA'].dt.strftime('%m-%Y')

# Agrupar vendas por mês
vendas_por_mes = df.groupby('mes_ano')['PRECO_UNI'].sum().reset_index()

# Ordenar por data
vendas_por_mes = vendas_por_mes.sort_values('mes_ano')

datas = vendas_por_mes['mes_ano']
vendas = vendas_por_mes['PRECO_UNI']

# grarfico
plt.figure(figsize=(12, 6))
plt.plot(datas, vendas)
plt.title('Vendas por Mês')
plt.xlabel('Mês-Ano')
plt.ylabel('Total de Vendas (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()