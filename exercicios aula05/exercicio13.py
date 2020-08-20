# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome=input('nome do cliente ')
idade=int(input('idade do cliente '))
endereco=str(input('informe o endereço '))
email=str(input('informe seu email '))
telefone=str(input('informe seu telefone '))

print("""

Selecione a opção desejada
1 - Dados
2 - Endereço
3 - Contato

""")

op=int(input('informe o número desejado '))
if op==1:
    print('o nome do cliente é',nome,'e a idade é',idade)
elif op==2:
    print('o nome do cliente é',nome,'e o endereço é',endereco)
elif op==3:
    print('o nome do cliente é',nome,'o telefone para contato é',telefone,'e seu email para contato é',email)    
else:
    print('Opção invalida')

