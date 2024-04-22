#praticando while, dessa vez o usuário tentará acertar o número de 1 a 10 que o programa irá escolher aleatoriamente e irá mostrar quantas tentativas o usuário teve.

import random

tentativas = 0
número = random.randint(1 , 10)
n = 0

while n != número:
    n = int(input('Digite um número de 1 a 10: '))
    tentativas += 1

print(f'O programa escolheu aleatoriamente o número {número} e você chutou {tentativas} vezes para acertar.')