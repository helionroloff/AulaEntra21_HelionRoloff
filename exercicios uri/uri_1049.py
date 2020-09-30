vertebra=input('vertebrado ou invertebrado: ')
classes=input('informe a classe: ')
alimentacao=input('informe a alimentacao')

if vertebra=='vertebrado' and classes == 'ave' and alimentacao == 'carnivoro':
    print('aguia')
elif vertebra=='vertebrado' and classes == 'ave' and alimentacao == 'onivoro':
    print('pomba')
elif vertebra=='vertebrado' and classes == 'mamifero' and alimentacao == 'onivoro':
    print('homem')
elif vertebra=='vertebrado' and classes == 'mamifero' and alimentacao == 'herbivoro':
    print('vaca')
elif vertebra=='invertebrado' and classes == 'inseto' and alimentacao == 'hematofago':
    print('pulga')
elif vertebra=='invertebrado' and classes == 'inseto' and alimentacao == 'herbivoro':
    print('lagarta')
elif vertebra=='invertebrado' and classes == 'anelideo' and alimentacao == 'hematofago':
    print('sanguessuga')
elif vertebra=='invertebrado' and classes == 'anelideo' and alimentacao == 'onivoro':
    print('minhoca')
