#o programa vai sortear um número e a pessoa tentará acertar qual número é

import random

número = random.randint(1,5)

número_escolhido = int(input('Tente acertar o número de 1 a 5 que o programa gerou automaticamente: '))
if número_escolhido == número:
    print(f'O número que o programa sorteou foi {número}, você acertou!! ')

else: print(f'O número que o programa sorteou foi {número}, você errou!! ')
