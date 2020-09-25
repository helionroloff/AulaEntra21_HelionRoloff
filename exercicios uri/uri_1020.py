def main():
    idadeemdias=int(input())
    restodias=idadeemdias
    anos=restodias//365
    restodias=restodias%365
    meses=restodias//30
    restodias=restodias%30
    dias=restodias//1
    print(f'{anos} ano (s)')
    print(f'{meses} mes (es)')
    print(f'{dias} dia (s)')
	    
if __name__ == '__main__':
	main()
