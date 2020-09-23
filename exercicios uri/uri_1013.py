a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
MaiorAB=(a+b+abs(a-b))/2
MaiorABC=(MaiorAB+c+abs(MaiorAB-c))/2
MaiorABC=int(MaiorABC)
print(f'{MaiorABC} eh o maior')
