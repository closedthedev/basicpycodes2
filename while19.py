#praticando while, agora com par ou impar

import random 

print('JOGO DO PAR OU ÍMPAR, SE VOCÊ PERDER O PROGRAMA SERÁ ENCERRADO AUTOMATICAMENTE')
números = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

while True:
    
    número_selecinado = random.choice(números)

    n = int(input('Digite um número:  '))
    parouimpar = str(input('PAR OU ÍMPAR? P / I  ')) .strip() .upper()

    soma = n + número_selecinado
    if soma % 2 == 0:
        resultado = 'par'
    else: resultado = 'ímpar'

    if resultado == 'par' and parouimpar == 'P':
        print(f'Você escolheu {n} e a máquina escolheu {número_selecinado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você ganhou!')

    elif  resultado == 'ímpar' and parouimpar == 'I':
        print(f'Você escolheu {n} e a máquina escolheu {número_selecinado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você ganhou!')

    elif resultado == 'ímpar' and parouimpar == 'P':
        print(f'Você escolheu {n} e a máquina escolheu {número_selecinado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você perdeu!')
        break

    elif resultado == 'par' and parouimpar == 'I':
        print(f'Você escolheu {n} e a máquina escolheu {número_selecinado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você perdeu!')
        break