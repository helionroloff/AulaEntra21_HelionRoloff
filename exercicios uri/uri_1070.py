x=int(input())
impares=0
valores=[]
if x%2==0:
    x=x+1
    impares=impares+1
    valores.append(x)
else:
    impares=impares+1
    valores.append(x)
for i in range(5):
    valores.append(x+2)
    x=x+2
for i in valores:
    print(i)
    