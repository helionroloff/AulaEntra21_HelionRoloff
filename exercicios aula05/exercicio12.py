# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

num1=float(input('informe o primeiro número '))
num2=float(input('informe o segundo número '))

print("""
++++++Escolha uma opção de operação++++++
1-adição
2-subtração
3-multiplicação
4-divisão
5-expoente
+++++++++++++++++++++++++++++++++++++++++
""")
op=int(input("""
informe o número da opção desejada
"""))

if op ==1:
    print('a soma dos números é',num1+num2)
elif op ==2:
    print('a subtração dos números é',num1-num2)
elif op ==3:
    print('a multiplicação dos números é',num1*num2)
elif op ==4:
    print('a divisão dos números é',num1/num2)
elif op ==5:
    print('o expoente entre os números é',num1**num2)


