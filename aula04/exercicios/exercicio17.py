# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 
r=float(input('informe a medida do raio que deseja calcular'))
pi=3.14
a=pi*(r**2)
print('a área do círculo é',a)