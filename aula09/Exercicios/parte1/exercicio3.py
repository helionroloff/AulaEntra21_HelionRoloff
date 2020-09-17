
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
#sem utilizar validação pensei em colocar o input direto do append para diminuir
#a quantidade de linhas, mas não sei fazer validação assim


#notas=[]
#for i in range(1,11):

 #   notas.append(float(input(f'informe a nota {i}: ')))



notas=[]
for i in range(1,11):
    nota=float(input(f'informe a nota {i}: '))
    if nota >=0 and nota <=10:
        notas.append(nota)
    else:
        print('nota inválida')

media=sum(notas)/len(notas)

if media < 5.5:
    print(f'Média {media} Reprovado')
elif media < 7:
    print(f'Média {media} Recuperação')
else:
    print(f'Média {media} Aprovado')

print('*****','FIM','*****')

    