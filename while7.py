#praticando while, dessa vez fazendo o fatorial do número escolhido no programa

import math


escolha = 1 
n_fatorados = 0

while escolha != 0:
    escolha = int(input('Digite um número para calcularmos o fatorial, digite 0 para sair.'))
    resultado = math.factorial(escolha)
    n_fatorados += 1
    print(f'Você escolheu fatoriar o número {escolha}. O resultado é: {resultado}. Esse é o {n_fatorados}ª número que você fatora.')