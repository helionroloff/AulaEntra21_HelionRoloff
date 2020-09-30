pares=0
impares=0
positivo=0
negativo=0
for i in range(5):
    numero=int(input())
    if numero%2==0:
        pares=pares+1
    if numero%2==1:
        impares=impares+1
    if numero > 0:
        positivo=positivo+1
    if numero < 0:
        negativo=negativo+1
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
