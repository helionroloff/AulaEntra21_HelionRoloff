#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

dinheiro_emprestado=float(input('qual a quantidade de dinheiro emprestada?'))
taxa_juros=float(input('informe a taxa de juros'))
tempo_emprestimo=int(input('quantos meses de tempo de empréstimo?'))
valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
print('o valor a receber é',valor_receber)