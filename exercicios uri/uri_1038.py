precos=[4.00,4.50,5.00,2.00,1.50]
codigo,quantidade=input().split()
codigo=int(codigo)
quantidade=int(quantidade)
codigo=precos[codigo-1]
total=codigo*quantidade
print(f'Total: R$ {total:.2f}')
