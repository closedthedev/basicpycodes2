#praticando ainda mais sobre acumulador e contador, agora só somando os pares

qnt_números = int(input('Digite quantos números quer utilizar no for para realizarmos a soma deles: '))
cont = 0
soma = 0
for i in range(0, qnt_números, 1):
    cont += 1 
    i = int(input('Digite um número: '))
    if i % 2 == 0:
     soma += i 
     
    

print(f'Você nos passou {cont} números, e a soma APENAS dos pares ficou em: {soma}')
