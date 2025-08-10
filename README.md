# Análise de Vendas 2023

Este projeto realiza uma análise de ponta a ponta sobre um conjunto de dados de vendas simuladas para o ano de 2023. O objetivo é demonstrar um fluxo de trabalho de análise de dados completo, incluindo geração de dados, limpeza (ETL), análise exploratória com Pandas, visualização de insights com Matplotlib e consultas com SQL.

## Estrutura do Repositório

O projeto está organizado da seguinte forma para separar as diferentes etapas da análise:

```
/projeto-vendas/
│
├── data/
│   ├── analise_vendas.db          # Banco de dados SQLite gerado pelo script de limpeza.
│   ├── dados_bruto_vendas.csv     # Dataset original com dados brutos e "sujos".
│   └── dados_clean.csv            # Dataset limpo, usado pelos scripts de análise e visualização.
│
├── img/
│   └── grafico_analise.png        # Grafico da análise
│
├── src/
│   ├── gerar_dados.py             # Script para simular e gerar o dataset bruto.
│   ├── limpeza_dados.py           # Script ETL: limpa os dados brutos e os carrega no banco de dados SQLite.
│   ├── analise_vendas.py          # Script que realiza cálculos e análises agregadas com Pandas.
│   └── visualizacoes.py           # Script que gera os gráficos e insights visuais da análise.
│
├── sql/
│   └── consultas_sql.sql          # Arquivo com queries SQL para análises no banco de dados.
│
├── relatorio/
│   └── relatorio_insights.md      # Relatório final com as conclusões e ações sugeridas.
│
└── README.md                      # Este arquivo, explicando o projeto.
```

## Tecnologias e Dependências

Este projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas e ferramentas:

* **Linguagem:** Python 3.9+
* **Bibliotecas Principais:**
    * `pandas`
    * `SQLAlchemy`
    * `matplotlib`
    * `Faker`
    * `numpy`
* **Ferramentas:**
    * **Visual Studio Code:** Editor de código recomendado.
    * **Extensão SQLite:** Extensão "SQLite" (publicada por alexcvzz) para interagir com o banco de dados `.db` diretamente no VS Code.

### Instalação

1.  Clone este repositório para a sua máquina local.
2.  Instale todas as dependências necessárias:
    ```bash
    pip install pandas sqlalchemy matplotlib faker numpy
    ```

## Como Executar o Projeto

Existem duas maneiras de explorar este projeto:

### Opção A: Reproduzir a Análise Original (Recomendado)

Esta opção utiliza os dados que já estão no repositório para que você possa ver os mesmos resultados apresentados no relatório.

1.  **Visualização Mensal:**
    ```bash
    python src/visualizacoes.py
    ```
2.  **Análise de Produtos:**
    ```bash
    python src/analise_vendas.py
    ```
3.  **Análise com SQL:**
    * No VS Code, com a extensão SQLite instalada, abra o arquivo `data/analise_vendas.db`.
    * O painel `SQLITE EXPLORER` aparecerá na barra lateral.
    * Abra o arquivo `sql/consultas_sql.sql`, selecione as queries que deseja executar, clique com o botão direito e escolha `Run Selected Query`.

### Opção B: Executar o Pipeline Completo (Gerar Novos Dados)

Esta opção irá gerar um novo conjunto de dados aleatórios. **Atenção:** os resultados e insights serão diferentes dos apresentados no relatório.

1.  **Gerar Dados Brutos:**
    ```bash
    python src/gerar_dados.py
    ```
2.  **Limpar e Carregar no Banco:**
    ```bash
    python src/limpeza_dados.py
    ```
3.  **Executar Análises:** Siga os passos da **Opção A** para analisar os novos dados.
