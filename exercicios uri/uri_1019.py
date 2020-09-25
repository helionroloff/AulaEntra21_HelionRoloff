def main():
    segundos=int(input())
    segundos_restantes=segundos%3600
    segundos_horas=segundos//3600
    segundos_minutos=segundos_restantes//60
    segundos_restantes=segundos%60
    segundos_segundos=segundos_restantes//1
    print(f'{segundos_horas} : {segundos_minutos} : {segundos_segundos}')


	    
if __name__ == '__main__':
	main()
