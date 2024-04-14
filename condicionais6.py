#simulador de passagem de ônibus para viagens longas

distância = float(input('Quantos km de distância irá percorrer nessa viagem?'))

if distância <= 200:
    print(f'A passagem custará R${distância * 0.5:.2f}')

else: print(f'A passagem custará R${distância * 0.45:.2f}')