# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

prod1=input('diga o nome do primeiro produto')
prod2=input('informe o nome dosegundoproduto')
qnt1=int(input('qual a quantidade comprada do primeiro produto?'))
qnt2=int(input('qual a quantidade comprada do segundo produto?'))
preco1=float(input('qual o valor do primeiro produto?'))
preco2=float(input('qual o valor do segundo produto?'))
print(prod1,'custa por unidade',preco1,'e foram',qnt1,'unidades, custando ao todo',preco1*qnt1)
print(prod2,'custa por unidade',preco2,'e foram',qnt2,'unidades, custando ao todo',preco2*qnt2)