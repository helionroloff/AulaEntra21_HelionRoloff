X=int(input())
Y=int(input())
numeros=[Y,X]
numeros.sort()
Y=numeros[1]
X=numeros[0]
impares=[]
for i in range(X+1,Y):
    if i%2==1:
        impares.append(i)
print(sum(impares))
