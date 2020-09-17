#'''
#Exercício 01

#Crie um programa que cadastre 5 clientes. 

#Cada cliente possui: Nome, sexo, Telefone
#(Guarde estes dados em listas separadas).

#Depois mostre os dados cadastrados no seguinte formato:



#***********************************
#Relatório de clientes cadastrados 
#***********************************
#Nome: 
#Sexo:
#Telefone:
#***********************************
#'''

nomes=[]
sexos=[]
telefones=[]

for i in range(5):
    nome=input('informe o nome: ')
    sexo=input('informe o sexo: ')
    telefone=input('informe o telefone: ')
    nomes.append(nome)
    sexos.append(sexo)
    telefones.append(telefone)

print('''
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
''')
for i in range(5):
    print(f'''
    ***********************************
    Nome:{nomes[i]} 
    Sexo:{sexos[i]}
    Telefone:{telefones[i]}
    ***********************************
    ''')


