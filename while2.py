#praticando while 

total_numeros = 0
par = 0
ímpar = 0
n = 1

while n != 0:
    n = int(input('Digite um número (digite 0 para sair): '))
    if n != 0:
        total_numeros += 1
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1

print(f'Você digitou {total_numeros} números. Entre eles, {par} são pares e {ímpar} são ímpares.')