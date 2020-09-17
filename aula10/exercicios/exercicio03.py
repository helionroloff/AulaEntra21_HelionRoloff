#"""Exercício 03

#3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

#3.2) Depois mostre os dados dos 5 clientes.

#3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

#3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
#- Para menores de 17 anos: Entrada Proibida
#- Para maiores de 17 anos: Entrada Liberada
#- Para o sexo Feminino: 50% de desconto
#- Para o sexo Masculino: 5% de desconto
#"""

id=0
ids=[]
nomes=[]
sexos=[]
idades=[]


for i in range(2):
    id=id+1
    nome=input('informe o nome: ')
    sexo=input('informe o sexo: M/F ')
    idade=int(input('informe a idade: '))
    print('\n')
    nomes.append(nome)
    sexos.append(sexo)
    idades.append(idade)
    ids.append(id)

for i in range(2):
    print(f'''
    ID: {ids[i]}
    Nome: {nomes[i]} 
    Sexo: {sexos[i]}
    Idade: {idades[i]}
    ''')

while True:
    escolha=int(input(f'Escolha um ID para mais informações: 1 - {len(ids)}: '))
    if escolha>=1 and escolha<= len(ids):
        print(f'''
        ID: {ids[escolha-1]}
        Nome: {nomes[escolha-1]} 
        Sexo: {sexos[escolha-1]}
        Idade: {idades[escolha-1]}
        ''')
        if idades[escolha-1] <17:
            print('ENTRADA PROIBIDA')
        else:
            print('ENTRADA LIBERADA')
            if sexos[escolha-1] == 'F' or sexos[escolha-1] == 'f':
                print(f'50% de desconto!')
            elif sexos[escolha-1] == 'M' or sexos[escolha-1] == 'm':
                print(f'5% de desconto!')
        continuar=input('''
        Deseja consultar outro ID? S-N 
        ''')
        if continuar=='N' or continuar=='n':
            break
    else:
        print('NÚMERO INVÁLIDO')

escolha=int(input(f'Escolha um ID para mais informações: 1 - {len(ids)}: '))

if idades[escolha-1] <17:
    print('ENTRADA PROIBIDA')
else:
    print('ENTRADA LIBERADA')
    if sexos[escolha-1] == 'F' or sexos[escolha-1] == 'f':
        print(f'50% de desconto!')
    elif sexos[escolha-1] == 'M' or sexos[escolha-1] == 'm':
        print(f'5% de desconto!')

     

