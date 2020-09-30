N=int(input())
casos=[]
for i in range(N):
    casos.append(input())
for caso in casos:
    F1 , F2 = caso.split()
    F1 = int(F1)
    F2 = int(F2)
    resto=1
    while resto != 0:
        resto = F1%F2
        F1 = F2
        F2 = resto
    print(F1)
