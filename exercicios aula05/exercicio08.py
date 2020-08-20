# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

num1=int(input('informe o primeiro número '))
num2=int(input('informe o segundo número '))
num3=int(input('informe o terceiro número '))

if num1 > num2: 
    if num1 > num3:
        print(num1)
if num2 > num1:
    if num2 > num3:
        print(num2)
if num3 > num2:
    if num3 > num1:
        print(num3)




