salario=input()
salario=float(salario)
if salario > 2000.00:
    reajuste=salario*0.04
    salariocomreajuste=salario+reajuste
    print(f'Novo salario: {salariocomreajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 4 %')
elif salario >= 1200.01 and salario <=2000.00:
    reajuste=salario*0.07
    salariocomreajuste=salario+reajuste
    print(f'Novo salario: {salariocomreajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 7 %')
elif salario >= 800.01 and salario <=1200.00:
    reajuste=salario*0.10
    salariocomreajuste=salario+reajuste
    print(f'Novo salario: {salariocomreajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 10 %')
elif salario >= 400.01 and salario <=800.00:
    reajuste=salario*0.12
    salariocomareajuste=salario+reajuste
    print(f'Novo salario: {salariocomreajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 12 %')
else:
    reajuste=salario*0.15
    salariocomreajuste=salario+reajuste
    print(f'Novo salario: {salariocomreajuste:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 15 %')

