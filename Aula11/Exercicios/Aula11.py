while True:
    opcao=str(input('''
    1- inserir nome
    2- inserir idade
    s- sair
    
    ''')).strip().upper()
    if opcao == '1':
        cont=''
        while cont=='S':
            nome=input('insira um nome: ')
            cont=input('continuar? S-N? ').upper()
            if cont=='S':
                continue
            else:
                break
    elif opcao == '2':
        cont=''
        while cont=='S':
            idade=int(input('insira a idade: '))
            conti=input('deseja continuar? S-N: ').upper()
            if conti == 'S':
                continue
            else:
                break
    elif opcao=='S':
        print('TCHAU BABAU')
        break
    