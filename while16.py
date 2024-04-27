#praticando while

soma = 0
continuar = ''
vezes = 0

while continuar != 'N':
    num = int(input('Digite um número: '))
    vezes += 1
    soma += num
    continuar = str(input('Quer continuar? S/N ')) .strip() .upper()

    if vezes == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

média = soma / vezes
print(f'Você digitou {vezes} números. A média deles é {média}, o maior número digitado foi o {maior} e o menor foi o {menor}')
