#um programa que irá comparar dois valores que o usuário vai passar

valor1 = int(input('Digite um número inteiro qualquer: '))
valor2 = int(input('Digite outro número inteiro qualquer: '))

if valor1 > valor2:
    print(f'Você escolheu os números {valor1} e {valor2}. O número {valor1} é maior. ')

elif valor2 > valor1:
    print(f'Você escolheu os números {valor1} e {valor2}. O número {valor2} é maior. ')

else: print(f'Você escolheu os números {valor1} e {valor2}. Eles são iguais.')
             
        