N=int(input())
pares=[]
for i in range(1,N+1):
    if i%2==0:
        pares.append(i)
for i in pares:
    print(f'{i}^2 = {i**2}')
    