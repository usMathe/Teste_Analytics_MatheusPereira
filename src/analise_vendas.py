import pandas as pd

df = pd.read_csv(r'data\data_clean.csv')

#Valor do total de vendas de cada produto
total_por_produto = df.groupby('PRODUTO')['PRECO_UNI'].sum()


# Soma de todas as vendas
faturamento_total = total_por_produto.sum()

print(total_por_produto)
print('--------------------------------------------------------')
print(f'O produto com maior faturamento foi o {total_por_produto.idxmax()} com valor total de R$: {total_por_produto.max()}')
print(f'Faturamento total R$: {faturamento_total:.2f}')

