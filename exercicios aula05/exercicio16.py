# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
print("""
combustiveis disponíveis
(g) gasolina 
(a) alcool
(d) diesel
""")
combustivel=input('informe o combustível g, a ou d ')
litros=float(input("Informe quantos litros deseja "))

if combustivel == 'g' and litros <= 20:
    print('o combustível escolhido é gasolina, foram abastecidos',litros,'litros, e o descondo é de 0%')
elif combustivel == 'g' and litros > 20:
      print('o combustível escolhido é gasolina, foram abastecidos',litros,'litros, e o descondo é de 10%')
elif combustivel == 'd' and litros <= 10:
    print('o combustível escolhido é Diesel, foram abastecidos',litros,'litros, e o descondo é de 1.5%')
elif combustivel == 'd' and litros > 10:
      print('o combustível escolhido é Diesel, foram abastecidos',litros,'litros, e o descondo é de 5%')
elif combustivel == 'a' and litros <= 10:
    print('o combustível escolhido é alcool, foram abastecidos',litros,'litros, e o descondo é de 5%')
elif combustivel == 'a' and litros > 10:
      print('o combustível escolhido é alcool, foram abastecidos',litros,'litros, e o descondo é de 10%')