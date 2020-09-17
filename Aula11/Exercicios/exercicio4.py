#"""Exercício 4

#(use o conhecimento que foi passado no curso)

#Crie um programa com um menu interativo:

#-----
#Cadastro de pessoas v1.0

#A) Cadastrar Pessoa
#B) Ver todos os nomes cadastrados:
#C) Ver cadastro pelo nome:
#D) Apagar um cadastro pelo nome:
#S) Sair

#-----



#Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
#Para B: Mostre todos os nomes dos clientes (só os nomes)
#Para C: Digite o nome do cliente e mostre todos os dados dele.
#Para D: Digite o nome do cliente e o apague do cadastro
#Para S: Mostre uma mensagem de despedida e termine o programa
#Para qualquer outro valor: Mostre "Opção invalida"
#"""
escolha=''
nomes=[]
idades=[]
sexos=[]
telefones=[]
while escolha!='S':
    print('''
    Cadastro de pessoas v1.0

    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair
    ''')
    escolha=input('escolha a opção: ')
    escolha=escolha.upper()
    escolha=escolha.strip()
    if escolha=='A':
        nome=input('diga o nome da pessoa que você deseja cadastrar: ')
        nome=nome.strip()
        if nome=="":
            print('NOME EM BRANCO')
        else:
            idade=input('diga a idade da pessoa que você deseja cadastrar: ')
            idade=idade.strip()
            if idade=="":
                print('IDADE EM BRANCO')
            else:
                idade=int(idade)
                sexo=input('diga o sexo da pessoa que você deseja cadastrar: F-M:  ')
                sexo=sexo.upper()
                if sexo=="F":
                    sexo='F'
                    telefone=input('diga o telefone da pessoa que você deseja cadastrar: ')
                    telefone=telefone.strip()
                    if telefone=="":
                        print('TELEFONE EM BRANCO')
                    else:
                        print('cadastro realizado com sucesso')
                        nomes.append(nome)
                        idades.append(idade)
                        sexos.append(sexo)
                        telefones.append(telefone)
                elif sexo=="M":
                    telefone=input('diga o telefone da pessoa que você deseja cadastrar: ')
                    telefone=telefone.strip()
                    if telefone=="":
                        print('TELEFONE EM BRANCO')
                    else:
                        print('cadastro realizado com sucesso')
                        nomes.append(nome)
                        idades.append(idade)
                        sexos.append(sexo)
                        telefones.append(telefone)
                else:
                    print('SEXO INVALIDO')        
    elif escolha=='B':
        print('os nomes dos clientes cadastrados são: ')
        for i in nomes:
            print(i)
    elif escolha=='C':
        consultar=input('informe o cliente que deseja consultar os dados: ')
        posicao=int(nomes.index(consultar))
        print(f'''
        nome: {nomes[posicao]}
        idade: {idades[posicao]}
        sexo: {sexos[posicao]}
        telefones: {telefones[posicao]}
        ''')
    elif escolha=='D':
        apagar=input('informe o cliente que deseja apagar os dados: ')
        posicao=int(nomes.index(apagar))
        confirmacao=input('apagar este contato? S-N')
        confirmacao=confirmacao.upper()
        if confirmacao=='S':
            nomes.pop(posicao)
            idades.pop(posicao)
            sexos.pop(posicao)
            telefones.pop(posicao)
            print('dados apagados')
    elif escolha=='S':
        print('PROGRAMA ENCERRADO')
    else:
        print('ESCOLHA INVÁLIDA')

        