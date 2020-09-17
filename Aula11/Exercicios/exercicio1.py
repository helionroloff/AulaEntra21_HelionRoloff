#"""Exercício 1

#(não usar o continue ou o break)

#Crie um programa que mostre um memu com as seguites opções:

#1) Soma
#2) Subtração
#3) Multiplicação
#S) Para sair!

#Para número 1: Peça 2 números e mostre a soma deles
#Para número 2: Peça 2 númeors e mostre a subtração deles
#Para númeor 3: Peça 2 números e mostre a multiplicação deles
#Para S: Mostre uma mensagem de despedida e termine o programa.

#Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
#"""
opcao=str('')
while opcao!='S':
    print('''
    *************************************
    MENU DE OPERAÇÕES DISPONÍVEIS
    1) Soma
    2) Subtração
    3) Multiplicação
    S) Sair
    *************************************''')
    opcao=str(input('ESCOLHA UMA OPÇÃO DE OPERAÇÃO: '))
    opcao=opcao.upper()


    if opcao == '1':
        n1=int(input('INFORME O PRIMEIRO NÚMERO: '))
        n2=int(input('INFORME O SEGUNDO NÚMERO: ')) 
        s=n1+n2
        print(f'A SOMA DOS DOIS NÚMEROS É {s}')
    elif opcao == '2':
        n1=int(input('INFORME O PRIMEIRO NÚMERO: '))
        n2=int(input('INFORME O SEGUNDO NÚMERO: '))
        sub=n1-n2
        print(f'A SUBTRAÇÃO DOS DOIS NÚMEROS É {sub}')
    elif opcao =='3':
        n1=int(input('INFORME O PRIMEIRO NÚMERO: '))
        n2=int(input('INFORME O SEGUNDO NÚMERO: '))
        m=n1*n2
        print(f'A SUBTRAÇÃO DOS DOIS NÚMEROS É {m}')
    elif opcao =='S':
        print('OBRIGADO POR UTILIZAR NOSSO PROGRAMA')
    else:
        print('OPÇÃO INVÁLIDA')
   