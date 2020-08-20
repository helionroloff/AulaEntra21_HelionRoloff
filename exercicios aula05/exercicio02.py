# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)
num=int(input('informe um número'))

if num > 0:
    print('número positivo')
elif num < 0:
    print('número negativo')
else:
    print('número zero')