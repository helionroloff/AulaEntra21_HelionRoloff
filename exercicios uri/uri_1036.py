a, b, c=input().split()
a=float(a)
b=float(b)
c=float(c)
if a ==0:
    print('Impossivel calcular')
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print('Impossivel calcular')
    else:
        raizum=(-b+(delta**(1/2)))/(2*a)
        raizdois=(-b-(delta**(1/2)))/(2*a)
        print(f'R1 = {raizum:.5f}')
        print(f'R2 = {raizdois:.5f}')
    