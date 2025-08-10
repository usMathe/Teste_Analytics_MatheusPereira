import pandas as pd
from sqlalchemy import create_engine

dados_bruto = r'data\dados_bruto_vendas.csv'

# Carregar os dados ja garantindo alguns formatos
df = pd.read_csv(dados_bruto, dtype={'ID': str, 'QUANTIDADE': int, 'PRECO_UNI': float}, parse_dates=['DATA'])

# Total de linhas no DataFrame
total_linhas = len(df)

# Total de linhas SEM NaN
linhas_sem_nan = len(df.dropna())

# Total de linhas COM NaN = Total - Sem NaN
total_linhas_com_nan = total_linhas - linhas_sem_nan

#  A técnica de limpaza aqui é deletar linhas onde as colunas tem NaN, porem so realiza essa técnica se a quantidade de linhas com NaN é menor 
# que 10% dos dados total, caso contrario prenche com a média dos valores daquele produto
if total_linhas * 0.1 > total_linhas_com_nan:
    df = df.dropna()
else:
    media_prod = df.groupby('PRODUTO')['PRECO_UNI'].transform("mean")
    df['PRECO_UNI'] = df['PRECO_UNI'].fillna(media_prod)

# Remover valores duplicados
df = df.drop_duplicates()
df.to_csv('data/data_clean.csv', index=False)
print(df)

# --------- DADOS EM TABELA PARA O SQLite ---------
# Salvar direto em um banco para fazer as consultas
db_file = r'data\analise_vendas.db'
table_name = 'vendas_teste'

# Crie a conexão com o banco de dados.
engine = create_engine(f'sqlite:///{db_file}')
print(f"\n--- Conectando ao banco de dados: {db_file} ---")

# Salve o DataFrame 'df' na tabela 'vendas' do banco.
df.to_sql(
    table_name,
    con=engine,
    if_exists='replace', # Apaga a tabela antiga e cria uma nova com os dados limpos
    index=False          # Não salva o índice do pandas no banco
)

print(f"SUCESSO! Os dados foram salvos diretamente na tabela '{table_name}'.")
