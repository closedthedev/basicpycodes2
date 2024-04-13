#praticado condicionais

import string

velocidade = float(input('A quantos km/h você estava quando ultrapassou o radar? '))
velocidadelimite = float(input('O limite da pista é de quantos km/h ?  '))
velocidade_excedente = abs(velocidadelimite - velocidade)
multa = velocidade_excedente * 7


if velocidade <= velocidadelimite:
    print(f'Você ultrapassou o radar a {velocidade}km/h, respeitando o limite de velocidade que é de {velocidadelimite}km/h. Logo, você respeitou o limite e não será multado.')
else:
    print(f'Você ultrapassou o radar a {velocidade}km/h, não respeitando o limite de velocidade, que é de {velocidadelimite}km/h. Logo, pagará uma multa de R$7.00 a cada km/h acima do limite, que no seu caso foram {velocidade_excedente}km/h. Sua multa será de R${multa}.')


   

