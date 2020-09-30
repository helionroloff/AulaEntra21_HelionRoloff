fibonati=[0,1]
fiba=fibonati[0]
fibb=fibonati[1]

numero=int(input('qual valor fibonati voce quer chegar? :'))
caso=(numero-1)
for i in range(caso):
    fibc=fiba+fibb
    fibonati.append(fibc)
    fiba=fibb
    fibb=fibc
print(f'fib({numero}) = calls = {fibb}')

n=int(input('informe o quantidade de testes: '))
casos=[]

for i in range(n):
    caso=input('informe a fib: ')
    casos.append(caso)

for i in casos:
    if i == 0:
        fib = [0]
    elif i == 1:
        fib = [1]
    else:


recursivos=[]
for i in range(numero+1):
    if i == 0:
        recursivo=i
        recursivos.append(recursivo)
    elif i == 1:
        recursivo=i
        recursivos.append(recursivo)
    else:
        recursivo=(i-1)+(i-2)
        recursivos.append(recursivo)
#for i in recursivos:
#    print (i)
