#aprendendo a usar acumulador e contador
qnt_números = int(input('Digite quantos números quer utilizar no for para realizarmos a soma deles: '))
cont = 0
soma = 0
for i in range(0, qnt_números, 1):
    i = int(input('Digite um número: '))
    cont += 1  #a cada rodada do laço, adicionará 1 a variável, no final resultando na quantidade de números que foram passados para o programa.
    soma += i #a cada rodada do laço, adicionará o valor de I a variável, sendo I o valor de cada número passado pelo usuario, consequentemente sendo somados um por um por eles mesmos.

print(f'Você nos passou {cont} números, e a soma deles ficou em: {soma}')

    
