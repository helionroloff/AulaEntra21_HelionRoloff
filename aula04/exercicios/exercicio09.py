
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.


nome = input("informe o nome do cliente")
qnt = int(input("qual a quantidade de produtos o cliente deseja"))
preco = float(input("qual o valor do produto?"))
valorvenda = float(preco*qnt)
print('o cliente',nome,'teve uma venda de',valorvenda)
print('o cliente',nome,'teve uma venda de',preco*qnt)