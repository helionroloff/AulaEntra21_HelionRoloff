
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
nomes=[]

for i in range(10):
    nomes.append(input(f'insira o nome da pessoa {i+1}: '))
print('''
Os nomes informados foram:
''')
for i in nomes:
    print(i)