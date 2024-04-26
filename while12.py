#praticando while, quando a soma dos números chegarem a 999, a contagem finaliza

cont = 0
soma = 0
print(('Digite alguns números. Quando a contagem deles chegar em 999, a contagem finaliza e o programa é encerrado. '))
while soma <= 999:
    num = int(input('Digite um número: '))
    soma += num
    print(f'A soma está em {soma}')
    if soma > 999:
        print(f'Você já ultrapassou os 999, a soma finalizou em {soma}.')
