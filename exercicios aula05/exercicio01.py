# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
# 
num1 = int(input('informe o primeiro numero'))
num2 = int(input('informe o segundo numero'))

if num1 > num2:
    print('o primeiro número é maior')
elif num2 > num1:
    print('o segundo número é maior')
else:
    print('os números são iguais')