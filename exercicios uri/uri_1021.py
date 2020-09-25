def main():
    N=float(input())
    troco=N
    cem=int(troco//100)
    troco=troco%100
    cinquenta=int(troco//50)
    troco=troco%50
    vinte=int(troco//20)
    troco=troco%20
    dez=int(troco//10)
    troco=troco%10
    cinco=int(troco//5)
    troco=troco%5
    dois=int(troco//2)
    troco=troco%2
    moedaum=int(troco//1)
    troco=troco%1*100
    moedacinquenta=int(troco//50)
    troco=troco%50
    moedavintecinco=int(troco//25)
    troco=troco%25
    moedadez=int(troco//10)
    troco=troco%10
    moedacinco=int(troco//5)
    troco=troco%5
    moedazeroum=int(troco//1)
    troco=troco%1
    print('NOTAS:')
    print(f'{cem} nota(s) de R$ 100.00')
    print(f'{cinquenta} nota(s) de R$ 50.00')
    print(f'{vinte} nota(s) de R$ 20.00')
    print(f'{dez} nota(s) de R$ 10.00')
    print(f'{cinco} nota(s) de R$ 5.00')
    print(f'{dois} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{moedaum} moeda(s) de R$ 1.00')
    print(f'{moedacinquenta} moeda(s) de R$ 0.50')
    print(f'{moedavintecinco} moeda(s) de R$ 0.25')
    print(f'{moedadez} moeda(s) de R$ 0.10')
    print(f'{moedacinco} moeda(s) de R$ 0.05')
    print(f'{moedazeroum} moeda(s) de R$ 0.01')

if __name__ == '__main__':
	main()
