/* 
Query para listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) 
para cada produto. Ordene o resultado pelo valor total de vendas em ordem decrescente. */
SELECT 
  PRODUTO, 
  CATEGORIA,
  DATA,
  SUM(PRECO_UNI) AS TOTAL_PRODUTO 
FROM vendas
GROUP BY PRODUTO
ORDER BY TOTAL_PRODUTO DESC;


/* 
Query para identificar os produtos que venderam menos no mês de junho de 2023.
*/
SELECT 
  PRODUTO, 
  DATA,
  SUM(PRECO_UNI) AS TOTAL_PRODUTO 
FROM vendas
WHERE DATA >= '2023-06-01' AND DATA < '2023-07-01'
GROUP BY PRODUTO
ORDER BY TOTAL_PRODUTO ASC;
