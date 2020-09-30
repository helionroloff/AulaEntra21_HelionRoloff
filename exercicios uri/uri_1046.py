horainicio, horatermino = map (int, input().split())
if horainicio == horatermino:
    print('O JOGO DUROU 24 HORA(S)')
elif horainicio>horatermino:
    tempo = 24-horainicio+horatermino
    print(f'O JOGO DUROU {tempo} HORA(S)')
else: 
    tempo = horatermino-horainicio
    print(f'O JOGO DUROU {tempo} HORA(S)')
