#Execicios 01
#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%
valor_total=float(input('informe o valor total '))

if valor_total >= 0.00 and valor_total <= 30000.00:
    print('você não possui comissão')
elif valor_total > 30000.00 and valor_total <= 50000.00:
    porcentagem=1.5
    comissao=valor_total*(porcentagem/100)
    print(f'o valor da comissão em cima de {valor_total:.2f} é de {porcentagem}%, resultando em {comissao:.2f}')
elif valor_total > 50000.00 and valor_total <= 100000.00:
    porcentagem=2.5
    comissao=valor_total*(porcentagem/100)
    print(f'o valor da comissão em cima de {valor_total:.2f} é de {porcentagem}%, resultando em {comissao:.2f}')
else:
    porcentagem=3.5
    comissao=valor_total*(porcentagem/100)
    print(f'o valor da comissão em cima de {valor_total:.2f} é de {porcentagem}%, resultando em {comissao:.2f}')
    

