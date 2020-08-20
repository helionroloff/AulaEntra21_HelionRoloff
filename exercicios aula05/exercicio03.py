# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# 
# Caso contrário deve aparecer a mensagem "Entrada Negada!"
idade=int(input('informe sua idade '))
if idade >= 18:
    print('Entrada permitida')
else:
    print('Entrada negada')