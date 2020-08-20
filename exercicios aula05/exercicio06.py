# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente
num1=int(input('informe o primeiro número '))
num2=int(input('informe o segundo número '))

if num1 > num2:
    print('o número menor e o maior são respetivamente',num2,'e',num1)
elif num1 < num2:
    print('o número menor e o maior são respetivamente',num1,'e',num2)
else:
    print('os números tem o mesmo valor')