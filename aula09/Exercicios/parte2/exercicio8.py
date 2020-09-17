"""Exercicio 08

Faça um programa que pegue a lista e calcule a seguinte formula: 32x+125

Com o resultado desta formula mostre sómente os resultados maiores que 550. Para os resultados menores que 550 mostre "número invalido!"

lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
"""
lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
for i in lista:
    num=32*i+125
    if num>=550:
        print(f'o número {i} aplicado a formula 32x+125 é {num}, por ser igual ou maior a 550 é válido')
    else:
        print(f'número inválido')