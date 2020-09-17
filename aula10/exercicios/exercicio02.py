#"""Exercício 02

#O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

#Exemplo:
#id: 1
#Nome: Dudu

#id: 2
#Nome: Marta

#id: 3
#Nome: Pedro


#ATENÇÃO!!!!
#O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


#Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
#(cadastre no minimo 4 clientes)
#"""
id=0
ids=[]
nomes=[]
idades=[]


for i in range(5):
    id=id+1
    nome=input('informe o nome: ')
    idade=input('informe a idade: ')
    nomes.append(nome)
    idades.append(idade)
    ids.append(id)

for i in range(5):
    print(f'''
    id: {ids[i]}
    nome: {nomes[i]}
    idade: {idades[i]}
    ''')
idd=int(input('informe o id para mostrar os dados do cliente: '))
print(f'''
id: {ids[idd-1]}
nome: {nomes[idd-1]}
idade: {idades[idd-1]}    
    ''')

print('*'*5,'FIM','*'*5)