#aprendendo mais sobre contador e acumulador, agora vendo se o numero é primo. basicamente, o numero é primo quando ele so é divisivel por 1 e por ele mesmo.


num = int(input('Digite um número: '))
cont = 0



for i in range(1, num + 1, 1 ):
    if num % i == 0:
        cont += 1

if cont == 2:
    print(f'O número {num} foi dividido {cont} vezes, então ele é primo. ')

else: print(f'O número {num} foi dividido {cont} vezes, então ele não é primo. ')



