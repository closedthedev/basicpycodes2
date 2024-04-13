#o programa vai sortear um número e a pessoa tentará acertar qual número é

import random

número = random.randint(0,5)

número_escolhido = int(input('Tente acertar o número de 0 a 5 que o programa gerou automaticamente: '))
if número_escolhido == número:
    print(f'O número que o programa sorteou foi {número}, você acertou!! ')

else: print(f'O número que o programa sorteou foi {número}, você errou!! ')

if número_escolhido >= 6: 
    print(f'Aliás, o número tinha que ser até 5 e você escolheu {número_escolhido}. leia de novo.')
