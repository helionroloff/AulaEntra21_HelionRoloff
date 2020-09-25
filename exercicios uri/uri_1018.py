N=int(input())
troco=N
cem=troco//100
troco=troco%100
cinquenta=troco//50
troco=troco%50
vinte=troco//20
troco=troco%20
dez=troco//10
troco=troco%10
cinco=troco//5
troco=troco%5
dois=troco//2
troco=troco%2
um=troco//1
troco=troco%1

print(N)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
