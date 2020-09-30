positivo=[]
positivos=0
for i in range(6):
    numero=float(input())
    if numero > 0:
        positivos=positivos+1
        positivo.append(numero)
media=(sum(positivo)/len(positivo))
print(f'{positivos} valores positivos')
print(f'{media:.1f}')

