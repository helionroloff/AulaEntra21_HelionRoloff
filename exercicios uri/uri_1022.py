teste=int(input())
for i in range(teste):
    entradas=input().split()
    N1=int(entradas[0])
    D1=int(entradas[2])
    OP= entradas[3]
    N2=int(entradas[4])
    D2=int(entradas[6])
    if ((0 < N1 < 1000) and (0 < N2 < 1000) and (0 < D1 < 1000) and (0 < D2 < 1000)):
        if OP == "+":
            numeradorsoma = (N1*D2 + N2*D1)
            denominadorsoma = (D1*D2)
            a = numeradorsoma
            b = denominadorsoma
            resto = 1
            while resto != 0:
                resto = a%b
                a = b
                b = resto
            mmc = a
            print(f'{numeradorsoma}/{denominadorsoma} = {numeradorsoma//mmc}/{denominadorsoma//mmc}')
        elif OP == '-':
            numeradorsubtracao = (N1*D2 - N2*D1)
            denominadorsubtracao = (D1*D2)
            a = numeradorsubtracao
            b = denominadorsubtracao
            resto = 1
            while resto != 0:
                resto = a%b
                a = b
                b = resto
            mmc = a
            print(f'{numeradorsubtracao}/{denominadorsubtracao} = {numeradorsubtracao//mmc}/{denominadorsubtracao//mmc}')
        elif OP =='*':
            numeradormultiplicacao = (N1*N2)
            denominadormultiplicacao = (D1*D2)
            a = numeradormultiplicacao
            b = denominadormultiplicacao
            resto = 1
            while resto != 0:
                resto = a%b
                a = b
                b = resto
            mmc = a
            print(f'{numeradormultiplicacao}/{denominadormultiplicacao} = {numeradormultiplicacao//a}/{denominadormultiplicacao//a}')
        elif OP =='/':
            numeradordivisao = (N1*D2)
            denominadordivisao = (N2*D1)
            a = numeradordivisao
            b = denominadordivisao
            resto = 1
            while resto != 0:
                resto = a%b
                a = b
                b = resto
            mmc = a
            print(f'{numeradordivisao}/{denominadordivisao} = {numeradordivisao//mmc}/{denominadordivisao//mmc}')
            