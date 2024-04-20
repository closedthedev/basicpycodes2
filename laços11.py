#praticando ainda mais sobre acumulador e contador, agora só somando os ímpares de 0 a 100


cont = 0
soma = 0
for i in range(0, 100, 1):
    cont += 1 # a cada rodada do for, adiciona 1 a variável, no final resultando no valor de números solicitados

    if i % 2 != 0:
        print(i)
        soma += i 
     
     
    

print(f'Você nos passou {cont} números, e a soma APENAS dos pares ficou em: {soma}')
