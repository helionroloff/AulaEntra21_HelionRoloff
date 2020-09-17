
"""----

 Uso de for com listas. 

----

Para poder usar o for com listas, você deve substituir o range() pelo nome da lista.

A cada interação (loop) do for, a variável i ficará com um elemento da lista.
"""

# Exemplo1: 
# Faça um programa que de o bom dia para cada convidade da lista.

convidados = ["Paulo", "Pedro", "João", "Guilherme","Fábio"]

for i in convidados:
    print(f"Bom dia {i}") # Note que a variável i recebe elementos da lista

# Exemplo2: 
# Faça um programa que solicite 3 nomes e depois mostre os nomes um em cada linha

nomes_cadastro = []
for i in range(3): # Parte do código responsável pela captura dos nomes
    nome = input("Digite o nome: ")
    nomes_cadastro.append(nome)

for i in nomes_cadastro: # Parde do código responsável pela apresentação dos nomes
    print(i)

# Exemplo
# Com a lista de idades, mostre a idade e se pode entrar na festa.
# A entrada é permitida para maiores de 16 anos.

idades = [13, 15, 19, 14, 16, 17, 17, 15, 18, 20, 12, 10, 15, 16, 16, 23]

for i in idades:
    if i >= 16:
        print(f"Idade: {i} - Entrada permitida!")
    else:
        print(f"Idade: {i} - Entrada negada!")