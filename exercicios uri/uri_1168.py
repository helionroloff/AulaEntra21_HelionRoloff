leds=[]
numero=list(input())
for i in numero:
    if i=='0':
        leds.append(6)
    elif i=='1':
        leds.append(2)
    elif i=='2':
        leds.append(5)
    elif i=='3':
        leds.append(5)
    elif i=='4':
        leds.append(4)
    elif i=='5':
        leds.append(5)
    elif i=='6':
        leds.append(6)
    elif i=='7':
        leds.append(3)
    elif i=='8':
        leds.append(7)
    elif i=='9':
        leds.append(6)
print(f'{sum(leds)} leds')
