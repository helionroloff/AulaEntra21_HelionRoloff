#"""Execicios 03
#Escreva um programa que contenha um menu com 4 opções:
#A) soma
#B) média
#C) divisão
#D) Sair
#As opções podem ser escolhidas com as letras maiusculas ou minusculas.
#Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.
#Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.
#Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"
#Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"

print("""Escolha um opção:
A) soma
B) média
C) divisão
D) Sair""")
opcao=str(input('Informe a opção desejada: '))

if opcao == 'a' or opcao == 'A':
    num1=int(input('informe um número'))
    num2=int(input('informe outro número número'))
    print(f'a soma dos dois números é{num1+num2}')
elif opcao == 'b' or opcao == 'B':
    num1=int(input('informe o primeiro número'))
    num2=int(input('informe o segundo número'))
    num3=int(input('informe o terceiro número'))
    num4=int(input('informe o quarto número'))
    media=(num1+num2+num3+num4)/4
    print(f'a média é {media}')
elif opcao == 'c' or opcao == 'C':
    num1=int(input('informe o primeiro número'))
    num2=int(input('informe o número pelo qual quer dividir'))
    div=num1/num2
    print(f'o valor da divisão é {div}')
elif opcao == 'd' or opcao == 'D':
    print('Muito Obrigado e Volte sempre!')
else:
    print('Opção invalida')