#"""Exercício 2

#(não usar o continue ou o break)

#Crie um menu interativo com as seguintes opções:

#A) soma
#B) Média
#C) Taboada
#S) Sair


#Para A: Peça 2 números, some e mostr o resultado
#Para B: Peça 4 números, faça a média e mostre o resultado
#Para C: Peça um número e mostre a taboada dele
#Para S: Mostre uma mensagem de despidida e encerre o programa.
#Para qualquer outro valor: Mostre a mensagem "opção inválida"
opcao=str('')
while opcao!='s':
    print('''
    *************************************
    MENU DE OPERAÇÕES DISPONÍVEIS
    1- Soma
    2- Média
    3- Taboada
    S) Sair
    *************************************''')
    opcao=str(input('ESCOLHA UMA OPÇÃO DE OPERAÇÃO: '))

    if opcao == '1':
        n1=int(input('INFORME O PRIMEIRO NÚMERO: '))
        n2=int(input('INFORME O SEGUNDO NÚMERO: ')) 
        s=n1+n2
        print(f'A SOMA DOS DOIS NÚMEROS É {s}')
    elif opcao == '2':
        n1=float(input('INFORME O PRIMEIRO NÚMERO: '))
        n2=float(input('INFORME O SEGUNDO NÚMERO: '))
        n3=float(input('INFORME O TERCEIRO NÚMERO: '))
        n4=float(input('INFORME O QUARTO NÚMERO: '))
        media=(n1+n2+n3+n4)/4
        print(f'A MÉDIA DOS QUATRO NÚMEROS É {media}')
    elif opcao =='3':
        n1=int(input('INFORME O NÚMERO DO QUAL DESEJA VISUALIZAR A TABUADA: '))
        for i in range(1,11):
            print(f'{n1} X {i} = {n1*i}')
    elif opcao =='s':
        print('OBRIGADO POR UTILIZAR NOSSO PROGRAMA')
    else:
        print('OPÇÃO INVÁLIDA')
   