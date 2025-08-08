from faker import Faker
import datetime
import random
import pandas as pd
import numpy as np


fake = Faker()

#datas aleatorias baseadas no periodo colocados no datetime
start_date = datetime.date(year=2023, month=1, day=1)
end_date = datetime.date(year=2023, month=12, day=31)
#date = fake.date_between(start_date=start_date, end_date=end_date)

lista_produtos = ['iPhone','Samsung Galaxy', 'MacBook Air', 'Dell Inspiron', 'iPad', 'Samsung Galaxy Tab', 'Xbox',
             'Smart TV LG', 'PlayStation', 'JBL', 'Apple Watch', 'Xiaomi Mi Band', 'Mouse Razer', 'Mouse Logitech', 'Teclado Logitech']

categorias = {
    'iPhone':'Celular',
    'Samsung Galaxy':'Celular',
    'MacBook Air':'Notebook',
    'Dell Inspiron':'Notebook',
    'iPad':'Tablet',
    'Samsung Galaxy Tab':'Tablet',
    'Xbox':'Videogame',
    'Smart TV LG':'TV',
    'PlayStation':'Videogame',
    'JBL':'Áudio',
    'Apple Watch':'Relógio', 
    'Xiaomi Mi Band':'Relógio',
    'Mouse Razer':'Periférico', 
    'Mouse Logitech':'Periférico', 
    'Teclado Logitech':'Periférico'
}

id = []
data = []
produto = []
categoria = []
quantidade = []
preco = []


for i in range(0, 50):

    id.append(i)
    data.append(fake.date_between(start_date=start_date, end_date=end_date))
    produto.append(random.choice(lista_produtos))
    categoria.append(categorias[produto[i]])
    quantidade.append(random.randint(1, 10))
    preco.append(round(random.uniform(100,5000),2))
    

#Gerar um DataFrame

df = pd.DataFrame(
    {
        'ID': id,
        'DATA': data,
        'PRODUTO': produto,
        'CATEGORIA': categoria,
        'QUANTIDADE': quantidade,
        'PRECO_UNI': preco
    }

)

#Insirir dados problemas nos dados para fazer a limpeza
#3 valores faltantes aleatórios na coluna 'PRECO_UNI'
for _ in range(3):
    indice_df = random.randint(0, len(df) - 1)
    df.loc[indice_df, 'PRECO_UNI'] = np.nan

# Adiciona algumas linhas duplicadas
df = pd.concat([df, df.sample(3, random_state=50)], ignore_index=True)

print(df)

# Gerar arquivo csv
df.to_csv('data/dados_bruto_vendas.csv', index=False)
