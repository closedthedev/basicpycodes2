#praticando while, agora com par ou impar

import random 

print('JOGO DO PAR OU ÍMPAR, SE VOCÊ PERDER O PROGRAMA SERÁ ENCERRADO AUTOMATICAMENTE')
números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vit = 0
while True:
    número_selecionado = random.choice(números)

    n = int(input('Digite um número: '))
    par_ou_impar = input('PAR OU ÍMPAR? P / I: ').strip().upper()

    soma = n + número_selecionado
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'

   

    if (resultado == 'PAR' and par_ou_impar == 'P') or (resultado == 'ÍMPAR' and par_ou_impar == 'I'):
         vit += 1
         print(f'Você escolheu {n} e a máquina escolheu {número_selecionado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você ganhou. Você está numa sequência de {vit} vitórias!')
    else:

        print(f'Você escolheu {n} e a máquina escolheu {número_selecionado}, a soma deles é {soma}. Resultando em um número {resultado}. Portanto, você perdeu!')
        break