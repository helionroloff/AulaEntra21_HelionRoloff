# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
nota1=float(input('nota 1 '))
nota2=float(input('nota 2 '))
nota3=float(input('nota 3 '))
nota4=float(input('nota 4 '))

media=(nota1+nota2+nota3+nota4)/4
print(media)

if media == 10:
    print('Aprovado com louvor!')
elif media >= 7:
    print('Aprovado')
else:
    print('reprovado')