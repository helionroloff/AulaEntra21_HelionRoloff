# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00] 

#sem declarar variável
print('+='*40)
print(f'A média de vendas de Armando é {sum(vendas_armando)/len(vendas_armando):.2f} reais')
print(f'Armando fez um total de {len(vendas_armando):.2f} vendas e um total de {sum(vendas_armando):.2f} reais')

print(f'A média de vendas de Eduardo é {sum(vendas_eduardo)/len(vendas_eduardo):.2f} reais')
print(f'Eduardo fez um total de {len(vendas_eduardo):.2f} vendas e um total de {sum(vendas_eduardo):.2f} reais')

print(f'A média de vendas de Paulo é {sum(vendas_paulo)/len(vendas_paulo):.2f} reais')
print(f'Eduardo fez um total de {len(vendas_paulo):.2f} vendas e um total de {sum(vendas_paulo):.2f} reais')

print('=+'*40)

#declarando variável 

media_armando=sum(vendas_armando)/len(vendas_armando)
total_armando=sum(vendas_armando)
quantidade_armando=int(len(vendas_armando))
print(f'A média de vendas de Armando é {media_armando:.2f} reais')
print(f'Armando fez um total de {quantidade_armando} vendas e um total de {total_armando:.2f} reais')

salario_comissão_armando=0
if total_armando <=1000.00 :
    salario_comissão_armando=total_armando+total_armando*(1/100)
elif total_armando <=2500.00:
    salario_comissão_armando=total_armando+total_armando*(1.5/100)
elif total_armando <=5000.00:
    salario_comissão_armando=total_armando+total_armando*(2/100)
else:
    salario_comissão_armando=total_armando+total_armando*(3/100)
print(f'o salario de Armando com a comissão inclusa é de {salario_comissão_armando:.2f}')

print('=+'*40)

media_eduardo=sum(vendas_eduardo)/len(vendas_eduardo)
total_eduardo=sum(vendas_eduardo)
quantidade_eduardo=int(len(vendas_eduardo))
print(f'A média de vendas de Eduardo é {media_eduardo:.2f} reais')
print(f'Eduardo fez um total de {quantidade_eduardo} vendas e um total de {total_eduardo:.2f} reais')

salario_comissão_eduardo=0
if total_eduardo <= 1000.00:
    salario_comissão_eduardo=total_eduardo+total_eduardo*(1/100)
elif total_eduardo <= 2500.00:
    salario_comissão_eduardo=total_eduardo+total_eduardo*(1.5/100)
elif total_eduardo <= 5000.00:
    salario_comissão_eduardo=total_eduardo+total_eduardo*(2/100)
else:
    salario_comissão_eduardo=total_eduardo+total_eduardo*(3/100)
print(f'o salario de Eduardo com a comissão inclusa é de {salario_comissão_eduardo:.2f}')

print('+='*40)

media_paulo=sum(vendas_paulo)/len(vendas_paulo)
total_paulo=sum(vendas_paulo)
quantidade_paulo=int(len(vendas_paulo))
print(f'A média de vendas de Paulo é {media_paulo:.2f} reais')
print(f'Paulo fez um total de {quantidade_paulo} vendas e um total de {total_paulo:.2f} reais')
salario_comissão_paulo=0
if total_paulo <= 1000.00:
    salario_comissão_paulo=total_paulo+total_paulo*(1/100)
elif total_paulo <= 2500.00:
    salario_comissão_paulo=total_paulo+total_paulo*(1.5/100)
elif total_paulo <= 5000.00:
    salario_comissão_paulo=total_paulo+total_paulo*(2/100)
else:
    salario_comissão_paulo=total_paulo+total_paulo*(3/100)
print(f'o salario de Paulo com a comissão inclusa é de {salario_comissão_paulo:.2f}')

print('+='*40)