#!/usr/bin/env python
# coding: utf-8

# FUNÇÕES E METODOS DE LISTAS
# 
# 

# **Funções para lista**
# 
# Estas funções ajudam no trabalho com as listas:
# 
# min(), max(), sum(), len()
# 
# min() ele retorna o menor valor de uma lista.
# Esta função funciona para números quanto para alfabeto.
# 
# 
# 



lista_numerica = [2,4,1,5,6,7,3]
lista_alfabetica = ['a','b','d','g']

print( min(lista_numerica) ) #o numero 1
print( min(lista_alfabetica) )#o caracter 'a'


# 
# 
# max() ele retorna o maior valor dentro de uma lisa.
# Esta função funciona para números quanto para alfabeto.
# 
# 

lista_numerica = [2,4,1,5,6,7,3]
lista_alfabetica = ['a','b','d','g']

print( max(lista_numerica) ) #o numero 7
print( max(lista_alfabetica) )#o caracter 'g'


# sum() faz a soma de todos os valores dentro da lista. Estes valore devem ser númericos para que esta função funcione.


lista_numerica = [2,4,1,5,6,7,3]

print( sum(lista_numerica) ) #o numero 28


# len() ele conta quantos itens tem um objeto como caracteres de uma string, bytes, tupla, lista, dicionário. 


lista_numerica = [2,4,1,5,6,7,3]
lista_alfabetica = ['a','b','d','g']

print( len(lista_alfabetica) ) #o resultado é 4 item
print( len(lista_numerica) ) #o resultado é 7 itens


# 
# 
# ---
# 
# 

# 
# **Metodos para Lista:**
# 
# Aqui vamos ver 90% dos metodos que podem ser usados em listas. Estes metodos ajudam a trabalhar, alterar, filtrar qualquer elemento de uma lista.
# 
# 
# 

# **.append()**
# 
# 
# Para adicionar itens em uma lista, usamos o metodo .append()
# .append(objeto)
# 
# Adiciona objeto no final da lista


lista = ['codigo', 'nome', 'idade', 'sexo']
lista.append('elemento')
print(lista)


# **.insert()**
# 
# insert(índice,objeto)
# 
# Insire o objeto na posição indicada (índice).
# 
# 


lista = [1,2,3,'a','b','c',3,'a',3]
lista.insert(4,'inserção na posição 4')
print(f'lista: {lista}')


# **.sort()**
# 
# sort(reverse=True/False)
# Ele ordena os valores de menor para maior. 
# 
# Caso o reverse estiver como True ele irá inverter do maior para menor. 
# 
# **Atenção**!
# 
# Os dados devem ser todos string ou numérico. Não pode haver mistura dos dois tipos na lista a ser ordenada.
# 
# ```
# >>> lista
# [1, 2, 3, 'a', 'inserção na posição 4', 'b', 'c', 3, 'a', 3]
# >>> lista.sort()
# Traceback (most recent call last):
#   File "<pyshell#178>", line 1, in <module>
#     lista.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'
# 
# 
# ```
# 
# 
 

lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]

# Ordenando a lista!

lista.sort()
print(f'lista ordenada: {lista}')
print()

# Ordenando a lista reversamente!

lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
lista.sort(reverse=True)
print(f'lista ordenada inversamente: {lista}')


# **.reverse()**
# 
# reverse()
# 
# Ele reverte a ordem da lista. Ele não ordena, só altera a posição para a 
# posição inversa.
# 
# 

lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
print(f'lista: {lista}')
lista.reverse()
print(f'lista revertida: {lista}')

lista.reverse()
print(f'lista re-revertida: {lista}')


# **.pop()**
# 
# pop(indice)
# 
# Remove o objeto na posição indicada e retorna o valor removido.
# 
# Caso não indique o indice do arquivo o .pop() irá remover o ultimo item 
# da lista. 
# 
# Note que o .pop() retorna o valor removido. O mesmo pode ser salvo em uma variável.
# 
# 
# 
# 


lista = [8,3,4,9,4,5,3,1,8,2,4,10,564,45,450]
print(f'lista: {lista}')
print(f'lista.pop(): {lista.pop()}')
print(f'lista: {lista}')

variavel = lista.pop()
print(f'variavel: {variavel}')
print()


>>> lista = [8, 3, 4, 9, 4, 5, 3, 1, 8, 2, 4, 10, 564]

# Agora vamos remover o item na terceira posição:

print(f'lista.pop(): {lista.pop(3)}')
print(f'lista: {lista}')


# **.remove()**
# 
# remove(valor)
# 
# remove a primeira ocorrência do valor digitado.
# 
# Neste caso o item removido não é retornado para o programa.


lista = [8, 3, 4, 4, 5, 3, 1, 8, 2, 4, 10, 564]
print(f'lista: {lista}')
print()
lista.remove(3)
print(f'lista: {lista}')




