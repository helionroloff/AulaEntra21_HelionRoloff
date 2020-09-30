A, B, C = map(float,input().split())
lados=[A, B, C]
lados.sort()
lados.reverse()
A=lados[0]
B=lados[1]
C=lados[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    
    if A==B or A==C or B==C:
        
        if A==B and B==C:
            print("TRIANGULO EQUILATERO")

        else:
            print("TRIANGULO ISOSCELES")
