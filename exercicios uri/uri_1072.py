N=int(input())
intervalo=[10,11,12,13,14,15,16,17,18,19,20]
valoresdentro=[]
valoresfora=[]
for i in range(N):
    valor=int(input())
    if valor in intervalo:
        valoresdentro.append(valor)
    else:
        valoresfora.append(valor)
print(f'{len(valoresdentro)}',"in")
print(f'{len(valoresfora)} out')
