numero1,numero2,numero3=input().split()
n1=int(numero1)
n2=int(numero2)
n3=int(numero3)
listaoriginal=[]
listaoriginal.append(n1)
listaoriginal.append(n2)
listaoriginal.append(n3)
lista=[]
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.sort()
for i in lista:
    print(i)
print('')
for i in listaoriginal:
    print(i)
    