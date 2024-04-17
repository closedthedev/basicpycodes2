#primeiro uso de laços de repetição, com uma contagem regressiva para fogos

import time

print('O ano novo começa em:')
for segundo in range(10 , 0 , -1): #vai começar em 10 e terminar no 1, com um pulo de 1 em 1.
 
    print(segundo)
    time.sleep(1) #intervalo de 1s de um para outro

print('Feliz ano novo!')