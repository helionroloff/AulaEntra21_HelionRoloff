#"""Execicios 04
#Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
n = float(input('Digite o primeiro lado :'))
n2 = float(input('Digite o do segundo lado :'))
n3 = float(input('Digite o do terceiro lado :'))
if n <= n2 + n3 and n2 <= n+n3 and n3 <= n + n2:
    print('Há possibilidade de formar um triangulo ')
    if n== n2 == n3:
        print('Equilatero')
    elif n != n2 and n2 != n3 and n3 != n:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Não a possibilidade de formar um triangulo!')