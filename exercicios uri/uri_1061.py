diainicio=int(input())
hora, minuto, seg=input().split()
horainicio=[]
horainicio.append(int(hora))
horainicio.append(int(minuto))
horainicio.append(int(seg))
print(horainicio)
diafim=int(input())
hora, minuto, seg=input().split()
horafim=[]
horafim.append(int(hora))
horafim.append(int(minuto))
horafim.append(int(seg))
dias=0
horas=0
minutos=0
segundos=0
restante=0
if diainicio==diafim:
    dias=0
else:
    dias=diafim-diainicio
print(dias)
if horainicio[0]==horafim[0]:
    horas=24
elif horainicio[0]<horafim[0]:
    horas=(horainicio[0]-horafim[0])
else:
    horas=24-(horainicio[0]+horafim[0])
print(horas)
