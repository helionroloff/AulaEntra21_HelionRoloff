# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

num=int(input('informe um numero de 1 a 7 '))
if num ==1:
    print('segunda-feira')
elif num ==2:
    print('terça-feira')
elif num ==3:
    print('quarta-feira')
elif num ==4:
    print('quinta-feira')
elif num ==5:
    print('sexta-feira')
elif num ==6:
    print('sábado')
elif num ==7:
    print('domingo')
else:
    print('número inválido')