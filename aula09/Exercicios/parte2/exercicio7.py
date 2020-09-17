"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""

for i in range(10):
    idade=int(input(f'informe a idade: '))
    if idade >=0:
        if idade<13:
          print('Piscina de bolinhas liberada')  
        elif idade >=13 and idade <16:
            print('Ingressos para fliperama liberado')
        elif idade>=16 and idade <18:
            print('Ingressos de cinema liberado')
        else:
            print('Ingressos da Rave liberado!')
    else:
        print('idade inválida')