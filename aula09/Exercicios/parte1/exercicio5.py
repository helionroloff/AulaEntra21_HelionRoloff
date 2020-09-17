"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda 
separadaemnte e depois mostre a média e o valor total vendido no dia.
"""

qnt=int(input('quantidade de vendas do dia: '))
if qnt >=0:
    valores=[]
    for i in range(qnt):
        valor=float(input(f'informe o valor da venda {i+1} = R$:'))
        if valor>0:
            valores.append(valor)
        else:
            print('valor inválido')
else:
    print('quantidade inválida')

media=sum(valores)/len(valores)
total=sum(valores)
print(f'''
Valor total de vendas: {total:.2f} reais.
Média de valor por venda: {media:.2f} reais.
''')
print('***FIM***')