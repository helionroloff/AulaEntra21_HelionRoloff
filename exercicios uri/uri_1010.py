codigo1,numero_pecas1,valor_peca1=str(input()).split()
codigo2,numero_pecas2,valor_peca2=str(input()).split()
valor=(int(numero_pecas1)*float(valor_peca1))+(int(numero_pecas2)*float(valor_peca2))
print(f'VALOR A PAGAR: R$ {valor:.2f}')
