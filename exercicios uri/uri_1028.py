N=int(input())
for i in range(N):
    figuras=input().split()
    F1=int(figuras[0])
    F2=int(figuras[1])
    if (1 <= F1 <= 1000) and (1 <= F2 <= 1000):
        resto=1
        while resto != 0:
            resto = F1%F2
            F1 = F2
            F2 = resto
        print(F1)