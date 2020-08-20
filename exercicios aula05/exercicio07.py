# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.
num1=int(input('informe o primeiro número'))
num2=int(input('informe o segundo número'))
num3=int(input('informe o terceiro número'))

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
else:
    print(num3)





