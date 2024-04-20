

qnt_pessoas = int(input('Quantas pessoas você  quer analisar o peso? '))
maior = 0
menor = 0

for p in range(1, qnt_pessoas + 1):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso solicitado foi de {maior:.1f}kg, e o menor foi de {menor:.1f}kg.')


