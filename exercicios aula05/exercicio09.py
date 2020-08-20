# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
# 
num1=int(input('informe o primeiro número'))
num2=int(input('informe o segundo número'))
num3=int(input('informe o terceiro número'))
if num1>num2:
    if num1>num3:
        maior=num1
        if num2>num3:
            meio=num2
            menor=num3
        else:
            meio=num3
            menor=num2
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')
if num1>num2:
    if num1>num3:
        maior=num1
        if num2<num3:
            meio=num3
            menor=num2
        else:
            meio=num2
            menor=num3
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')
if num2>num1:
    if num2>num3:
        maior=num2
        if num1>num3:
            meio=num1
            menor=num3
        else:
            meio=num3
            menor=num1
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')
if num2>num1:
    if num2>num3:
        maior=num2
        if num1<num3:
            meio=num3
            menor=num1
        else:
            meio=num1
            menor=num3
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')
if num3>num1:
    if num3>num2:
        maior=num3
        if num1>num2:
            meio=num1
            menor=num2
        else:
            meio=num2
            menor=num1
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')
if num3>num1:
    if num3>num2:
        maior=num3
        if num1<num2:
            meio=num2
            menor=num1
        else:
            meio=num1
            menor=num2
            print(f'numero menor {menor} numero do meio {meio} e numero maior {maior}')

