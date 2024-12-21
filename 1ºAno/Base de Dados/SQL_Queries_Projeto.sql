--Query1 
--Quais os produtos vendidos, em valor e quantidade no corrente mês;

SELECT Faturas.PRODUCT_CODE, SUM(Faturas.QUANTITY),sum(Faturas.value) as TotalValor,sum(Faturas.QUANTITY)  as TotalQuantidade
FROM Faturas
where MONTH(DATE) = MONTH(GETDATE()) and YEAR(DATE) = YEAR(GETDATE())
GROUP BY Faturas.PRODUCT_CODE;

--Query2 
--Quais os produtos comprados, em valor e quantidade no corrente mês;

Select Supplier.PRODUCT_CODE as Produto,Sum(Supplier.PRICE) as Valor,Sum(Supplier.QUANTITY) as Quantidade 
from Supplier

where MONTH(Supplier.BUY_DATE) = MONTH(GETDATE()) and YEAR(Supplier.BUY_DATE) = YEAR(GETDATE())
Group by Supplier.PRODUCT_CODE

--Query3 
--Quais os produtos transferidos, em quantidade, e com a informação da loja de saída e da loja de entrada do stock, na corrente semana.

select MOVIMENTOS.PRODUCT_CODE as produtos, MOVIMENTOS.QUANTITY as quantidade,MOVIMENTOS.STORE_OUT_CODE as loja_de_saida,MOVIMENTOS.STORE_IN_CODE as loja_de_entrada
where datepart(ww, getdate())= datepart(ww, MOVIMENTOS.date)
group by MOVIMENTOS.product_Code ,MOVIMENTOS.store_out_code, MOVIMENTOS.store_in_code


--Query4 
--Quais o top 3 de empregados com mais vendas em valor no corrente mês.

select TOP 3 FUNCIONARIOS.EMPLOYEE_NUMBER,Funcionarios.NAME,SUM(Total) as Total from Funcionarios inner join Faturas on Faturas.EMPLOYEE_NUMBER= Funcionarios.EMPLOYEE_NUMBER
Group By Funcionarios.EMPLOYEE_NUMBER,Funcionarios.NAME
Order By Total desc

--Query5 
-- Produtos vendidos em quantidade no corrente mês e respectiva comparação com o mês anterior.

SELECT Faturas.PRODUCT_CODE, SUM(Faturas.QUANTITY),sum(Faturas.value) as TotalValorMesAtual,sum(Faturas.QUANTITY)  as TotalQuantidadeMesAtual
FROM Faturas
where MONTH(DATE) = MONTH(GETDATE()) and YEAR(DATE) = YEAR(GETDATE())
GROUP BY Faturas.PRODUCT_CODE;

SELECT Faturas.PRODUCT_CODE, SUM(Faturas.QUANTITY),sum(Faturas.value) as TotalValorMesPassado,sum(Faturas.QUANTITY)  as TotalQuantidadeMesPassado
FROM Faturas
where MONTH(DATE) = MONTH(MONTH(DATEADD(MONTH, -1, CURRENT_TIMESTAMP))) and YEAR(DATE) = YEAR(MONTH(DATEADD(MONTH, -1, CURRENT_TIMESTAMP)))

GROUP BY Faturas.PRODUCT_CODE;

--Query6 
--Que produtos foram vendidos em valor e com o número de fatura.
SELECT Faturas.PRODUCT_CODE, Faturas.VALUE, Faturas.INVOICE_NUMBER
FROM Faturas
GROUP BY Faturas.PRODUCT_CODE, Faturas.INVOICE_NUMBER, Faturas.VALUE;


--Query7 
--Qual a família de produtos com mais venda no corrente Ano, valor.
Select Nome from ( 
Select top 1 Familias.ID_FAMILY,Familias.FAMILY_CODE as Nome, sum(QUANTITY) as TotalQuantidade from Faturas

inner join Produtos on Produtos.PRODUCT_CODE = Faturas.PRODUCT_CODE
inner join Familias on Familias.ID_FAMILY = Produtos.FAMILY_CODE
where YEAR(DatE) = YEAR(GETDATE())
Group By  Familias.ID_FAMILY,Familias.FAMILY_CODE
order by TotalQuantidade desc) as t
 