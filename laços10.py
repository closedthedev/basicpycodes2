#praticando ainda mais sobre acumulador e contador, agora só somando os pares

qnt_números = int(input('Digite quantos números quer utilizar no for para realizarmos a soma deles: '))
cont = 0
soma = 0
for i in range(0, qnt_números, 1):
    cont += 1 # a cada rodada do for, adiciona 1 a variável, no final resultando no valor de números solicitados
    i = int(input('Digite um número: '))
    if i % 2 == 0: #basicamente, se o valor da rodada do laço (I) for divisível por 2 (ele ser um número par) o valor de I será adicionado a variável soma.
     soma += i 
     
    

print(f'Você nos passou {cont} números, e a soma APENAS dos pares ficou em: {soma}')
