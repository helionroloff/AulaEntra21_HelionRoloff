# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 
num1=int(input('informe o primeiro número'))
num2=int(input('informe o segundo número '))
num3=int(input('informe o terceiro número '))

if num1>num2>num3:
    maior=num1
    meio=num2
    menor=num3
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
elif num1>num3>num2:
    maior=num1
    meio=num3
    menor=num2
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
elif num2>num1>num3:
    maior=num2
    meio=num1
    menor=num3
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
elif num2>num3>num1:
    maior=num2
    meio=num3
    menor=num1
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
elif num3>num2>num1:
    maior=num3
    meio=num2
    menor=num1
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
elif num3>num1>num2:
    maior=num3
    meio=num1
    menor=num2
    print(f'maior número {maior},número do meio {meio}, número menor{menor}')
