# Exercicio 19
# Faça um programa para calcular a fórmula do bhaskara para equação de segundo grau: ax²+bx+c
# 
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta for igual a zero, use esta fórmula "x=-b/(2*a)" e mostre o valor de x
# 
# Se delta for maior que zero, então use estas 2 fórmulas "x =(-b+(delta**(1/2)))/(2*a)" e "x2=(-b-(delta**(1/2)))/(2*a)"
# e mostre o os valores de x1 e x2  
#     
#    
# ________________
# Nota: 
# Para testar se seu programa está certo use estes valores para a, b e c
# delta negativo a=1, b=1, c=1
# delta zero a=1, b=2, c=1
# delta positivo a=1, b=4, c=1

a=float(input('informe o valor a '))
b=float(input('informe o valor b '))
c=float(input('informe o valor c '))



delta=(b**2)-(4*a*c)

if delta < 0:
    print('Delta negativo! Equação não pode ser resolvida!')
elif delta == 0:
    x=-b/(2*a)
    print('o valor de x é',x)
    print((a*x**2)+(b*x)+c)
  
    
elif delta > 0:
    x =(-b+(delta**(1/2)))/(2*a)
    x2=(-b-(delta**(1/2)))/(2*a)

    print('o valor de x é',x,'e o valor de x2 é',x2)


