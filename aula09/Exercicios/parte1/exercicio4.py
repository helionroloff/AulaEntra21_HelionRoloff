"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""

nomes=[]
idades=[]
emails=[]
for i in range(10):
    nome=str(input(f'Informe o nome {i+1} '))
    nomes.append(nome)
for i in range(10):
    idade=str(input(f'Informe a idade {i+1} '))
    idades.append(idade)
for i in range(10):
    email=str(input(f'Informe o email {i+1} '))
    emails.append(email)
print('''
As listas em formato de valores são: 
''')
print(f'Lista de nomes:{nomes}')
print(f'Lista de idades:{idades}')
print(f'Lista de emails:{emails}')
print("""
As listas também podem ser impressas sem ' e , como a seguir: 
""")
print('''
***lista de nomes***
''')
for i in nomes:
    print(i)
print('''
***lista de idades***
''')
for i in idades:
    print(i)
print('''
***lista de emails***
''')
for i in emails:
    print(i)
print('''
***FIM***
''')