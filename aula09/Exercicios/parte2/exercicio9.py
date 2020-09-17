
"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""
vendas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
listamenores=[]
listamaiores=[]

for i in vendas:
    if i<500:
        listamenores.append(i)
    else:
        listamaiores.append(i)
print(f'da lista de números de valor menor a 500, o menor valor é {min(listamenores)} e o maior é {max(listamenores)}')
print(f'da lista de números de valor 500 ou superior, o menor valor é {min(listamaiores)} e o maior é {max(listamaiores)}')
