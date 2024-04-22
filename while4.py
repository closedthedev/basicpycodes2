#praticando while, colocando o usuário num looping até ele digitar o número 0, e quando ele digitar 0 o programa irá multiplicar todos os números que foram digitados anteriormente
n = 1
tentativas = 0
numero = 1



while numero != 0:
    numero = int(input('Digite um número. Digite 0 para encerrar a multiplicação: '))
    
    if numero != 0:
        tentativas += 1
        n = n * numero
    
    
        

print(f'Você colocou um número diferente de ZERO {tentativas} vezes. Eles multiplicados entre eles ficou em: {n}')
