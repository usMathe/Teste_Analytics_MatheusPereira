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
# Salva a imagem em um arquivo usado para análise
plt.savefig('img/grafico_analise.png')
plt.show()

print("Gráfico com anotações salvo como 'grafico_vendas_analise.png'")

# --- Anotações e Insights ---

analise_texto = """
=====================================================
        ANÁLISE E INSIGHTS DO GRÁFICO DE VENDAS
=====================================================

Aqui estão as principais observações dos dados de vendas de 2023:

Insight 1: Forte Sazonalidade em Novembro
-------------------------------------------
- PICO: As vendas atingiram o ponto mais alto do ano em Novembro, superando R$ 25.000.
- MOTIVO PROVÁVEL: Este pico é característico de eventos como a Black Friday, que concentra um volume de compras muito acima da média.

Insight 2: Uma Grande Queda
-------------------------------------------
- QUEDA PÓS-PICO: Após o recorde de Novembro, as vendas de Dezembro caíram para o nível mais baixo do ano. Isso pode sugerir que a Black Friday pode ter antecipado as compras de Natal.
Outro ponto de baixa relevante ocorreu em Agosto, representando o mês mais fraco do segundo semestre.

=====================================================
"""

print(analise_texto)
