#praticando while, fazendo com que o programa se interrompa quando chegar em 999, mostrando quantos números foram digitados e a soma entre eles
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n

    if n == 999:
        break
print(f'Você digitou {cont} números, e a soma entre eles é {soma}')