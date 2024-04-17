#fazendo um programa que me amostre todos os múltiplos de 3 (de 1 a 500) que são ímpares e faça a soma de todos eles

soma = 0
contagem = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0: #descobrindo os números que são múltiplos de 3. todos que  a divisão por 3 resulte no resto 0, são múltiplos dele.
        soma = soma +  numero #irá somar número por número, por exemplo os primeiros multiplos sao o proprio 3, depois o 6 e depois o nove, a soma deles é 15, e por ai vai...
        contagem = contagem + 1 #irá fazer com que, a cada vez que o contador encontrar um múltiplo de 3, adicione 1. temos 83 múltiplos na faixa solicitada, por isso nossa contagem fica em 83.

print(f'A soma de todos os {contagem} números solicitados é de  {soma}.')