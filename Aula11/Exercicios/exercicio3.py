#"""Exercício 3

#(use somente o while)

#Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

#Para mairores de 18 anos: Entrada Permitida
#Para menores de 18 anos: Entrada proibida.

#Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

#Regras:
#- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
#- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
#"""
nomes=[]
opcao=('')
while opcao!='N':
    nome=str(input(f'INFORME O NOME DO CLIENTE: ')).strip()
    if nome=="":
        print('NOME EM BRANCO')
    else:
        idade=input('INFORME A IDADE: ').strip()
        if idade=="":
            print('OBRIGADO PELA PREFERÊNCIA')
            opcao='N'
        elif idade!="":
            idade=int(idade)
            if idade>=18:        
                print('ENTRADA PERMITIDA')
                nomes.append(nome)
                opcao=(input('DESEJA CADASTRAR MAIS UMA PESSOA? S/N: ')).strip().upper()
            else:
                print('ENTRADA PROIBIDA')
                opcao=(input('DESEJA CADASTRAR MAIS UMA PESSOA? S/N: ')).strip().upper()
                
if nomes!="":
    print('OS NOMES DOS CLIENTES MAIORES DE IDADE SÃO: ')
    for i in nomes:
        print(i)
print('********FIM DE PROGRAMA********')