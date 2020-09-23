a, b, c=input().split()
a=float(a)
b=float(b)
c=float(c)
pi=3.14159
areatriangulo=(a*c)/2
areacirculo=pi*c**2
areatrapezio=((a+b)*c)/2
areaquadrado=b*b
arearetangulo=a*b
print(f'TRIANGULO: {areatriangulo:.3f}')
print(f'CIRCULO: {areacirculo:.3f}')
print(f'TRAPEZIO: {areatrapezio:.3f}')
print(f'QUADRADO: {areaquadrado:.3f}')
print(f'RETANGULO: {arearetangulo:.3f}')
